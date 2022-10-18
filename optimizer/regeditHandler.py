import os
import sys

if getattr(sys, 'frozen', False): # Running as compiled
    running_dir = sys._MEIPASS + "/regedits/" # Same path name than pyinstaller option
else:
    running_dir = "regedits" # Path name when run with Python interpreter

 
def Replice(dir:str):
    dir = dir.replace('\\','/')
    list = dir.split('/')
    list.remove(list[-1])
    strg2 = ''
    for i in dir.split('/'):
        if ' ' in i:
            position = list.index(i)
            strg = i.replace(i[0],'"'+i[0]).replace(i[-1],i[-1]+'"')
            list.insert(position,strg)
            list.remove(i)
    for i in list:
        strg2 = strg2+i+"/"   
    return strg2  

a = __file__.replace("\\",'/').split("/")                     
a.remove(a[-1])
strg2 = ''
for i in a:
    strg2 = strg2+i+"/"

def ApplyRegs(strg2 = strg2):
    sus = os.listdir(running_dir)
    if getattr(sys, 'frozen', False):
        with open('logs.txt','w') as w :
            for i in sus:
                w.write(i+'\n')
        for i in sus:
            s = i.split('.')[1]
            if s == 'bat':
                os.system(f'{running_dir}"{i}"')
            elif s == 'reg':
                os.system(f"reg import {running_dir}"+i)
    else:
        with open('logs.txt','w') as w :
            for i in sus:
                w.write(i+'\n')
        for i in sus:
            s = i.split('.')[1]
            if s == 'bat':
                os.system(f'{Replice(dir=strg2)}/regedits/"{i}"')
            elif s == 'reg':
                os.system(f"reg import {Replice(dir=strg2)}/regedits/"+i)          
