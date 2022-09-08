@echo off
pip install pyinstaller
pip install discord_webhook
pip install requests

pyinstaller --onefile giftmainer.pyw
