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
  transcritor_video.py

echo.
echo Pronto! O executavel esta em dist\TranscritorDeVideo.exe
pause
