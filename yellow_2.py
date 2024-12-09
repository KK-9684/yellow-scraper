import pandas as pd
import requests
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import undetected_chromedriver as uc

a = []
b = []
c = []
d = []
e = []

options = uc.ChromeOptions() 
options.headless = True 
for i in range(1, 6):
    driver = uc.Chrome()
    driver.get("https://www.yellowpages.com.au/")
    # driver.maximize_window()
    time.sleep(5)
    df = pd.read_csv('list'+str(i)+'.csv')
    for index, row in df.iterrows():
        driver.get(row[0])
        print(index)
        try:
            try:
                aa = driver.find_element(By.CLASS_NAME, 'listing-name')
                a.append(aa.text)
            except:
                a.append('None')
            try:
                bb = driver.find_element(By.CLASS_NAME, 'contact-email')
                b.append(bb.get_attribute('data-email'))
            except:
                b.append('None')
            try:
                cc = driver.find_element(By.CLASS_NAME, 'desktop-display-value')
                c.append(cc.text)
            except:
                c.append('None')
            try:
                dd = driver.find_element(By.CLASS_NAME, 'listing-address')
                d.append(dd.text)
            except:
                d.append('None')
            try:
                ee = driver.find_element(By.CLASS_NAME, 'contact-url')
                e.append(ee.get_attribute('href'))
            except:
                e.append('None')
        except:
            pass
    df = pd.DataFrame({'business_name': a, 'business_email': b, 'business_phone_number': c, 'business_location': d, 'business_website_url': e})
    df.to_csv('data'+str(i)+'.csv', index=False, encoding='utf-8')
    a = []
    b = []
    c = []
    d = []
    e = []
    driver.close()
    time.sleep(10)




    