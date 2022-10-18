from .etc.collors import *
def LoadWordlists(locales):
    try:
        with open(locales, "r") as W:
            arquivo  = W.read().split("\n")
            return arquivo
    except:
        print(RED+"-"*30+"sorry! i can't find the wordlist"+"-"*30)
        print(RESET)
        exit()          