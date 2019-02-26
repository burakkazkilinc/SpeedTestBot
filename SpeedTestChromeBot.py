# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 22:54:27 2019

@author: Burakk

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import datetime
#import pylab
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

browser = webdriver.Chrome("C:/chromedriver.exe")
browser.get("https://www.speedtest.net/")
browser.implicitly_wait(3)
test_et = browser.find_element_by_xpath("//*[@id='container']/div[2]/div/div/div/div[3]/div[1]/div[1]/a/span[4]")
test_et.click()

element = WebDriverWait(browser, 45).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[3]/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div[1]/a[1]")))
element.click()

browser.implicitly_wait(2)
link_al = browser.find_element_by_id('share-image').get_attribute('value')
urllib.request.urlretrieve(link_al, "speedtest_"+datetime.datetime.today().strftime('%I%M%p-%d%m%Y')+".png")
print("indirme tamamlandı")
browser.close()

img=mpimg.imread("speedtest_"+datetime.datetime.today().strftime('%I%M%p-%d%m%Y')+".png")
imgplot = plt.imshow(img)
plt.show()






