# Transcritor de Vídeo

Interface bem simples para transcrever vídeos em português: escolher o vídeo, clicar em
"Transcrever" e salvar o texto em um arquivo `.txt`.

A transcrição roda localmente no computador (usando o modelo Whisper via
[faster-whisper](https://github.com/SYSTRAN/faster-whisper)) — não precisa de chave de API nem de
pagamento. Só é necessário ter internet na primeira vez que o programa rodar, para baixar o modelo
de transcrição (depois disso funciona offline).

## Como gerar o executável (.exe) para Windows

O `.exe` precisa ser gerado em um computador Windows (não é possível gerar um `.exe` do Windows a
partir de Linux/Mac). Passos, em um Windows com [Python 3.10+](https://www.python.org/downloads/)
instalado:

1. Copie a pasta `transcritor-video` para o computador Windows.
2. Dê duplo clique em `build.bat` (ou rode-o em um terminal).
3. Aguarde a instalação e a geração do executável — vai aparecer em `dist\TranscritorDeVideo.exe`.
4. Copie `TranscritorDeVideo.exe` para o computador da sua esposa. Não precisa instalar Python nem
   mais nada nela — é só dar duplo clique no `.exe`.

## Como usar o programa

1. Abrir `TranscritorDeVideo.exe`.
2. Clicar em **"Escolher vídeo..."** e selecionar o arquivo de vídeo.
3. Clicar em **"Transcrever"** e aguardar (pode levar alguns minutos, dependendo do tamanho do
   vídeo e do computador).
4. Clicar em **"Salvar como .txt"** para salvar a transcrição.

## Observações

- Na primeira transcrição, o programa baixa o modelo de linguagem (alguns centenas de MB) — é
  necessário estar conectado à internet nesse momento.
- Para vídeos longos, use um computador com internet estável na primeira execução e tenha
  paciência: em CPUs comuns a transcrição pode demorar mais que a duração do próprio vídeo.
- Formatos de vídeo suportados: mp4, mkv, avi, mov, webm, m4v, wmv.
