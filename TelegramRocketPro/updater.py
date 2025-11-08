# updater.py
import os
import sys
import requests
import subprocess
import tempfile
from PyUpdater import PyUpdater

def check_for_update():
    updater = PyUpdater(
        name='TelegramRocketPro',
        version='4.0',
        url='https://github.com/hresource/TelegramRocketPro/releases/latest/download/'
    )
    if updater.update_available():
        print("[UPDATE] New version found! Downloading...")
        if messagebox.askyesno("Update Available", "New version v4.0 detected.\nUpdate now?"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".exe") as tmp:
                tmp.write(requests.get(updater.latest_url).content)
                tmp_path = tmp.name
            subprocess.Popen([tmp_path])
            sys.exit(0)
    else:
        print("[UPDATE] Up to date.")