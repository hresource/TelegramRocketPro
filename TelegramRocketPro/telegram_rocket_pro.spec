# telegram_rocket_pro.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None  # <-- REMOVED

a = Analysis(
    ['telegram_rocket_pro.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('config.json', '.'),
        ('countries.json', '.'),
        ('proxies.txt', '.'),
        ('saas_dashboard.py', '.'),
        ('public_key.pem', '.'),
    ],
    hiddenimports=[
        'telethon', 'selenium', 'webdriver_manager', 'socks',
        'schedule', 'streamlit', 'sqlite3', 'tkinter', 'rsa', 'requests'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,  # <-- REMOVED
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='B 007',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='007.ico',
    uac_admin=True
)
