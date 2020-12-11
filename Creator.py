from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import requests
import undetected_chromedriver as uc
import pyautogui
from pynput.mouse import Button, Controller
import os
import re
import json
from urllib.request import Request, urlopen
import win32com.client as comctl
import pyperclip
import sys
import ctypes
from colorama import init, Fore, Style, Back
import colorama
from discord_webhook import DiscordWebhook
import json
from urllib.request import Request, urlopen

ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Creator V0.5")
colorama.init()

with open('config.json') as f:
    config = json.load(f)

tokenwebhook = config.get('tokenwebhook')
detailswebhook = config.get('detailswebhook')


nordsmallx = config.get('Nord Vpn Small Icon X Position')
nordsmally = config.get('Nord Vpn Small Icon Y Position')

nordonx = config.get('Nord Vpn On Button X Position')
nordony = config.get('Nord Vpn On Button Y Position')

nordoffx = config.get('Nord Vpn Off Button X Position')
nordoffy = config.get('Nord Vpn Off Button Y Position')


wsh = comctl.Dispatch("WScript.Shell")

months = ['December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']

selection_month = random.choice(months)
selection_day = random.randint(1,28)

m = Controller()

r2 = requests.get('http://names.drycodes.com/50')
fem = r2.json()


text = f"""{Fore.RED}


                         _____  _                       _    _____                _             
                        |  __ \(_)                     | |  / ____|              | |            
                        | |  | |_ ___  ___ ___  _ __ __| | | |     _ __ ___  __ _| |_ ___  _ __ 
                        | |  | | / __|/ __/ _ \| '__/ _` | | |    | '__/ _ \/ _` | __/ _ \| '__|
                        | |__| | \__ \ (_| (_) | | | (_| | | |____| | |  __/ (_| | || (_) | |   
                        |_____/|_|___/\___\___/|_|  \__,_|  \_____|_|  \___|\__,_|\__\___/|_|   
                        
                                                     
                                                  {Fore.RESET}{Fore.RED}   Made by Jonah {Fore.RESET}                                                                                                                                                                                                                                                                                                                            
"""



def main():
    #nordvpn
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(nordsmallx, nordsmally)
    m.click(Button.right, 1)
    time.sleep(.4)
    pyautogui.moveTo(nordonx, nordony) # on button 
    m.click(Button.left, 1)
    time.sleep(.4)
    pyautogui.moveTo(nordoffx, nordoffy) # of button to on 
    m.click(Button.left, 1)
    time.sleep(5)
    email =  random.choice(lines)
    date = random.randint(1970, 2002)
    passwordinput = random.randint(2000000,353434353453)
    driver = uc.Chrome()
    start = time.time()
    driver.get("https://discord.com/register")
    os.system('cls')
    print(text)
    enter_searchbar = driver.find_element_by_name("email")
    enter_searchbar.send_keys(email)
    enter_user = driver.find_element_by_name("username")
    enter_user.send_keys(f"{username}")
    enter_passwd = driver.find_element_by_name("password")
    enter_passwd.send_keys(passwordinput)
    enter_month = driver.find_element_by_id("react-select-2-input")
    enter_month.send_keys(selection_month, Keys.ENTER)
    enter_day = driver.find_element_by_id("react-select-3-input")
    enter_day.send_keys(selection_day, Keys.ENTER)
    enter_year = driver.find_element_by_id("react-select-4-input")
    enter_year.send_keys(date, Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath("//input[@class='inputDefault-3JxKJ2 input-3ITkQf']").click()
    driver.find_element_by_xpath("//button[@type='submit']").click()
    os.system('cls')
    print(text)

    pyautogui.moveTo(1789, 374)
    time.sleep(2)
    m.click(Button.left, 2)
    time.sleep(.8)
    pyautogui.moveTo(618, 668) # click on cap 
    m.click(Button.left, 1)
    print(f"\n    [{Fore.MAGENTA}>{Fore.RESET}] Type enter when you're done with the captcha! ", end='')
    captdone = input()
    os.system("cls")
    if captdone == captdone:

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Host': 'discord.com',
            'Accept': '*/*',
            'Accept-Language': 'en-US',
            'Content-Type': 'application/json',
            'Referer': 'https://discord.com/register',
            'Origin': 'https://discord.com',
            'DNT': '1',
            'Connection': 'keep-alive',
        }

        json = {
            'email': email,
            'password': passwordinput,
        }

        esafaf = requests.post('https://discord.com/api/v6/auth/login', headers=headers, json=json)
        rab = esafaf.json()


        time.sleep(.3)
        token = rab['token']
        end = time.time()
        print(text)
        print(f"    [{Fore.GREEN}+{Fore.RESET}] Account made, token is: {Fore.RED}{rab['token']}{Fore.RESET}\n", end='')
        print(f"    [{Fore.GREEN}+{Fore.RESET}] Email: {email} {Fore.RED}{Fore.RESET}\n", end='')
        print(f"    [{Fore.GREEN}+{Fore.RESET}] Username: {username} {Fore.RED}{Fore.RESET}\n", end='')
        print(f"    [{Fore.GREEN}+{Fore.RESET}] Password: {passwordinput} {Fore.RED}{Fore.RESET}\n", end='')
        driver.quit()
        webhook = DiscordWebhook(url=f'{tokenwebhook}', content=f'{token}')
        response = webhook.execute()

        accdetails = f'''
        ```Email: {email}
Username: {username}
Password: {passwordinput}
Time Taken: {end - start} seconds``` '''

        details = DiscordWebhook(url=f'{detailswebhook}', content=f'{accdetails}')
        response2 = details.execute()
    




