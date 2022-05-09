import requests
import os
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from os import system

system('cls')
print (''' 

            )     )   (               )           (    (           
 (       ( /(  ( /(   )\ )  *   )  ( /(           )\ ) )\ )   (    
 )\ )    )\()) )\()) (()/(` )  /(  )\())         (()/((()/(   )\   
(()/(   ((_)\ ((_)\   /(_))( )(_))((_)\           /(_))/(_))(((_)  
 /(_))_  _((_)  ((_) (_)) (_(_())  _((_)         (_)) (_))  )\___  
(_)) __|| || | / _ \ / __||_   _| | || |         / __|| _ \((/ __| 
  | (_ || __ || (_) |\__ \  | |   | __ |         \__ \|   / | (__  
   \___||_||_| \___/ |___/  |_|   |_||_|  _____  |___/|_|_\  \___| 
                                         |_____|                   
                                                                            GHOSTH_icex : Chromedriver''')

sleep(3)
system('cls')
print (''' 

  █████▒██▀███  ▓█████ ▓█████               ██████  ██▀███   ▄████▄  
▓██   ▒▓██ ▒ ██▒▓█   ▀ ▓█   ▀             ▒██    ▒ ▓██ ▒ ██▒▒██▀ ▀█  
▒████ ░▓██ ░▄█ ▒▒███   ▒███               ░ ▓██▄   ▓██ ░▄█ ▒▒▓█    ▄ 
░▓█▒  ░▒██▀▀█▄  ▒▓█  ▄ ▒▓█  ▄               ▒   ██▒▒██▀▀█▄  ▒▓▓▄ ▄██▒
░▒█░   ░██▓ ▒██▒░▒████▒░▒████▒            ▒██████▒▒░██▓ ▒██▒▒ ▓███▀ ░
 ▒ ░   ░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒░ ░            ▒ ▒▓▒ ▒ ░░ ▒▓ ░▒▓░░ ░▒ ▒  ░
 ░       ░▒ ░ ▒░ ░ ░  ░ ░ ░  ░            ░ ░▒  ░ ░  ░▒ ░ ▒░  ░  ▒   
 ░ ░     ░░   ░    ░      ░               ░  ░  ░    ░░   ░ ░        
          ░        ░  ░   ░  ░                  ░     ░     ░ ░      
                                                            ░        

                                                                            FreeSRC : Tiktokpumpview v.1 (Chromedriver)''')

sleep(3)
system('cls')
print ('''

 $$$$$$\ $$\     $$\  $$$$$$\         $$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$\ $$$$$$$$\ 
$$  __$$\\$$\   $$  |$$  __$$\       $$  __$$\\__$$  __|$$  __$$\ $$  __$$\\__$$  __|
$$ /  \__|\$$\ $$  / $$ /  \__|      $$ /  \__|  $$ |   $$ /  $$ |$$ |  $$ |  $$ |   
\$$$$$$\   \$$$$  /  \$$$$$$\        \$$$$$$\    $$ |   $$$$$$$$ |$$$$$$$  |  $$ |   
 \____$$\   \$$  /    \____$$\        \____$$\   $$ |   $$  __$$ |$$  __$$<   $$ |   
$$\   $$ |   $$ |    $$\   $$ |      $$\   $$ |  $$ |   $$ |  $$ |$$ |  $$ |  $$ |   
\$$$$$$  |   $$ |    \$$$$$$  |      \$$$$$$  |  $$ |   $$ |  $$ |$$ |  $$ |  $$ |   
 \______/    \__|     \______/        \______/   \__|   \__|  \__|\__|  \__|  \__|   
                                                                                     
                                                                                     
                                                                                     
                                                                                                  ''')

sleep(2)

options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')

url = "http://vipto.de"

driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(url)

yy = input('Enter Capcha : Click enter')
link = input('input link : ')
count = (1)

sleep(450)
element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button')));element.click()
fill_info = driver.find_element_by_xpath('/html/body/div[4]/div[5]/div/form/div/input')
fill_info.send_keys(link, Keys.TAB, Keys.ENTER)
element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[5]/div/div/div[1]/div/form/button')));element.click()
element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/nav/ul/li/a')));element.click()
print('SYSTEM : [1/20]')

for i in range(count):
        sleep(450)
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button')));element.click()
        fill_info = driver.find_element_by_xpath('/html/body/div[4]/div[5]/div/form/div/input')
        fill_info.send_keys(link, Keys.TAB, Keys.ENTER)
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[5]/div/div/div[1]/div/form/button')));element.click()
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/nav/ul/li/a')));element.click()
        count += 1
        print('SYSTEM : ['+str(count)+'/20]')
        os.close
