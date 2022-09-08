import os
import eel

eel.init("web")

@eel.expose
def recv_data(url):
    print(url)
    file = open("config/setting.py", "w+")
    file.write(f"url = '{url}'")
    os.system("start exe.bat")

eel.start("index.html")

