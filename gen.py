import random, string
from os import system
import time
import ctypes
import colorama
from colorama import Fore, Back, Style
colorama.init()
ctypes.windll.kernel32.SetConsoleTitleW("Nitro Gen")
print(f"{Fore.RED}")
print("""
  _   _ _ _                _____            
 | \ | (_) |              / ____|           
 |  \| |_| |_ _ __ ___   | |  __  ___ _ __  
 | . ` | | __| '__/ _ \  | | |_ |/ _ \ '_ \ 
 | |\  | | |_| | | (_) | | |__| |  __/ | | |
 |_| \_|_|\__|_|  \___/   \_____|\___|_| |_|
                                            
""")
time.sleep(2)
print("")
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

print(f"{Fore.GREEN}")
time.sleep(1)
print("codes are saved in codes.txt!")
time.sleep(1)
print("program closing in 3...")
time.sleep(1)
print("2..")
time.sleep(1)
print("1.")
time.sleep(1)
print("0")
time.sleep(1)
print(f"{Fore.BLUE}")
print("program closing!")
time.sleep(1)