def nitrogen():
    def Nitro():
        code = ''.join(random.choices(randomness + randomnum, k=16))
        return f'https://discord.gift/{code}'
    randomness = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlkmnopqrstuvwxyz123456789'
    randomnum = '123456789'
    print(f"\n    [{Fore.MAGENTA}>{Fore.RESET}] How many discord nitro codes do you want to generate? ", end='')
    nitrocount = input()
    nitrocount = int(nitrocount)
    nitro_file = open("nitro.txt", 'a')
    nitrostart = time.time()
    try:
        for i in range(int(nitrocount)):
            nitro_file.write(Nitro() + "\n")


    except:
        while True:
            nitro_file.write(Nitro() + "\n")
    nitroend = time.time()

    fname = "nitro.txt"
    count = 0
    with open(fname, 'r') as f:
        for line in f:
            count += 1
    print()
    print(f"    [{Fore.MAGENTA}!{Fore.RESET}] Codes Generated: {nitrocount}")
    print(f"    [{Fore.MAGENTA}!{Fore.RESET}] Time Taken {nitroend -  nitrostart} seconds")
    print(f"    [{Fore.MAGENTA}!{Fore.RESET}] Total number of gifts in nitro.txt: {count} gifts")






def tokenInfo(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
            [{Fore.RED}User ID{Fore.RESET}]         {userID}
            [{Fore.RED}User Name{Fore.RESET}]       {userName}
            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}

            [{Fore.RED}Email{Fore.RESET}]           {email}
            [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else "No phone number added!"}
            [{Fore.RED}Token{Fore.RESET}]           {token}

            ''')
    else:
        print(f"[{Fore.RED}!{Fore.RESET}] The token {Fore.RED}{tokeninput}{Fore.RESET} is not a valid token!")




lines = open("emails.txt").read().splitlines()



menuchoice = f"""
    {Fore.RED}Discord Creator Menu{Fore.RESET}

    [{Fore.MAGENTA}1{Fore.RESET}] Create Accounts
    [{Fore.MAGENTA}2{Fore.RESET}] Token Checker
    [{Fore.MAGENTA}3{Fore.RESET}] Random Nitro Generator
"""
print(text)
time.sleep(2)


print(menuchoice)

print(f"    [{Fore.MAGENTA}>{Fore.RESET}] Menu Choice : ", end='')
choice = input()

if choice == "1":
    os.system('cls')
    print(text)
    print(f"\n     {Fore.RED}Discord Account Creator{Fore.RESET}")
    print(f"\n    [{Fore.MAGENTA}>{Fore.RESET}] How many accounts do you want to make? (NOTE: You need to do the captchas) ", end='')
    number = input()
    number = int(number)
    print(f"    [{Fore.MAGENTA}>{Fore.RESET}] What username do you want to use for the accounts? ", end='')
    username = input()
    print(f"\n    [{Fore.RED}!{Fore.RESET}] IMPORTANT: Do not move your mouse at all except doing captchas!", end='')
    time.sleep(1)
    for i in range(number):
        main()
elif choice == "2":
    os.system('cls')
    print(text)
    print(f"\n     {Fore.RED}Discord Token Checker{Fore.RESET}")
    print(f"\n    [{Fore.MAGENTA}>{Fore.RESET}] Input the token for the information! ", end='')
    tokeninput = input()
    os.system('cls')
    print(text)
    tokenInfo(tokeninput)

elif choice == "3":
    os.system('cls')
    print(text)
    print(f"\n     {Fore.RED}Random Nitro Generator{Fore.RESET}")
    nitrogen()





    
time.sleep(30000)



 
