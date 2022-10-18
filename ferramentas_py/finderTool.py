
import sys, requests, os, time,_thread, socket, platform,subprocess
from datetime import datetime

class collors:
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[;7m"

logo = """
{0}______      _____                               _____           _ 
{0}| ___ \    /  ___|                             |_   _|         | |
{0}| |_/ /   _\ `--.  ___ __ _ _ __  _ __   ___ _ __| | ___   ___ | |
{0}|  __/ | | |`--. \/ __/ _` | '_ \| '_ \ / _ \ '__| |/ _ \ / _ \| |
{0}| |  | |_| /\__/ / (_| (_| | | | | | | |  __/ |  | | (_) | (_) | |
{0}\_|   \__, \____/ \___\__,_|_| |_|_| |_|\___|_|  \_/\___/ \___/|_|
{0}       __/ |                                                      
{0}      |___/ 

{1}                    Nando Msc © 2022 - current.

{2}By using this software you accept and understand the following terms
{2}1 - I am not responsible for even an immature attitude with this tool
{3}---------------------------------------------------------------------                                                    
""".format(collors.BLUE, collors.GREEN, collors.RED, collors.RESET)


class main:
    def __init__(self, kw):
        print(logo)
        self.session = requests.session()
        self.navagtor = requests
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36","Content-Type":"text"}  
        for nm,vl in kw.items():
            exec("self.{0} = {1!r}".format(nm,vl))

            if nm == "wordlist":
                if not os.path.isfile(vl):
                    return print("Error! {0!r} is not a file".format(vl))
                else:
                    with open(vl, "r") as r:
                        exec("self.{0} = {1!r}".format(nm,r.read().split("\n")))


    def dir(self):
        print("Dir listing method\n")
        requeries = ["wordlist", "url", "useragent"]
        self.setRequiries(requeries)
        self.initFile("dir listing")

        for i in self.wordlist:
            try: 
                self.navagtor.get(self.url.replace("[dir]", i))
            except Exception as e:
                return print(self.url.replace("[dir]", i) + " is not a valid url")
            
            def run(i=i):
                t = time.time()
                r = self.navagtor.get(self.url.replace("[dir]", i), headers=self.setHeaders)
                t2 = time.time()
                
                resultStr = "[*]Url: {0}{1}[*]Status code: {2!r}{3}[*]Request time: {4} [*]Dir: {5}{6}[*]".format(r.url, " "*(50 - r.url.__len__()), r.status_code, " "*(10-r.status_code.__str__().__len__()), "{0}.{1}".format((t2-t).__str__().split(".")[0], (t2-t).__str__().split(".")[1][:3]), i, " "*(30-i.__len__()) )
                print(resultStr)

                self.setResults(resultStr)

            self._ThreadingTime
            _thread.start_new_thread(run, ())

    def PortScanner(self):
        print("Port scanner method\n")
        requeries = ["url", "all", "ranger"]
        self.setRequiries(requeries)
        self.initFile("port scanner")

        ranger = 0
        start = 0

        if "all" in self.ranger.split("-"): 
            ranger = 65535
            start = 0
        elif self.ranger.split("-").__len__() == 2:
            if self.ranger.split("-")[0].isnumeric() and self.ranger.split("-")[1].isnumeric():
                ranger = int(self.ranger.split("-")[1])
                start = int(self.ranger.split("-")[0])
            else: 
                ranger = 65535
                start = 0
        else:
            ranger = 65535
            start = 0

        for i in range(start, ranger):
            def _start_thread(i=i):
                if i == 0: return
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                res = s.connect_ex((self.url, i))

                result = "[*]Url: {0}{1}[*]Port: {2}{3}[*]Port Status: {4}{5}[*]".format(self.url, " "*(20-self.url.__len__()), i, " "*(7-str(i).__len__()), "Open" if res == 0 else "Close", " "*(10 - "Open".__len__() if res == 0 else "Close".__len__()))
                s.close()

                if self.all in ["true", "True"]:
                    self.setResults(result)
                    print(result)
                else:
                    if res == 0:
                        self.setResults(result)
                        print(result)

            self._ThreadingTime
            _thread.start_new_thread(_start_thread, ())

    def command_bruteforce(self):
        print("Command brute force method\n")
        requeries = ["wordlist","command"]
        self.setRequiries(requeries)
        self.initFile("command brute force")

        for i in self.wordlist:
            def _start_thread(i=i):
                result = subprocess.run(self.command.replace("[brute]", i),  capture_output=True, text=True).stdout.strip("\n")
                r2 = result
                r = "[*]Command: {0}{1}[*]Result: {2}{3}[*]".format(self.command.replace("[brute]", i), " "*(50-self.command.replace("[brute]", i).__len__()), r2, " "*(50-r2.__len__()))

                print(r)
                
            self._ThreadingTime
            _thread.start_new_thread(_start_thread, ())            
    def setRequiries(self,req):
        for i in req:
            if not i in self.__dict__:
                print("Not {0!r} parameter has been passed".format(i))
                exit()

    @property         
    def setHeaders(self):
        if self.useragent in ["true", "True"]:
            return self.headers
        else:
            return {}
    
    def initFile(self, origin):
        if os.path.isfile("./RESULTS.txt"):
            with open("./RESULTS.txt", "r") as r:
                r_old = r.read()
                with open("./RESULTS.txt", "w") as w:
                    w.write(r_old+ "\n[{0}] - {1}\n".format(datetime.now().strftime("%d/%m/%Y- %H:%M:%S"), origin))
        else:
            with open("./RESULTS.txt", "w") as w:
                w.write(r_old+ "\n[{0}] - {1}\n".format(datetime.now().strftime("%d/%m/%Y- %H:%M:%S"), origin))         

    def setResults(self,res):
        with open("./RESULTS.txt", "r") as r:
            r_old = r.read()
            with open("./RESULTS.txt", "w") as w:
                w.write(r_old + "\n{0}".format(res))

    @property
    def _ThreadingTime(self):
        if "thread" in self.__dict__ and self.thread.isnumeric:
            time.sleep(float(self.thread))
        else:
            time.sleep(3)        

if __name__ == "__main__":
    allArgs,handling,baseArgs = {}, {"dir": "dir", "portscanner": "PortScanner", "command_bruteforce": "command_bruteforce"}, {"url": ["--url", "-u"],"wordlist": ["--wordlist", "-w"], "thread": ["-t", "--thread"], "useragent": ["--useragent", "-ur"], "all": ["--all", "-a"], "ranger": ["-r", "--ranger"], "command": ["--command", "-c"]}

    validArgs ={
        "dir": 
            ["--url:url&Argument used to pass the url you want, and replace the location, where you want to do the listing by [dir]", "--wordlist:file&Here you pass the wordlists file you want", "-w:file&Here you pass the wordlists file you want", "-u:url&Argument used to pass the url you want", "-t:threading&Thread interveal", "--thread:threading&Thread interveal", "-ur:agent&User Agent, True or False", "--useragent:agent&User Agent, True or False"],
        "portscanner":
            ["--url:url or ip&Argument used to pass the url you want", "--u:url or ip&Argument used to pass the url you want",  "--useragent:agent&User Agent, True or False", "-ur:agent&User Agent, True or False", "--thread:threading&Thread interveal", "-t:threading&Thread interveal", "--all:log port&Show log for all ports open and close, true or false", "-a:log port&Show log for all ports open and close, true or false", "-r:ranger&Port discovery ranger, ex: 10-4000 or 'all' ","--ranger:ranger&Port discovery ranger, ex: 10-4000 or 'all' " ],
        "command_bruteforce":
            ["--command:command&comando to realize te brute force, change the local per [brute]", "-c:command&comando to realize te brute force, change the local per [brute]","--thread:threading&Thread interveal", "-t:threading&Thread interveal", "--wordlist:file&Here you pass the wordlists file you want", "-w:file&Here you pass the wordlists file you want"]
    }
    usedArgs = sys.argv[1:]

    menu = "Nando Msc© 2022 - current\nBy using this software you accept and understand the following terms\n1 - I am not responsible for even an immature attitude with this tool"
    for nm,vl in validArgs.items():
        a = []
        for i in vl:
            iDesc = "".join(i.split(":")[1:])
            a.append("{0}".format("{0}{2}{1}".format(i.split(":")[0], "Type: {0}{2} - Description: {1}".format( iDesc.split("&")[0], iDesc.split("&")[1], " "*(5-iDesc.split("&")[0].__len__()) ), " "*(20-i.split(":")[0].__len__()))))
        menu = menu + "\n\n{0}:\n   {1}".format(nm,"\n\n   ".join(a))
    menu = menu + "\n\nUsage: <file.py> <type> <*args>"


    if usedArgs.__len__() > 0:
        if usedArgs[0] in ["-h", "--help"]:
            print(menu)
            exit()
        if not usedArgs[0] in validArgs:
            print("\n{0!r} not a valid method\nView see the valid methods\n\n".format(usedArgs[0].title()))
            print(menu)
            exit()
        if usedArgs.__len__() >1:
            arg = usedArgs[0]
            kargs = usedArgs[1:]
            invalid_args = []

            for i in kargs:
                if i.startswith(("--", "-")) and not i in [x.split(":")[0] for x in validArgs[arg]]:
                    invalid_args.append(i)

            if invalid_args.__len__() > 0:
                print("Invalid arg{1}: {0!r}\nType '-h' for help".format(", ".join(invalid_args), "s" if invalid_args.__len__() > 1 else ""))
                exit()
            for i in kargs:
                try:
                    if (i.startswith(("-", "--"))) and kargs[kargs.index(i)+1].startswith(("-", "--", " ")):
                        print("Invalid usage.\nCorrect usage <file.py> <type> <{0!r}> <what u want> ".format(i))
                        exit()
                    else:
                        for nm,vl in baseArgs.items():
                            if i in vl:
                                allArgs[nm] = kargs[kargs.index(i)+1]
                except Exception as e:
                    print(e)
                    if isinstance(e, IndexError):
                        print("Invalid usage.\nCorrect usage <file.py> <type> <{0!r}> <what u want> ".format(i))
                        exit()
        else:
            print("You did not provide arguments to execute method {0!r}".format(usedArgs[0]))
            exit()
    else:
        print(menu)
        exit()
    
    try:
        exec("main({0}).{1}()".format(allArgs,handling[usedArgs[0]]))
    except KeyboardInterrupt:
        print("\n\nExiting...")
        exit()