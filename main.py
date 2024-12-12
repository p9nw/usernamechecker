import random
import string
import requests
import os
import time
import json
from colorama import Fore, init
import datetime
from configparser import ConfigParser
import sys
init(autoreset=True)
__version__ = "Author: mk48 1.0"
__github__= "https://github.com/p9nw"
dir_path = os.path.dirname(os.path.realpath(__file__))
configur = ConfigParser()
configur.read(os.path.join(dir_path, f"config.ini"))
tokens_list = os.path.join(dir_path, f"tokens.txt")
integ_0 = 0
sys_url = "https://discord.com/api/v9/users/@me"
URL = "https://discord.com/api/v9/users/@me/pomelo-attempt"
bunny = '''
⢀⣀⠀⠀⠀⠀⠀⢀⣀⠀
⢠⣯⢬⣷⡀⠀⠀⣴⡯⢌⣧
⠸⣿⠀⠹⣷⠀⢸⡝⠀⢸⡿
⠀⠻⣧⣀⣿⣦⣼⡁⣠⣿⠃
⠀⢀⡾⠋⠀⠀⠀⠈⣙⣯⠀
⠀⣾⠀⠀⠀⠀⠀⠀⠀⠸⡆
⢰⡧⢄⢰⡆⠀⢰⡆⡠⢄⣧
⠀⠳⣼⣤⣤⣤⣤⣤⣧⠾⠁
'''
Lb = Fore.LIGHTBLACK_EX
Ly = Fore.LIGHTYELLOW_EX
Delay = configur.getfloat("config", "default_delay")

def s_sys_h():
    if configur.getboolean("sys", "MULTI_TOKEN") == True:
        return {
            "Content-Type": "Application/json",
            "Orgin": "https://discord.com/",
            "Authorization": avail_tokens(tokens_list)[integ_0]
        }
    elif configur.getboolean("sys", "MULTI_TOKEN") == False:
        return {
            "Content-Type": "Application/json",
            "Orgin": "https://discord.com/",
            "Authorization": configur.get("sys", "TOKEN")
        }
    else:
        return {
            "Content-Type": "Application/json",
            "Orgin": "https://discord.com/",
            "Authorization": configur.get("sys", "TOKEN")
        }

def sys_c_t():
    if configur.get("sys", "TOKEN") != "":
        pass
    elif configur.get("sys", "TOKEN") == "" and configur.getboolean("sys", "MULTI_TOKEN") == False:
        print(f"{Lb}[!]{Fore.RED} No token found. You must paste your token inside the 'config.ini' file, in front of the value 'TOKEN'.")
        exit()
    elif configur.getboolean("sys", "MULTI_TOKEN") == True and not avail_tokens(tokens_list)[0]:
        print(f"{Lb}[!]{Fore.RED} No tokens found. You must paste your tokens inside the 'tokens.txt' file.")
        exit()
    elif configur.getboolean("sys", "MULTI_TOKEN") is not True and configur.getboolean("sys", "MULTI_TOKEN") is not False and configur.get("sys", "TOKEN") == "":
        print(f"{Lb}[!]{Fore.RED} Invalid config detected. Please re-check the config file, `config.ini` and your settings.")
        exit()

available_usernames = []
av_list = os.path.join(dir_path, f"available_usernames.txt")
sample_0 = r"_."
def setconf():
    global string_0
    global digits_0
    global punctuation_0
    global webhook_0
    global sat_string
    global sat_digits
    global sat_multi_token
    global sat_punct
    global sat_webhook
    sat_webhook = configur.get("sys", "WEBHOOK_URL")
    sat_string = configur.getboolean("config", "string")
    sat_digits = configur.getboolean("config", "digits")
    sat_punct = configur.getboolean("config", "punctuation")
    sat_multi_token = configur.getboolean("sys", "MULTI_TOKEN")
    if sat_webhook == "":
        webhook_0 = False
    elif sat_webhook != "":
        webhook_0 = True
    if sat_string == True:
        string_0 = string.ascii_lowercase
    elif sat_string == False:
        string_0 = ""
    else:
        string_0 = string.ascii_lowercase
        sat_string = True
    if sat_digits == True:
        digits_0 = string.digits
    elif sat_digits == False:
        digits_0 = ""
    else:
        digits_0 = string.digits
        sat_digits = True
    if sat_punct == True:
        punctuation_0 = sample_0
    elif sat_punct == False:
        punctuation_0 = ""
    else:
        punctuation_0 = sample_0
        sat_punct = True
    if sat_punct == False and sat_digits == False and sat_string == False:
        punctuation_0 = sample_0
        digits_0 = string.digits
        string_0 = string.ascii_lowercase

