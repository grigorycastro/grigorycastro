"""Transcritor de Vídeo - interface simples para transcrever vídeos em português."""

import truststore

truststore.inject_into_ssl()

import os
import queue
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

MODELO = "small"  # tiny, base, small, medium, large-v3 (maior = mais preciso e mais lento)
IDIOMA = "pt"


def caminho_do_modelo():
    """No executável, o modelo vem embutido junto (não depende de internet).
    Rodando o script direto (modo desenvolvimento), baixa da Hugging Face."""
    if getattr(sys, "frozen", False):
        return os.path.join(sys._MEIPASS, "whisper_model")
    return MODELO

TIPOS_DE_VIDEO = [
    ("Arquivos de vídeo", "*.mp4 *.mkv *.avi *.mov *.webm *.m4v *.wmv"),
    ("Todos os arquivos", "*.*"),
]


class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Transcritor de Vídeo")
        self.geometry("700x520")
        self.minsize(560, 420)

        self.caminho_video = None
        self.fila = queue.Queue()
        self.modelo_whisper = None
        self.transcrevendo = False

        self._montar_interface()
        self.after(100, self._verificar_fila)

    def _montar_interface(self):
        margem = {"padx": 12, "pady": 8}

        topo = ttk.Frame(self)
        topo.pack(fill="x", **margem)

        self.botao_escolher = ttk.Button(
            topo, text="Escolher vídeo...", command=self.escolher_video
        )
        self.botao_escolher.pack(side="left")

        self.rotulo_arquivo = ttk.Label(topo, text="Nenhum vídeo selecionado")
        self.rotulo_arquivo.pack(side="left", padx=10)

        botoes = ttk.Frame(self)
        botoes.pack(fill="x", **margem)

        self.botao_transcrever = ttk.Button(
            botoes, text="Transcrever", command=self.iniciar_transcricao, state="disabled"
        )
        self.botao_transcrever.pack(side="left")

        self.botao_salvar = ttk.Button(
            botoes, text="Salvar como .txt", command=self.salvar_transcricao, state="disabled"
        )
        self.botao_salvar.pack(side="left", padx=10)

        self.barra_progresso = ttk.Progressbar(self, mode="determinate", maximum=100)
        self.barra_progresso.pack(fill="x", **margem)

        self.rotulo_status = ttk.Label(self, text="Pronto.")
        self.rotulo_status.pack(fill="x", padx=12)

        self.caixa_texto = scrolledtext.ScrolledText(self, wrap="word", font=("Segoe UI", 11))
        self.caixa_texto.pack(fill="both", expand=True, **margem)

    def escolher_video(self):
        caminho = filedialog.askopenfilename(
            title="Escolha o vídeo", filetypes=TIPOS_DE_VIDEO
        )
        if not caminho:
            return
        self.caminho_video = caminho
        self.rotulo_arquivo.config(text=os.path.basename(caminho))
        self.botao_transcrever.config(state="normal")
        self.botao_salvar.config(state="disabled")
        self.caixa_texto.delete("1.0", tk.END)
        self.rotulo_status.config(text="Pronto para transcrever.")
        self.barra_progresso["value"] = 0

    def iniciar_transcricao(self):
        if self.transcrevendo or not self.caminho_video:
            return
        self.transcrevendo = True
        self.botao_transcrever.config(state="disabled")
        self.botao_escolher.config(state="disabled")
        self.botao_salvar.config(state="disabled")
        self.caixa_texto.delete("1.0", tk.END)
        self.barra_progresso["value"] = 0
        self.rotulo_status.config(text="Preparando o modelo de transcrição (pode demorar na primeira vez)...")

        thread = threading.Thread(target=self._transcrever_em_segundo_plano, daemon=True)
        thread.start()

    def _transcrever_em_segundo_plano(self):
        try:
            if self.modelo_whisper is None:
                from faster_whisper import WhisperModel

                self.modelo_whisper = WhisperModel(caminho_do_modelo(), device="cpu", compute_type="int8")

            self.fila.put(("status", "Transcrevendo... isso pode levar alguns minutos."))

            segmentos, info = self.modelo_whisper.transcribe(
                self.caminho_video, language=IDIOMA, beam_size=5
            )

            duracao_total = info.duration or 0
            partes_do_texto = []
            for segmento in segmentos:
                partes_do_texto.append(segmento.text.strip())
                progresso = (segmento.end / duracao_total * 100) if duracao_total else 0
                self.fila.put(("progresso", progresso, " ".join(partes_do_texto)))

            texto_final = " ".join(partes_do_texto).strip()
            self.fila.put(("concluido", texto_final))
        except Exception as erro:
            self.fila.put(("erro", str(erro)))

    def _verificar_fila(self):
        try:
            while True:
                mensagem = self.fila.get_nowait()
                tipo = mensagem[0]

                if tipo == "status":
                    self.rotulo_status.config(text=mensagem[1])
                elif tipo == "progresso":
                    _, progresso, texto_parcial = mensagem
                    self.barra_progresso["value"] = min(progresso, 100)
                    self.rotulo_status.config(text=f"Transcrevendo... {progresso:.0f}%")
                    self.caixa_texto.delete("1.0", tk.END)
                    self.caixa_texto.insert(tk.END, texto_parcial)
                elif tipo == "concluido":
                    self.barra_progresso["value"] = 100
                    self.rotulo_status.config(text="Transcrição concluída!")
                    self.caixa_texto.delete("1.0", tk.END)
                    self.caixa_texto.insert(tk.END, mensagem[1])
                    self._finalizar_transcricao(sucesso=True)
                elif tipo == "erro":
                    self.rotulo_status.config(text="Ocorreu um erro na transcrição.")
                    messagebox.showerror("Erro", f"Não foi possível transcrever o vídeo:\n{mensagem[1]}")
                    self._finalizar_transcricao(sucesso=False)
        except queue.Empty:
            pass
        finally:
            self.after(100, self._verificar_fila)

    def _finalizar_transcricao(self, sucesso: bool):
        self.transcrevendo = False
        self.botao_escolher.config(state="normal")
        self.botao_transcrever.config(state="normal")
        self.botao_salvar.config(state="normal" if sucesso else "disabled")

    def salvar_transcricao(self):
        texto = self.caixa_texto.get("1.0", tk.END).strip()
        if not texto:
            messagebox.showwarning("Aviso", "Não há transcrição para salvar.")
            return

        nome_sugerido = "transcricao.txt"
        if self.caminho_video:
            base = os.path.splitext(os.path.basename(self.caminho_video))[0]
            nome_sugerido = f"{base}.txt"

        caminho_destino = filedialog.asksaveasfilename(
            title="Salvar transcrição",
            defaultextension=".txt",
            initialfile=nome_sugerido,
            filetypes=[("Arquivo de texto", "*.txt")],
        )
        if not caminho_destino:
            return

        with open(caminho_destino, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)

        messagebox.showinfo("Sucesso", "Transcrição salva com sucesso!")


if __name__ == "__main__":
    app = Aplicativo()
    app.mainloop()
