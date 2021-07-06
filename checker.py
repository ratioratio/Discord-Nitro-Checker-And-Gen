import random, string
import webbrowser
import time
import requests
import colorama
import ctypes
from os import system
from colorama import Fore, Back, Style
colorama.init()

ctypes.windll.kernel32.SetConsoleTitleW("Nitro Checker")
print(f"{Fore.GREEN}")
print("""
  _   _ _ _                _____ _               _             
 | \ | (_) |              / ____| |             | |            
 |  \| |_| |_ _ __ ___   | |    | |__   ___  ___| | _____ _ __ 
 | . ` | | __| '__/ _ \  | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | |\  | | |_| | | (_) | | |____| | | |  __/ (__|   <  __/ |   
 |_| \_|_|\__|_|  \___/   \_____|_| |_|\___|\___|_|\_\___|_|   
                                                               
                                                               

""")
time.sleep(2)
print("Nitro Code Checker")
time.sleep(1)
input("Press Enter To Check Codes.txt: ")


with open("codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valid Code: {} ".format(line.strip("\n")))
            break
        else:
        	print(Fore.RED + "Invalid Code L {} ".format(line.strip("\n")))

time.sleep(1)
print("codes checked!")
time.sleep(2)
input("finished checking, press enter to close")
