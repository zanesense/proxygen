import os,sys

try:
    import requests
    from huepy import *
except:
    print("required modules missing, installing..")
    os.system("pip install huepy requests")

print(green(r'''                                                      
_____________  _______  ______.__. ____   ____   ____  
\____ \_  __ \/  _ \  \/  <   |  |/ ___\_/ __ \ /    \ 
|  |_> >  | \(  <_> >    < \___  / /_/  >  ___/|   |  \
|   __/|__|   \____/__/\_ \/ ____\___  / \___  >___|  /
|__|                     \/\/   /_____/      \/     \/ 

'''))

types = input(info("Enter proxy type (socks/http)\n>> "))
if types == "socks":
    proxy_type = "socks4,socks5"
elif types == "http":
    proxy_type = "http"
elif len(types) == 0:
    print(bad("No input was provided, exiting.."))
    sys.exit()
else:
    print(bad("Bad proxy type, exiting.."))
    sys.exit()

proxy_country = input(info("Enter proxy countries (e.g ru,us,cn,nl)\n>> "))
if len(proxy_country) == 0:
    print(bad("No input was provided, exiting.."))
    sys.exit()

proxy_limit = input(info("Upto how many proxies to generate, if possible? (min. 10)\n>> "))
if len(proxy_limit) == 0:
    print(bad("No input was provied, exiting.."))
    sys.exit()

def gen():
    r=requests.get("https://www.proxyscan.io/api/proxy?last_check=9800&country="+proxy_country+"&uptime=80&ping=200&limit="+proxy_limit+"&type="+proxy_type)
    with open("output.json", "w") as f:
        f.write(r.text)
    print(good("Wrote the output to output.json in the current dir."))

try:
    gen()
except:
    print(bad("Proxy generation failed, check your internet connection."))
    sys.exit()


