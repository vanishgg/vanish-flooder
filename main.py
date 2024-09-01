from assets import *
from assets.utility.util import *



async def spam(token, uid, message, count, rs, rm, em):
    inte = discord.Intents.all()
    client = discord.Client(intents=inte)

    @client.event
    async def on_ready():
        await asyncio.sleep(0.5)
        print(f"{datetime.now().strftime(f'{blue}[{r}{d}%H{r}{w}:{r}{d}%M{r}{w}:{r}{d}%S{r}{blue}]{r}')}    {w}[{r}{blue}/{r}{w}]{r}      {d}->{r}    {Colors.blue_to_white(f'Logged in as')} ({d}{client.user.name}{r})")
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
                print(f"{datetime.now().strftime(f'{c}[{r}{d}%H{r}{w}:{r}{d}%M{r}{w}:{r}{d}%S{r}{c}]{r}')}    {w}[{c}+{r}{w}]{r}      {d}->{r}    {Colors.mint(f'Sent DM ~ {message}')} ({d}{client.user.name}{r})")

            except discord.Forbidden:
                print(f"{datetime.now().strftime(f'{red}[{r}{d}%H{r}{w}:{r}{d}%M{r}{w}:{r}{d}%S{r}{red}]{r}')}  {w}[{red}-{r}{w}]{r}      {d}->{r}    {Colors.red_to_white(f'{tar.name} DMs are closed')} ({d}{client.user.name}{r})")
                continue

    await client.start(token)




    

async def main():
    tokens = load_tokens()
    set_t(f'Vanish Flooder ~ Loaded {len(tokens)} tokens')
    clr()
    logo()
    option = input(f'            {c}[~] $Choice ~{r} ')

    if option == "1":
        print()
        tokens = open('input/tokens.txt', 'r').read().splitlines()


        uid = input(Colors.mint("Vanish@cmd$~ → User Id ~ "))
        if uid == '':
            await main()
        message = input(Colors.mint("Vanish@cmd~  → Message ~ "))
        if message == '':
            await main()
        count = int(input(Colors.mint("Vanish@cmd$~ → Amount ~ ")))
        if count == '':
            await main()        
        rs = input(Colors.mint("Vanish@cmd$~ → Random String (y/n) ~ ")).strip().lower() == 'y'
        if rs == '':
            await main()        
        rm = input(Colors.mint("Vanish@cmd$~ → Random Emojis (y/n) ~ ")).strip().lower() == 'y'
        if rm == '':
            await main()
        em = 5
        if rm:
            em = int(input(Colors.mint("Vanish@cmd$~ → Emoji Amount ~ ")))
        if em == '':
            await main()

        tasks = [spam(token, uid, message, count, rs, rm, em) for token in tokens]
        await asyncio.gather(*tasks)

    elif option == "2":
        print('exiting..')
        exit()

if __name__ == "__main__":
    asyncio.run(main())