def main():
    sys_c_t()
    os.system(f"title {__version__} - Connected as {requests.get(sys_url, headers=s_sys_h()).json()['username']}")
    s_sys_h()
    setconf()
    print(f"""{Fore.LIGHTYELLOW_EX}
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
  {__version__} 
  {__github__}                     {Fore.LIGHTCYAN_EX}Connected as {requests.get(sys_url, headers=s_sys_h()).json()['username']}{Ly}#{Fore.LIGHTCYAN_EX}{requests.get(sys_url, headers=s_sys_h()).json()['discriminator']}{Ly}
                             
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
  {bunny}  -  mk48's signature ;-)
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

.-----------------------------.
|           _    _  _    ___  |     {Fore.LIGHTCYAN_EX}1-{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}Generate names and check{Fore.LIGHTBLACK_EX}]{Ly}     
| _ __ ___ | | _| || |  ( _ ) |     {Fore.LIGHTCYAN_EX}2-{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}Check a specific list{Fore.LIGHTBLACK_EX}]{Ly}             
|| '_ ` _ \| |/ / || |_ / _ \ |
|| | | | | |   <|__   _| (_) ||      Config.ini:
||_| |_| |_|_|\_\  |_|  \___/ |      {Fore.LIGHTCYAN_EX}Digits: {Fore.YELLOW}{sat_digits}{Ly}
'-----------------------------'      {Fore.LIGHTCYAN_EX}String: {Fore.YELLOW}{sat_string}{Ly}
                                                  {Fore.LIGHTCYAN_EX}Punctuation: {Fore.YELLOW}{sat_punct}{Ly}
                                                  {Fore.LIGHTCYAN_EX}Multi-Token: {Fore.YELLOW}{sat_multi_token}{Ly}
                                                  {Fore.LIGHTCYAN_EX}Webhook: {Fore.YELLOW}{webhook_0}{Ly}
                                                  {Fore.LIGHTCYAN_EX}Delay: {Fore.YELLOW}{Delay}{Ly}
                                                          

  Discord Username's availability validator.
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
""")
    proc0()

def proc0():
    m_input = input(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}mk48{Fore.LIGHTBLACK_EX}]:> {Fore.LIGHTYELLOW_EX}").lower()
    if m_input == "exit":
        sys.exit(0)
    if m_input == "":
        proc0()
    elif m_input == "2":
        setdelay()
        opt2load()
    elif m_input == "1":
        setdelay()
        opt1load()
    else:
        print(f"{Lb}[!]{Fore.RED} Invalid input! Please enter '1' or '2'.")
        proc0()

def setdelay():
    global Delay
    print(f"{Lb}[!]{Ly} Default delay is: {Delay}s (config.ini){Lb}")
    d_input = input(f"{Lb}[{Ly}Edit Delay (Press Enter to skip){Lb}]:> ")
    if d_input == "" or d_input.isspace():
        return
    else:   
        try:
            int(d_input)
            Delay = int(d_input)
        except ValueError:
            print(f"{Lb}[!]{Fore.RED}Error: You must enter a valid integer. No strings.")
            setdelay()

def validate_names(opt, usernames):
    global available_usernames
    global integ_0
    if opt == 2:
        for username in usernames:
            body = {
                "username": username
            }
            time.sleep(Delay)
            endpoint = requests.post(URL, headers=s_sys_h(), json=body)
            json_endpoint = endpoint.json()
            if endpoint.status_code == 429 and sat_multi_token == True and len(avail_tokens(tokens_list)) != integ_0:
                integ_0 = (integ_0 + 1) % len(avail_tokens(tokens_list))
                print(f"{Lb}[!]{Ly} Token {integ_0} went rate limited. Using token index: {integ_0} connected as: {requests.get(sys_url, headers=s_sys_h()).json()['username']}#{requests.get(sys_url, headers=s_sys_h()).json()['discriminator']}")
            elif endpoint.status_code == 429 and sat_multi_token == False:
                sleep_time = endpoint.json()["retry_after"]
                print(f"{Lb}[!]{Fore.RED} Rate limit hit. Sleeping for {sleep_time}s (Discord rate limit)")
                time.sleep(sleep_time)
            if json_endpoint.get("taken") is not None:
                if json_endpoint["taken"] is False:
                    print(f"{Lb}[+]{Fore.LIGHTGREEN_EX} '{username}' available.")
                    ch_send_webhook(username)
                    save(username)
                    available_usernames.append(username)
                elif json_endpoint["taken"] is True:
                    print(f"{Lb}[-]{Fore.RED} '{username}' taken.")
            else:
                print(f"{Lb}[?]{Fore.RED} Error validating '{username}': {endpoint.json()['message']} |mk48: Make sure you have a valid token.")
    elif opt == 1:
        body = {
            "username": usernames
        }
        endpoint = requests.post(URL, headers=s_sys_h(), json=body)
        json_endpoint = endpoint.json()
        if endpoint.status_code == 429 and len(avail_tokens(tokens_list)) != integ_0 and sat_multi_token == True:
            integ_0 = (integ_0 + 1) % len(avail_tokens(tokens_list))
            print(f"{Lb}[!]{Ly} Token {integ_0} went rate limited. Using token index: {integ_0} connected as: {requests.get(sys_url, headers=s_sys_h()).json()['username']}#{requests.get(sys_url, headers=s_sys_h()).json()['discriminator']}")
        elif endpoint.status_code == 429 and sat_multi_token == False:
            sleep_time = endpoint.json()["retry_after"]
            print(f"{Lb}[!]{Fore.RED} Rate limit hit. Sleeping for {sleep_time}s (Discord rate limit)")
            time.sleep(sleep_time)
        if json_endpoint.get("taken") is not None:
            if json_endpoint["taken"] is False:
                print(f"{Lb}[+]{Fore.LIGHTGREEN_EX} '{usernames}' available.")
                ch_send_webhook(usernames)
                save(usernames)
                available_usernames.append(usernames)
            elif json_endpoint["taken"] is True:
                print(f"{Lb}[-]{Fore.RED} '{usernames}' taken.")
        else:
            print(f"{Lb}[?]{Fore.RED} Error validating '{usernames}': {endpoint.json()['message']} |mk48: Make sure you have a valid token.")
