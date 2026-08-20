@echo off
REM Gera o executavel TranscritorDeVideo.exe (rodar este script no Windows)

python -m venv venv
call venv\Scripts\activate.bat

pip install --upgrade pip
pip install -r requirements.txt

pyinstaller --onefile --windowed --name "TranscritorDeVideo" ^
  --collect-all numpy ^
  --collect-all ctranslate2 ^
  --collect-all av ^
  --collect-all tokenizers ^
  --collect-all faster_whisper ^
  --collect-all huggingface_hub ^
  --collect-all requests ^
  --collect-all urllib3 ^
  --collect-all certifi ^
  --collect-all charset_normalizer ^
  --collect-all idna ^
  --collect-all filelock ^
  --collect-all fsspec ^
  --collect-all tqdm ^
  --collect-all packaging ^
  --collect-all yaml ^
  --collect-all truststore ^
  transcritor_video.py

echo.
echo Pronto! O executavel esta em dist\TranscritorDeVideo.exe
pause
