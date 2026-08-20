# Transcritor de Vídeo

Interface bem simples para transcrever vídeos em português: escolher o vídeo, clicar em
"Transcrever" e salvar o texto em um arquivo `.txt`.

A transcrição roda 100% localmente no computador (usando o modelo Whisper via
[faster-whisper](https://github.com/SYSTRAN/faster-whisper)) — não precisa de chave de API, de
pagamento nem de internet: o modelo de transcrição já vem embutido dentro do `.exe`.

## Link para baixar (mande este link para ela)

O programa é gerado automaticamente pelo GitHub Actions (em uma máquina Windows) e publicado como
Release pública neste repositório, como um `.zip` (executável + pastas de apoio com as
bibliotecas — mais rápido para abrir e menos sujeito a bloqueio de antivírus do que um `.exe`
único autoextraível). Ela não precisa de conta no GitHub, é só clicar no link:

**https://github.com/grigorycastro/grigorycastro/releases/latest/download/TranscritorDeVideo.zip**

Esse link é fixo: sempre baixa a versão mais recente, mesmo quando o programa for atualizado no
futuro. (O build leva alguns minutos para ficar pronto depois de um push — veja o andamento em
https://github.com/grigorycastro/grigorycastro/actions.)

## Passo a passo para ela (usuária comum do Windows)

1. Clicar no link acima para baixar o arquivo `TranscritorDeVideo.zip`.
2. Clicar com o botão direito no arquivo baixado e escolher **"Extrair Tudo..."** (ou
   **"Extrair aqui"**), criando uma pasta `TranscritorDeVideo`.
3. Abrir essa pasta e dar duplo clique em `TranscritorDeVideo.exe` (o ícone do programa — os outros
   arquivos e a pasta `_internal` ao lado são bibliotecas de apoio, não precisa mexer neles).
4. O Windows pode mostrar um aviso de "arquivo não é baixado com frequência" ou o SmartScreen pode
   avisar "O Windows protegeu seu PC" — isso é normal para um programa novo sem assinatura digital
   paga. Clicar em **"Mais informações"** e depois em **"Executar assim mesmo"**.
5. Clicar em **"Escolher vídeo..."** e selecionar o arquivo de vídeo.
6. Clicar em **"Transcrever"** e aguardar (pode levar alguns minutos, dependendo do tamanho do
   vídeo e do computador). Não precisa de internet — o modelo já vem dentro do programa.
7. Clicar em **"Salvar como .txt"** para salvar a transcrição onde ela quiser.

Dica: depois de extrair, ela pode criar um atalho do `TranscritorDeVideo.exe` na Área de Trabalho
(botão direito no arquivo → "Enviar para" → "Área de trabalho (criar atalho)") para abrir mais
fácil da próxima vez — mas a pasta original não pode ser apagada nem movida sem o atalho junto.

## Como gerar o executável manualmente (opcional)

Isso já acontece sozinho pelo GitHub Actions a cada atualização do código, mas se quiser gerar
localmente em um Windows com [Python 3.10+](https://www.python.org/downloads/):

1. Copie a pasta `transcritor-video` para o computador Windows.
2. Dê duplo clique em `build.bat` (ou rode-o em um terminal).
3. O programa aparece em `dist\TranscritorDeVideo\TranscritorDeVideo.exe`, e um `.zip` pronto para
   distribuir aparece em `TranscritorDeVideo.zip`.

## Observações

- A pasta/zip é grande (mais de 500 MB) porque o modelo de transcrição vem embutido dentro dela —
  é proposital, assim o programa funciona sem internet e sem depender de antivírus/firewall
  liberarem acesso à Hugging Face.
- Para vídeos longos, tenha paciência: em CPUs comuns a transcrição pode demorar mais que a
  duração do próprio vídeo.
- Formatos de vídeo suportados: mp4, mkv, avi, mov, webm, m4v, wmv.
