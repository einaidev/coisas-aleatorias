import base64
import json
import time
from ttkthemes import ThemedTk
from tkinter import Frame, ttk
import ctypes
import win32api
import tkinter as tk
import os as os
import shutil as sh
from ramOpt import main
from setPriority import SetUp
from regeditHandler import ApplyRegs
import sys 



if getattr(sys, 'frozen', False): # Running as compiled
    running_dir = sys._MEIPASS + "/files/" # Same path name than pyinstaller option
else:
    running_dir = "./" # Path name when run with Python interpreter
iconFileName = running_dir + "agiota.ico"
iconFileName2 = running_dir + "agiota.png"

myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

dirU = os.getlogin()

class Config:
    Theme = "equilux"
    BG_Colour = '#23282b'
    BG_Frame = '#1d2124'
    config = {}
    actions = {}

class NewWindow():
    string = ""
    def __init__(self):   
        string = self.string
        lista = ['']
        lista_2 = ['']
        lista2 = []
        lista3 = []
        for i in range(0,string.__len__(),105):
            lista.append(string[:i])
            adicionar = string.replace(lista[-1],"")
            lista2.append(adicionar[:105]+"\n")
        string = ""

        for i in lista2: 
            string = string + i 
        if string.__len__()> 1600:
            for i in range(0,string.__len__(),1600):
                lista_2.append(string[:i])
                adicionar = string.replace(lista_2[-1],"")
                lista3.append(adicionar[:1600])   
            string = lista3[0]       
        conf = Config()

        screen2 = ThemedTk(theme=conf.Theme)
        screen2.maxsize(720, 720)
        screen2.minsize(650, 650)
        screen2.title("Optimizador")

        s = ttk.Style(screen2)
        s.configure("Frame1.TFrame", background=conf.BG_Frame)
        s.configure("Frame2.TFrame", background=conf.BG_Colour)
        s.configure("Label.TLabel", background=conf.BG_Frame)
        s.configure("RED.TButton", background="red", anchor="s")
        s.configure("CHANGER1.TButton",anchor="l", background="red")
        s.configure("CHANGER.TButton",anchor="o", background="red")

        screen2.configure(background=conf.BG_Colour)
        frame = ttk.Frame(screen2,style="Frame1.TFrame",height=640,width=640)
        frame2 = ttk.Frame(screen2,style="Frame2.TFrame")

        ttk.Label(screen2, text="Caso não esteja aparencendo os logos, tente fechar esta janela e clicar novamente no botão LOGS",style="Frame1.TFrame").pack()

        frame.pack(pady=20)
        frame2.pack()

        texto =  ttk.Label(frame,text=string,width=55,relief="solid",borderwidth=1,anchor="nw",style='Label.TLabel')
        texto.place(width=639,height=639)


        botão1 = ttk.Button(frame2,text="Pagina Aterior",style="RED.TButton", command= lambda: PageChangerDown())
        botão2 = ttk.Button(frame2,text="Pagina Posterior",style="RED.TButton",command= lambda: PageChangerUp())

        def PageChangerUp(lista3=lista3,string=string, texto=texto):
            try:
                string = texto["text"]
                rangerList = lista3.__len__()
                positionRel = lista3.index(string)
                if string == "": return
                if rangerList <= 1: return
                if positionRel == rangerList-1 : return

                texto["text"] = lista3[positionRel+1]
            except:
                pass    

        def PageChangerDown(lista3=lista3,string=string, texto=texto):
            try:
                string = texto["text"]
                rangerList = lista3.__len__()
                positionRel = lista3.index(string)
                if string == "": return
                if rangerList <= 1: return
                if positionRel == 0 : return

                texto["text"] = lista3[positionRel-1]    
            except:
                pass    

        botão1.pack(side='left')
        botão2.pack(padx=10)

if os.path.isfile("config.json"):
    try:
        with open("config.json", "r") as r:
            loader = []
            loaded = json.load(r)
            for i in loaded:
                loader.append(i)
            for i in loader:
                Config.config[i] = loaded[i]   
    except:
        pass

screen = ThemedTk(theme=Config.Theme)
screen.configure(background=Config.BG_Colour)
screen.maxsize(700, 500)
screen.minsize(700, 500)
screen.title("Optimizador")
img = None
if os.path.isfile(iconFileName2):
    img = tk.PhotoImage(file=iconFileName2)
else:   
    img = tk.PhotoImage(file='src/agiota.png')
s = ttk.Style()
s.configure("RED.TButton",background="red")
s.configure("GREEN.TButton",background="green")
s.configure("Frame1.TFrame", background=Config.BG_Colour)

bottomFrame = ttk.Frame(screen,style="Frame1.TFrame")

frameMoreOpt = ttk.Frame(screen, width=450,height=420,style="Frame1.TFrame",relief="solid",borderwidth=1)
frameMoreOpt.pack()
frameMoreOpt.place(x=220,y=20)

frame = ttk.Frame(bottomFrame,width=200,height=500,style="Frame1.TFrame")
frame2 = ttk.Frame(screen,width=300,height=500,style="Frame1.TFrame")

frame.pack(side="right")
frame2.pack(side="left")

bottomFrame.pack(side="bottom")
img = img.zoom(1,1)
canvas = tk.Canvas(screen,width=160,height=160,bg='black',relief="solid")
canvas.create_image(0,0, anchor=tk.NW,image=img)
canvas.pack(pady=10)
canvas.place(x=21,y=21)

