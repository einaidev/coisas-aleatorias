import logging 
import time
import requests
from utils.etc.collors import *
from utils.wordlistLoader import LoadWordlists
import sys
from utils.getArgs import Get
from multiprocessing import Process
import threading

STARTED = """
THIS IS A BRUTE FORCE TOOL FOR DIRECTORIES AND SUB DOMAINS.          

FAQ:

ART 1.1: THIS TOOL MUST BE USED IN THE CORRECT                       
WAY, IN CASE OF ANY ERROR CHECK THE ARGUMENTS YOU PASSED.

ART 1.2: THIS TOOL MAY HAVE NEW UPDATES WITH MORE FUNCTIONALITIES.
 I WANT TO CHECK IT OUT, GO TO OUR GIT HUB AND DOWNLOAD THE LATEST
VERSION   

HELP:
-u --- give the url [--url]
-w --- inform a wordlist [--wordlist]
                                


NANDO FROM CAPUCCION TEAM ™ 2021 - 2022 ®
"""

STARTED_PT_BR = """
ESTA É UMA FERRAMENTA DE BRUTE FORCE DE DIRETÓRIOS E SUB DOMINIOS.

FAQ:

ART 1.1: ESTA FERRAMENTE DEVE SER UTILIZADA DA MANEIRA
CORRETA, CASO DE ALGUM ERRO VERIFIQUE OS ARGUMENTOS QUE VOCE PASSOU.

ART 1.2: ESTA FERRAMENTA PODE TER NOVAS
ATUALIAÇÕES, COM MAIS FUNCIONALIDADES.
 QUER VERIFICAR, VA AO NOSSO GIT HUB E BAIXE A ULTIMA VERÇÃO

HELP:
-u --- informa a url [--url]
-w --- inform a wordlist [--wordlist]



NANDO FROM CAPUCCION TEAM ™ 2021 - 2022 ®
"""


ajuda = """
pt-br

-u --- informa a url [--url]
-w --- inform a wordlist [--wordlist]

see the final results in the tool directory and results.txt
"""

args = sys.argv
Machine = GREEN+STARTED + "-"*60 + STARTED_PT_BR + "\n"+"-"*60 + ajuda + "-"*60
for l in Machine:
    sys.stdout.write(l)
    sys.stdout.flush()
    # time.sleep(.00000000000000000000000000000000000000000000000000000000001)

locales = Get(args)[0]
Wordlist = LoadWordlists(locales)
siteUrl = Get(args)[1]


def core(siteUrl,Wordlist):
    try:
        REPLACEDURL = ""
        VERFY = str(siteUrl).split("/")
        VERFY2 = str(siteUrl).replace(
            "https://", "").replace("http://", "").split(".")
        __POSITION = 0
        try:
            __POSITION = int(str(siteUrl).split("/").index("DIR"))
            REPLACEDURL = str(siteUrl).replace(str(VERFY[__POSITION]), "")
        except:
            __POSITION = int(str(siteUrl).replace(
                "https://", "").replace("http://", "").split(".").index("DIR"))
            REPLACEDURL = str(siteUrl).replace(str(VERFY2[__POSITION]), "")

        print("\n"+GREEN+"[*] Starting [*]")

        if VERFY[__POSITION] == "DIR" or VERFY2[__POSITION] == "DIR":
            tempoDeRequest = ""
            lists = 1
            r = ""
            __typeError = ""
            inicio = time.time()
            for DIRS in Wordlist:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
                                        'AppleWebKit/537.36 (KHTML, like Gecko) '\
                                        'Chrome/75.0.3770.80 Safari/537.36'}

                try:
                    initTime= time.time()
                    r = requests.get(REPLACEDURL+DIRS,headers = headers)
                    endTime= time.time()
                    tempoDeRequest = str(endTime - initTime)
                    formatedT = tempoDeRequest.split(".")[0]+"."+str(tempoDeRequest.split(".")[1])[:3] + " s"
                except:
                    str(logging.exception("Erro inesperado! \n")) 
                    try:
                        REDIRECT_TYPE = REPLACEDURL.split(":")[0]
                        REPLACEDURL = REPLACEDURL.replace(
                            "https://", "").replace("http://", "")
                        initTime= time.time()    
                        r = requests.get(REDIRECT_TYPE+"://"+DIRS+REPLACEDURL,headers = headers)
                        endTime= time.time()
                        tempoDeRequest = str(endTime - initTime)
                        __typeError = "wordlist"
                        
                    except:
                        if __typeError == "wordlist":
                            print("please, select a sub domains wordlist")
                            exit()
                        else:
                            print(RESET)
                            print("-"*60+"\n"+"bye")
                            exit()
   

                largura = int(len(DIRS))

                porcentagem = int(lists)*100/len(Wordlist)

                textFormated = "| "+"[*] STATUS CODE:" + " "*3 + str(r.status_code) + "|" + " [*] url: "+str(r.url) + " "*int(30-largura) + "| " + str(porcentagem).split(".")[0]+"."+str(porcentagem).split(".")[1][:2] + "% | " + "[*] tryed " + str(
                    lists) + "/" + str(len(Wordlist))+ " "*int(8-len(str(lists))) + "| [*] " + str(int(len(Wordlist)) - lists) + " missing" + "      "+ "| [*] Request Time "+ formatedT + " |"

                TRUEORFALSE = False

                if r.status_code == 404:
                    print("\r"+RED+textFormated)
                elif r.status_code == 200:
                    print(GREEN+textFormated)
                    TRUEORFALSE = True
                else:
                    print(CYAN+textFormated)
                    TRUEORFALSE = True
                if TRUEORFALSE:
                    with open("results.txt", "r") as r:
                        Writess = r.read() + "\n" + textFormated
                        with open("results.txt", "w") as w:
                            w.write(Writess)
                            TRUEORFALSE = False

                lists = lists + 1
                #time.sleep(.01)
            fim = time.time()
            tempoPercorrido = inicio - fim
            print("time elapsed "+tempoPercorrido)
            with open("results.txt", "r") as r:
                print(r.read())
            print(RESET)
    except:
        print(RESET)
        exit()


#core(siteUrl,Wordlist)
if __name__ == "__main__":
    threads = []
#    t1 = threading.Thread(target=core, args= (siteUrl,Wordlist))
#    t1.start()
#    threads.append(t1)
    process = Process(target=core, args=(siteUrl,Wordlist))
    process.start()

    