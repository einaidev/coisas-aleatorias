validARGS = ["-u","--url","-w","--wordlist"]


def Get(args):
    urlGeted = ""
    urlPATH = ""
    URL = args

    if "-u" in URL or "--url" in URL:
        try:
            urlGeted = URL[URL.index("-u")+1]
        except:
            urlGeted = URL[URL.index("--url")+1]    

    if "-w" in URL or "--wordlist" in URL:
        try:
            urlPATH = URL[URL.index("-w")+1]
        except:
            urlPATH = URL[URL.index("--wordlist")+1]    
        
    return  urlPATH,   urlGeted       