def Aplly(dirU=dirU):
    type_ = ""
    try:
        if Config.config["OptmizePing"][0] == "true":
            ApplyRegs()  
            NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Aplicando regedit \n"
    except:
        pass
    try:
        if Config.config["CacheDel"][0] == "true":
            DelTemp(dirU)    
    except:
        pass            
    try:    
        if Config.config['OptmizeRam'][0] == "true":
            NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Otimizando Memoria Ram"
            main()   
    except:
        pass  
    try:
        if Config.config["SetPriority"][0] == "true":
            NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Configurando Prioridade \n"
            Res = SetUp
            NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + Res() + "\n"
    except:
        pass        

    if Config.config.__len__() == 0:
        win32api.MessageBox(0, 'Não a nada celecionado', 'Erro', 0x00001000)

    with open("config.json", 'w') as w:
        w.write(Config.config.__str__().replace("'", '"'))

def DelTemp(dirU):  
    for i in os.listdir("C:\\Users\\"+dirU+"\\AppData\\Local\\Temp"):
        try:
            sh.rmtree("C:\\Users\\"+dirU+"\\AppData\\Local\\Temp\\"+i)
            NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Removendo pasta temporaria : " + i + "\n"
        except:
            try:
                sh.rmtree("C:\\Users\\"+dirU+"\\AppData\\Local\\Temp\\"+i)
                NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Removendo arquivo temporario : " + i + "\n"
            except:
                NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Falha ao remover alguns arquivos temporarios "+ "\n"

    for i in os.listdir("C:\Windows\Temp"):
        try:
            sh.rmtree("C:\\Windows\\Temp\\"+i)
            NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Removendo arquivo temporario : " + i + "\n"
        except:
            try:
                sh.rmtree("C:\\Windows\\Temp\\"+i)
                NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Removendo pasta temporaria : " + i + "\n"  
            except:
                NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Falha ao remover alguns arquivos temporarios " + "\n"
    for i in os.listdir("C:\\Windows\\SoftwareDistribution"):
        try:
            sh.rmtree("C:\\Windows\\SoftwareDistribution\\"+i)
            NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Removendo arquivo temporario : " + i + "\n"
        except:
            try:
                sh.rmtree("C:\\Windows\\SoftwareDistribution\\"+i)
                NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Removendo pasta temporaria : " + i + "\n"
            except:
                NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Falha ao remover alguns arquivos temporarios : " + i + "\n"
    win32api.MessageBox(0, 'Caso não seja posivel apagar o cache, tente rodar como administrado', 'Erro', 0x00001000)                
    os.system("Ipconfig /flushdns")
    NewWindow.string = NewWindow.string + "["+str(time.localtime(time.time()).tm_hour)+":"+str(time.localtime(time.time()).tm_min)+"] " + "Limpando cache do DNS" + "\n"

def Update_Sys(a,b):
    load = a.__str__().replace("{", "").replace(
        "'", "").replace("}", "").split(":")[0]
    try:
        if Config.config[load][0]=="true":
            Config.config[load][0]="false"
            exec(b+"['style'] = 'RED.TButton'") 
                        
        elif Config.config[load][0]=="false":
            Config.config[load][0]="true"
            exec(b+"['style'] = 'GREEN.TButton'")
    except:
        exec(b+"['style'] = 'GREEN.TButton'")     
        Config.config[load]=["true",b] 

optimizeRam = ttk.Button(frameMoreOpt, text="Optimizar Memoria Ram",style="RED.TButton", command=lambda: [Update_Sys("OptmizeRam",b="optimizeRam")])
SetPriority = ttk.Button(frameMoreOpt, text="Aumentar A Prioridade Do Processo Java",style="RED.TButton", command=lambda: [Update_Sys("SetPriority",b="SetPriority")])
button = ttk.Button(frame, text="Apply",command=lambda: [Aplly()] ,style='RED.TButton')
button2 = ttk.Button(frame2,width=27, text="Optimizar Ping & Fps",style='RED.TButton', command=lambda: [Update_Sys("OptmizePing",b="button2")])
button3 = ttk.Button(frame2, text="Apagar todos os tipos de cache",style='RED.TButton',command=lambda: [Update_Sys("CacheDel",b="button3")])
texto1 = ttk.Label(frame2,text="V 0.1.0",background=Config.BG_Colour,foreground="gray")
button4 = ttk.Button(frame,text="LOGS",style='RED.TButton',command=lambda: NewWindow())

optimizeRam.grid(row=0,column=0, pady=10,padx=10)
texto1.grid(row=0,column=0)
button4.grid(row=10,column=5,sticky=tk.E,padx=10,pady=10)
button.grid(row=10, column=4,sticky=tk.E,padx=0,pady=10)
button2.grid(row=1, column=0,padx=10,pady=10)
button3.grid(row=2, column=0,padx=10,pady=10)
SetPriority.grid(row=0,column=1, pady=10,padx=10)



if os.path.isfile(iconFileName):
    screen.iconbitmap(iconFileName)
else:    
    screen.iconbitmap(default="src/agiota.ico")

    

def loadColors():
    with open('config.json','r') as r:
        loadss = json.loads(r.read())
        for i in loadss :
            if loadss[i][0] == 'true':
                exec(loadss[i][1]+"['style']='GREEN.TButton'")       
try:                        
    loadColors()   
except:
    pass    

def minecraftLocation():
    with open("config.json", "w") as w:
        pass

screen.mainloop()
