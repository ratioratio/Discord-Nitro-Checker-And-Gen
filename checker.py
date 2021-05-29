import random, string
import webbrowser
import time
import requests
import ctypes
from os import system


print("""
╔═╗░╔╗╔╗░░░░░░░░░░░░░░░░░░░░░░░░░
║║╚╗║╠╝╚╗░░░░░░░░░░░░░░░░░░░░░░░░
║╔╗╚╝╠╗╔╬═╦══╗░░░░░░░░░░░░░░░░░░░
║║╚╗║╠╣║║╔╣╔╗╠══╦══╦══╦══╦══╦══╗░
║║░║║║║╚╣║║╚╝╠══╩══╩══╩══╩══╩══╝░
╚╝░╚═╩╩═╩╝╚══╝░░░░░░░░░░░░░░░░░░░
╔═══╦╗░░░░░░░╔╗░░░░░░░░░░░░░░░░░░
║╔═╗║║░░░░░░░║║░░░░░░░░░░░░░░░░░░
║║░╚╣╚═╦══╦══╣║╔╦══╦═╗░░░░░░░░░░░
║║░╔╣╔╗║║═╣╔═╣╚╝╣║═╣╔╩═╦══╦══╦══╗
║╚═╝║║║║║═╣╚═╣╔╗╣║═╣╠══╩══╩══╩══╝
╚═══╩╝╚╩══╩══╩╝╚╩══╩╝░░░░░░░░░░░░


""")
time.sleep(2)
print("made by awsome#0001")
time.sleep(1)
input("press any key to start checking:")


with open("codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valid | {} ".format(line.strip("\n")))
            break
        else:
        	print(" Invalid | {} ".format(line.strip("\n")))
input("The end! Press Enter 5 times to close the program.")
input("4")
input("3")
input("2")
input("1")