def avail_tokens(path):
    with open(path, 'r') as at:
        tokens = at.read().splitlines()
    return tokens

def save(content: str):
    with open(av_list, "a") as file:
        file.write(f"\n{content}")

def checkavail(): 
    if len(available_usernames) < 1:
        print(f"{Lb}[!]{Fore.RED} Error: No available usernames found.")
        exit()
    else:
        return

def opt2load():
    global av_list
    global dir_path
    list_path = os.path.join(dir_path, f"usernames.txt")
    print(f"{Lb}[!]{Ly}Checking 'usernames.txt' for a valid list...")
    try:
        with open(list_path) as file:
            usernames = [line.strip() for line in file]
            validate_names(2, usernames)
        checkavail()
        print(f"\n{Lb}[=]{Fore.LIGHTGREEN_EX} Done. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Available usernames, are saved in the following file: '{av_list}' .")
        exit()
    except FileNotFoundError:
        print(f"{Lb}[!]{Fore.RED} Error: Couldn't find the list (usernames.txt). Please make sure to create a valid list file in the same directory: \n({dir_path}\\)")
        exit()

def opt1load():
    opt1_input: int = input(f"{Lb}[{Ly}How many letters in a username{Lb}]:> ")
    try:
        int(opt1_input)
        if int(opt1_input) > 32 or int(opt1_input) < 2:
            print(f"{Lb}[!]{Fore.RED} Error: The username must contain at least 2 letters, and not more than 32 letters.")
            opt1load()
        opt2_input: int = input(f"{Lb}[{Ly}How many usernames to generate{Lb}]:> ")
        opt1func(int(opt2_input), int(opt1_input))
    except ValueError:
        print(f"{Lb}[!]{Fore.RED} Error: You must enter a valid integer. No strings.")
        opt1load()

def opt1func(v1, v2):
    for i in range(v1):
        name = get_names(int(v2))
        validate_names(1, name)
        time.sleep(Delay)
    checkavail()
    print(f"\n{Lb}[=]{Fore.LIGHTGREEN_EX} Done. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Available usernames, are saved in the following file: '{av_list}' .")
    exit()

def ch_send_webhook(name):
    if webhook_0 == True:
        try:
       
            embed = {
                "embeds": [{
                    "title": "we found a name",
                    "description": f"user: **{name}** is available",  
                    "color": 197085,
                    "footer": {
                        "text": "Username checker by @mk48xd\n```⢀⣀⠀⠀⠀⠀⠀⢀⣀⠀\n⢠⣯⢬⣷⡀⠀⠀⣴⡯⢌⣧\n⠸⣿⠀⠹⣷⠀⢸⡝⠀⢸⡿\n⠀⠻⣧⣀⣿⣦⣼⡁⣠⣿⠃\n⠀⢀⡾⠋⠀⠀⠀⠈⣙⣯⠀\n⠀⣾⠀⠀⠀⠀⠀⠀⠀⠸⡆\n⢰⡧⢄⢰⡆⠀⢰⡆⡠⢄⣧\n⠀⠳⣼⣤⣤⣤⣤⣤⣧⠾⠁```",  # Bunny in a code block
                    },
                }]
            }

      
            response = requests.post(sat_webhook, json=embed)
            
            if response.status_code == 204:
                print(f"{Lb}[+]{Fore.LIGHTGREEN_EX} Webhook sent successfully for {name}.")
            else:
                print(f"{Lb}[!]{Fore.RED} Failed to send webhook for {name}. Error: {response.status_code}")
                
        except Exception as e:
            print(f"{Lb}[!]{Fore.RED} Error while sending webhook: {e}")



def get_names(length):
    allchars = string_0 + digits_0 + punctuation_0
    name = ''.join(random.choice(allchars) for i in range(length))
    return name

if __name__ == "__main__":
    main()
