import psutil
import os

arr = []
arrayJava = ['javaw.exe','java.exe','javaw','java']
arrayLow = ['brave.exe','chrome.exe','edge.exe']

json_ = {}

def SetUp(arr = arr, arrayJava=arrayJava, json_ = json_):
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            arr.append(processName)
            json_[proc.name()] = proc.username()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass       

    for i in arrayJava:
        if i in arr:
            os.system(f'wmic process where name="{i}" CALL setpriority 128 > NUL')
            for i2 in arr:
                    try:
                        if json_[i2] == 'NT AUTHORITY\\SYSTEM' or i2 in arrayJava or i2 == 'Discord.exe':
                            pass
                        else:
                            os.system(f'wmic process where name="{i2}" CALL setpriority 16384 > NUL')
                    except:
                        pass 
            return 'Prioridade configurada com exito' 
        else:
            return 'Erro ao encontrar o proscesso Java'