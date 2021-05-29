import random, string
from os import system
import time
import ctypes
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()
ctypes.windll.kernel32.SetConsoleTitleW("Awsome's Nitro Gen")
print(f"{Fore.RED}")
print("""
╔═╗▒╔╦══╦════╦═══╦═══╗▒▒▒▒▒▒▒▒▒▒▒▒
║║╚╗║╠╣╠╣╔╗╔╗║╔═╗║╔═╗║▒▒▒▒▒▒▒▒▒▒▒▒
║╔╗╚╝║║║╚╝║║╚╣╚═╝║║▒║║▒▒▒▒▒▒▒▒▒▒▒▒
║║╚╗║║║║▒▒║║▒║╔╗╔╣║▒║╠══╦══╦══╦══╗
║║▒║║╠╣╠╗▒║║▒║║║╚╣╚═╝╠══╩══╩══╩══╝
╚╝▒╚═╩══╝▒╚╝▒╚╝╚═╩═══╝▒▒▒▒▒▒▒▒▒▒▒▒
╔═══╦═══╦═╗▒╔╗▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
║╔═╗║╔══╣║╚╗║║▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
║║▒╚╣╚══╣╔╗╚╝║▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
║║╔═╣╔══╣║╚╗║╠══╦══╦══╦══╦══╦══╗▒▒
║╚╩═║╚══╣║▒║║╠══╩══╩══╩══╩══╩══╝▒▒
╚═══╩═══╩╝▒╚═╝▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
""")
time.sleep(2)
print("Owner: Awsome#0001 ")
time.sleep(0.5)
print("follow the instructions below   \n")
time.sleep(0.2)

num=input('how many codes to gen?: ')


f=open("codes.txt","w", encoding='utf-8')

print("Wait a few seconds!")

for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")


a_file = open("codes.txt")

lines = a_file.readlines()
for line in lines:
    print(line)


a_file.close()
