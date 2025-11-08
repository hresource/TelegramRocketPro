@echo off
echo Building EXE...
pyinstaller --key=your_secret_key telegram_rocket_pro.spec

echo Collecting artifacts...
pyupdater collect

echo Signing...
pyupdater pkg --process --sign

echo Uploading to GitHub...
pyupdater upload --service github

echo Done! New version live.
pause