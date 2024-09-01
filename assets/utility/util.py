from assets import *


c = "\033[38;2;194;255;182m"
d = "\033[1;90m"
red = "\033[1;31m"
blue = "\033[1;34m"
w = "\033[1;37m"
r = Style.RESET_ALL

def load_tokens():
    with open("input/tokens.txt", "r") as f:
        tokens = f.readlines()
        bt = [token.strip() for token in tokens if token.strip().startswith(('MT'))]
        return bt


tokens = load_tokens

def emo():
    with open('assets/get/emojis.txt', 'r', encoding='utf-8') as file:
        em = [line.strip() for line in file.readlines()]
        return em

emojis = emo()

def center(var:str, space:int=None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())


def set_t(t):
    os.system(f'title {t}')

def clr():
    os.system('cls')

def logo():
    nm = (center(fr"""
{c}                                                       
___    __             _____       ______  
__ |  / /_____ __________(_)_________  /_ 
__ | / /_  __ `/_  __ \_  /__  ___/_  __ \
__ |/ / / /_/ /_  / / /  / _(__  )_  / / /
_____/  \__,_/ /_/ /_//_/  /____/ /_/ /_/                                         
 {r}
    """))
    print(nm)
    print(f"""
                                            {c}[{r}1{c}]{r} {w} Dm Spam     {c}[{r}2{c}]{r} {w} Exit
    """) 
