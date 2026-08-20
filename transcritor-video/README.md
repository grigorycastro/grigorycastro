# Transcritor de Vídeo

Interface bem simples para transcrever vídeos em português: escolher o vídeo, clicar em
"Transcrever" e salvar o texto em um arquivo `.txt`.

A transcrição roda 100% localmente no computador (usando o modelo Whisper via
[faster-whisper](https://github.com/SYSTRAN/faster-whisper)) — não precisa de chave de API, de
pagamento nem de internet: o modelo de transcrição já vem embutido dentro do `.exe`.

## Link para baixar (mande este link para ela)

O `.exe` é gerado automaticamente pelo GitHub Actions (em uma máquina Windows) e publicado como
Release pública neste repositório. Ela não precisa de conta no GitHub, é só clicar no link:

**https://github.com/grigorycastro/grigorycastro/releases/latest/download/TranscritorDeVideo.exe**

Esse link é fixo: sempre baixa a versão mais recente, mesmo quando o programa for atualizado no
futuro. (O build leva alguns minutos para ficar pronto depois de um push — veja o andamento em
https://github.com/grigorycastro/grigorycastro/actions.)

## Passo a passo para ela (usuária comum do Windows)

1. Clicar no link acima para baixar o arquivo `TranscritorDeVideo.exe`.
2. O Windows/navegador pode mostrar um aviso de "arquivo não é baixado com frequência" ou o
   SmartScreen pode avisar "O Windows protegeu seu PC" — isso é normal para um `.exe` novo sem
   assinatura digital paga. Clicar em **"Mais informações"** e depois em **"Executar assim mesmo"**.
3. Dar duplo clique no arquivo para abrir o programa (não precisa instalar nada).
4. Clicar em **"Escolher vídeo..."** e selecionar o arquivo de vídeo.
5. Clicar em **"Transcrever"** e aguardar (pode levar alguns minutos, dependendo do tamanho do
   vídeo e do computador). Não precisa de internet — o modelo já vem dentro do programa.
6. Clicar em **"Salvar como .txt"** para salvar a transcrição onde ela quiser.

## Como gerar o executável manualmente (opcional)

Isso já acontece sozinho pelo GitHub Actions a cada atualização do código, mas se quiser gerar
localmente em um Windows com [Python 3.10+](https://www.python.org/downloads/):

1. Copie a pasta `transcritor-video` para o computador Windows.
2. Dê duplo clique em `build.bat` (ou rode-o em um terminal).
3. O executável aparece em `dist\TranscritorDeVideo.exe`.

## Observações

- O `.exe` é grande (mais de 500 MB) porque o modelo de transcrição vem embutido dentro dele — é
  proposital, assim o programa funciona sem internet e sem depender de antivírus/firewall
  liberarem acesso à Hugging Face.
- Para vídeos longos, tenha paciência: em CPUs comuns a transcrição pode demorar mais que a
  duração do próprio vídeo.
- Formatos de vídeo suportados: mp4, mkv, avi, mov, webm, m4v, wmv.
