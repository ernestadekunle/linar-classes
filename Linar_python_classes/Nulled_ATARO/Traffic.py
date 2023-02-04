import random
import time
import selenium
import requests
import sys
import pyautogui
import threading
import os
import re
import json

from colorama import Fore, init, Style
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common import exceptions
from requests import RequestException
from tkinter import filedialog
from selenium.webdriver.common.proxy import Proxy, ProxyType


init()

global proxy
global age
global snap
global code
global snap_input
global age_input
global thread_input
global proxy_file
global proxy
global jusdeouaisouais
global x
global using_proxy
global response
global send_total
global send
response = "0"


os.system("title Heil hitler ᛋᛋ")

send = 0
send_total = send
x = 0

class launch_thread(threading.Thread):

    def _init_(self):

        threading.Thread._init_(self)

    def run(self):

        print(threading.current_thread())

        if using_proxy == "Y":

            if response == "1":

                connection_coco(snap_input,age_input,code_input,proxy[x])

            elif response == "2":

                omegle_bot(snap_input,proxy[x])

            elif response == "3":

                randomchat(snap_input)

        else:

            if response == "1":

                connection_coco(snap_input,age_input,code_input,"none")

            elif response == "2":

                omegle_bot(snap_input)

            elif response == "3":

                randomchat(snap_input)




def print_banner():
    banner = '''                             --------------------
                   ??????             |Ewho traffic bot  |
                    ????              |By divinou and 7up|
				      |v2 by ataro       |
                  _ ) &._/ /          --------------------
                 /  )__| .'
                /./| _)_)
               ( | \.--|
                \|  ) !|
                /| /.__|
               (_// _\_/______
                 (            )
                  '..____.-'/ |
                   \  |    (  |
                    \ /     \ |
                    / |      )|
                   (  |     / |
                    \ |      \|
                     )|
                    / |
                     \|'''


    print(Fore.LIGHTRED_EX + banner)


def test_conn():

    print(Fore.LIGHTBLUE_EX + "Before starting, let me check your internet connection....")

    if requests.get("http://httpbin.org/get").status_code == 200:

        print(Fore.LIGHTGREEN_EX + "Ok, you're connected :)")
        print(Style.RESET_ALL + "--------------------------")
        sys.stdout.flush()

    else:

        print(Fore.LIGHTRED_EX + "Your connection is not working, please check it and come back later :)")
        print(Style.RESET_ALL + "--------------------------")
        time.sleep(3)
        exit(0)



def ask_info():

    global snap_input
    global age_input
    global code_input
    global thread_input
    global proxy_file
    global proxy
    global jusdeouaisouais
    global using_proxy

    snap_input = input("What's your snapchat username : ")
    age_input = int(input("E-Whore's age? : "))
    code_input = int(input("Postal # (for French users only. else type 00000) : "))
    thread_input = int(input("How many threads? (1 is safer)  : "))
    using_proxy = input("Usage of proxy ? (Y/N) :")
    time.sleep(1)
    os.system('cls')
    print("Ewho Traffic bot")

    print(Fore.LIGHTRED_EX + "V0.4")
    print("Your informations" + Fore.LIGHTBLUE_EX + " ~")
    print(Style.RESET_ALL)
    print("Snap : " + snap_input)
    print("Age : " + str(age_input))
    print("Postal code : " + str(code_input))
    print("proxy usage : " + using_proxy)
    print("# of thread : " + str(thread_input))


    if using_proxy == "Y":
        jusdeouaisouais = os.getcwd()
        proxy_file = filedialog.askopenfilename(title="Open Proxy File",initialdir=jusdeouaisouais)
        proxy =  open(proxy_file).read().splitlines()

    elif using_proxy == "N":
        proxy = ["none"]

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

def connection_coco(snap,age,code,proxy):

    if proxy == "none":

        driver = webdriver.Chrome(ChromeDriverManager().install())

    else:

        PROXY = proxy
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' ,(PROXY))
        driver = webdriver.Chrome(options=chrome_options)


    driver.get("https://www.coco.fr/")
    nom = str(snap+str(random.randint(10000,100000)))
    driver.find_element_by_css_selector("#nicko").send_keys(nom)
    driver.find_element_by_css_selector("#invitea > form > input[type=radio]:nth-child(2)").click()
    driver.find_element_by_css_selector("#ageu").send_keys(age)
    driver.find_element_by_css_selector("#zipo").send_keys(code)
    time.sleep(1)
    driver.find_element_by_css_selector("#invitea > div.bouton").click()
    driver.get("https://www.coco.fr/chat/index.html#"+nom+"_2_18_11938_0_889950887_0_")
    time.sleep(1)
    driver.get("https://www.coco.fr/chat/index.html#"+nom+"_2_18_11938_0_889950887_0_")




    xx = 2
    mess = 0
    bougre = True

    while bougre:


        try:
            textechat = "/html/body/div[14]/div[7]/div[2]/div["+str(xx)+"]"
            driver.find_element_by_id("opt0").click()
            time.sleep(3)
            driver.find_element_by_xpath(textechat).click()
            time.sleep(3)
            continueu = True

        except:
            continueu = False
            time.sleep(1)

        if continueu == True:

            driver.find_element_by_id("cocoa").send_keys("Hey ! Add me on snap darling! (hot pics and nudes!)  : "+snap+"\n")
            time.sleep(3)
            driver.find_element_by_id("cocoa").send_keys(Keys.RETURN)
            time.sleep(1)
            try:
                captcha = driver.find_element_by_xpath("/html/body/div[14]/div[12]/div[1]")
            except:
                captcha = 0
                pass

            if captcha != 0:

                input("Please complete the captcha")
                print(Fore.GREEN+"Message sent ! "+Style.RESET_ALL)
                xx = xx+1
                mess = mess+1
                captcha = None

            else:
                print(Fore.GREEN+"Message sent ! "+Style.RESET_ALL)
                mess = mess + 1
                xx = xx+1
                continue

            if mess == 5:

                driver.quit()
                driver.get("https://www.coco.fr/")
                nom = str(snap+str(random.randint(10000,100000)))
                driver.find_element_by_css_selector("#nicko").send_keys(nom)
                driver.find_element_by_css_selector("#invitea > form > input[type=radio]:nth-child(2)").click()
                driver.find_element_by_css_selector("#ageu").send_keys(age)
                driver.find_element_by_css_selector("#zipo").send_keys(code)
                time.sleep(1)
                driver.find_element_by_css_selector("#invitea > div.bouton").click()
                driver.get("https://www.coco.fr/chat/index.html#"+nom+"_2_18_11938_0_889950887_0_")
                time.sleep(1)
                xx=2












