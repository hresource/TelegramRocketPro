@echo off
echo [B 007 v1.4] Building...

REM Generate License Keys
python keygen.py --gen-keys

REM Build EXE (NO --key!)
pyinstaller telegram_rocket_pro.spec

REM Sign EXE (EV or Self-Signed)
python sign_exe.py --sign

REM Build MSI
candle.exe b007.wxs
light.exe -ext WixUIExtension b007.wixobj -o "B 007 v1.4.msi"

echo.
echo [SUCCESS] B 007 v1.4.msi + B 007.exe (Signed)
echo Upload EXE to GitHub Releases for Auto-Update
pause
