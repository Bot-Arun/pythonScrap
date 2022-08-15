import undetected_chromedriver as uc
from selenium import webdriver
import time
options,drivers = [],[] 
urls = [
    'https://www.autodoc.co.uk/spares-search?keyword=turbo+charger',
    'https://www.auto-doc.it/pezzi-di-ricambio/compressore-10972',
    'https://www.oscaro.com/'
    ]
user_agent ="user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
keys = [0]*3

for x in urls :
    print(x)
    options.append( webdriver.ChromeOptions())
    # options[-1].add_argument(user_agent)
    # options[-1].add_argument("--proxy-server={}".format("127.0.0.1:8080"))
    drivers.append(uc.Chrome(options=options[-1]))

for i in range(len(drivers)):
    drivers[i].get(urls[i])

time.sleep(1300)

for i in range(len(drivers)):
    cookies =drivers[i].get_cookies()

    for x in cookies :
        if x["name"]=="cf_clearance" :
            cookies = x["value"]
    keys[i] = cookies
    print(cookies)