def omegle_bot(snap,*proxy2):

    global send
    global send_total
    print(proxy2)

     #if proxy is not None:

        #chrome_options = webdriver.ChromeOptions()
        #proxy parameter to options
        #chrome_options.add_argument('--proxy-server=%s' + (proxy2))
        #options to Chrome()
        #driver = webdriver.Chrome(chrome_options= chrome_options)
        #driver.implicitly_wait(0.6)

    #else:

    driver = webdriver.Chrome(ChromeDriverManager().install())
    truchiant = True
    while truchiant:
        try:
            driver.get("https://www.omegle.com/")
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td[2]/img').click()
            input("Accepter le reglement !")
            element = driver.find_element_by_css_selector('body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.chatmsgcell > div > textarea')
            element.click()
            time.sleep(1)
            element.send_keys("Hey ! Add me on snap darling! (hot pics and nudes!)  : "+snap)
            time.sleep(1)
            driver.find_element_by_css_selector("body > div.chatbox3 > div > div > div.logwrapper > div.logbox > div > div:nth-child(6) > div > div > img").click()
            truchiant=False
        except:
            try:
                driver.find_element_by_css_selector("body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.disconnectbtncell > div > button").click()
                time.sleep(1)
                driver.find_element_by_css_selector("body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.disconnectbtncell > div > button").click()
                truchiant=False

            except:
                pass
        while True:

            try:


                try:
                    issou = driver.find_element_by_css_selector("#recaptcha-anchor > div.recaptcha-checkbox-border")
                    issou.click()
                    issou.click()
                    time.sleep(1)
                except:
                    pass
                try:

                    element = driver.find_element_by_css_selector('body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.chatmsgcell > div > textarea')
                    element.click()
                    time.sleep(1)
                    element.send_keys("Hey ! Add me on snap darling! (hot pics and nudes!) : "+snap)
                    time.sleep(1)
                except:
                    pass



                driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[3]/div/button').click()
                time.sleep(1)
                print(Fore.GREEN+"Message envoyé ! "+Style.RESET_ALL)
                send = send+1
                send_total = send_total + 1
                os.system("title Message send : "+str(send_total))
                try:
                    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button').click()
                    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button').click()
                except:
                    pass
                driver.find_element_by_css_selector("body > div.chatbox3 > div > div > div.logwrapper > div.logbox > div > div:nth-child(6) > div > div > img").click()
            except:
                pass

def randomchat(snap):

    global send
    global send_total

    driver = webdriver.Chrome(ChromeDriverManager().install())
    while True:
        try:
            driver.get("https://fr.randomchat.com/#")
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[4]/div/div[4]/div/div/div/div[2]/div[1]/div/ul/li[2]/a").click()
            time.sleep(2)
            arabe = driver.find_element_by_idd("start-preview-bt").click()
            try:
                arabe = driver.find_element_by_css_selector("#message_text")
                arabe.click()
                time.sleep(1)
                arabe.send_keys("Hey ! Add me on snap darling! (hot pics and nudes!) : "+snap)
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div/div/div[1]/div/div/div[3]/div/div/button").click()
            except:
                pass
        except:
            pass



def menu(): 

    global response

    print_banner()
    test_conn()
    ask_info()


    print("["+Fore.LIGHTBLUE_EX + "*" + Fore.RESET + "] 1 >> Coco")
    print("["+Fore.LIGHTBLUE_EX + "*" + Fore.RESET + "] 2 >> Omegle")
    print("["+Fore.LIGHTBLUE_EX + "*" + Fore.RESET + "] 3 >> Randomchat")

    response = input("["+Fore.LIGHTRED_EX + "?" + Fore.RESET + "] >> ")
    for i in range(thread_input):

        launch_thread().start()

menu()
