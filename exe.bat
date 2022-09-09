@echo off
pip install pyinstaller
pip install discord_webhook
pip install requests

cd modules

pyinstaller --onefile giftmainer.pyw
