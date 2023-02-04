import random
import time
import selenium
import requests
import sys
import pyautogui
import threading
import os

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

global send_total
global send

snap = "<loreehilt"

os.system("title BAZOOCAM E-WHORING BOT")

send = 0
send_total = send

def bazoocambot():
    global send
    global send_total
    global snap

    driver = webdriver.Chrome(ChromeDriverManager().install())

    while True:

        if send == 50:

            driver.quit()
            driver = webdriver.Chrome(ChromeDriverManager().install())
            send = 0

        else:
            try:

                driver.get("https://bazoocam.org/fr/")
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="chkgeo"]').click()
                time.sleep(1)
                element = driver.find_element_by_css_selector('#nextButton_first')
                element.click()
                try:


                    text = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/input")
                    time.sleep(1)
                    text.send_keys("Hey, I send nudes and we can video call to do some naughty stuff together! Here is my snap: "+snap)
                    text.send_keys(Keys.RETURN)
                    time.sleep(1)
                except:
                    driver.quit()
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                print(Fore.GREEN+"Message sent ! "+Style.RESET_ALL)
                send = send+1
                send_total = send_total + 1
                os.system("title Message n°"+str(send_total))
                skip = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[3]/div[1]/button[1]")
                skip.driver.click()
            except:
                pass

bazoocambot()
