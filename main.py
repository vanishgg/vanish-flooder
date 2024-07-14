# ~~ Imports ~~ #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             # no rat here. u thought tho i bet LMAO

import discord
import asyncio
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore, Style
import os
import random
from datetime import datetime

# ~~ Colors ~~ #

c = "\033[38;2;25;25;112m"
d = "\033[1;90m"
black = "\033[1;30m"
red = "\033[1;31m"
blue = "\033[1;34m"
w = "\033[1;37m"
r = Style.RESET_ALL

# ~~ Source (do not mess with unless you know what you are doing) ~~ #

emj = "stuff/emojis.txt"

def tkns():
    if os.path.exists('input/tokens.txt'):
        with open('input/tokens.txt', 'r') as file:
            tokens = [line.strip() for line in file.readlines()]
            return tokens, len(tokens)
    return [], 0

tokens, tok = tkns()

def cc():
        os.system('cls')

def emo():
    if os.path.exists(emj):
        with open(emj, 'r', encoding='utf-8') as file:
            emojis = [line.strip() for line in file.readlines()]
            return emojis
    return []

emojis = emo()

async def spam(token, uid, message, count, rs, rm, em):
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        await asyncio.sleep(1)
        print(f"{datetime.now().strftime(f'{c}[{r}{d}%H{r}{w}:{r}{d}%M{r}{w}:{r}{d}%S{r}{c}]{r}')}    {blue}[+]{Style.RESET_ALL}      {d}->{r}    {c}Logged in as{r} {d}{client.user.name}{r}")
        await asyncio.sleep(1)
        tar = await client.fetch_user(int(uid))

        for _ in range(count):
            try:
                msg = message
                if rs:
                    msg += " -> " + ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=25))

                if rm:
                    msg += " -> " + ' '.join(random.choices(emojis, k=em))
        
                await tar.send(msg)
                await asyncio.sleep(0.5)
                print(f"{datetime.now().strftime(f'{c}[{r}{d}%H{r}{w}:{r}{d}%M{r}{w}:{r}{d}%S{r}{c}]{r}')}    {blue}[+]{Style.RESET_ALL}      {d}->{r}    {c}Sent DM{r} ~ {green}{message}{r} ({d}{client.user.name}{r})")

            except discord.Forbidden:
                print(f"{datetime.now().strftime(f'{c}[{r}{d}%H{r}{w}:{r}{d}%M{r}{w}:{r}{d}%S{r}{c}]{r}')}  {red}[-]{Style.RESET_ALL}      {d}->{r}    {tar.name} DMs are closed ({client.user.name})")
                continue

        await client.close()

        await client.start(token)

def logo():
    nn = Center.XCenter(f"""
{c}
                                                        
 _____         _     _      _____ _           _         
|  |  |___ ___|_|___| |_   |   __| |___ ___ _| |___ ___ 
|  |  | .'|   | |_ -|   |  |   __| | . | . | . | -_|  _|
 \___/|__,|_|_|_|___|_|_|  |__|  |_|___|___|___|___|_|   
 {r}
    """)
    print(nn)

async def main():
    cc()
    logo()
    print(f'                                               {w}Loaded:{r} {c}‹{r}{w}{tok}{r}{c}›{r} {w}tokens') 
    print(f"""
                                            {c}[{r}1{c}]{r} {w} Dm Spam     {c}[{r}2{c}]{r} {w} Exit
    """) 
    option = input(f'            {c}[~] $Choice ~{r} ')

    if option == "1":
        print()
        tokens = open('input/tokens.txt', 'r').read().splitlines()
        uid = input(Colorate.Horizontal(Colors.blue_to_white, "Vanish@cmd$~ → User Id ~ "))
        if uid == '':
            await main()
        message = input(Colorate.Horizontal(Colors.blue_to_white, "Vanish@cmd~ → Message ~ "))
        if message == '':
            await main()
        count = int(input(Colorate.Horizontal(Colors.blue_to_white, "Vanish@cmd$~ → Amount ~ ")))
        if count == '':
            await main()        
        rs = input(Colorate.Horizontal(Colors.blue_to_white, "Vanish@cmd$~ → Random String (y/n) ~ ")).strip().lower() == 'y'
        if rs == '':
            await main()        
        rm = input(Colorate.Horizontal(Colors.blue_to_white, "Vanish@cmd$~ → Random Emojis (y/n) ~ ")).strip().lower() == 'y'
        if rm == '':
            await main()
        em = 5
        if rm:
            em = int(input(Colorate.Horizontal(Colors.blue_to_white, "Vanish@cmd$~ → Emoji Amount ~ ")))
        if em == '':
            await main()

        tasks = [spam(token, uid, message, count, rs, rm, em) for token in tokens]
        await asyncio.gather(*tasks)

    elif option == "2":
        print('exiting..')
        exit()

if __name__ == "__main__":
    cc()
    asyncio.run(main())

# ~~ the end ~~ #
####################################
# made by virtual                  #
# if u paid for this u got scammed #
# no rat here check!               #
####################################                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        # dw no rat!
