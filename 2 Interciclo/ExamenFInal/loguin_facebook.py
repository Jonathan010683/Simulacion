from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
import os
import pyautogui
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

import xlrd 

def facebook():

    usr = "jonatanuzhca@yahoo.com"
    pwd = "***************"
    driver = webdriver.Firefox(executable_path=r'C:\dirverFirefox\geckodriver.exe')

    
    driver.get("http://www.facebook.com")
    sleep(2)
    
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
   
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
   
    elem.send_keys(Keys.RETURN)
    sleep(20)
    
    elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/span[2]/span").click()    
    pyautogui.write('yaku')
    pyautogui.press("enter")
    
    sleep(5)
    elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div").click()
    
def correo():
    
    driver = webdriver.Firefox(executable_path=r'C:\dirverFirefox\geckodriver.exe')
    
    driver.get("https://www.canva.com/design/DAEVwTlOGtw/mBUl5Kr4swutnSFpPPfBoQ/edit")
  
    
    driver.get("https://temp-mail.org/es/")
    
    
    element = driver.find_element(By.ID, "click-to-refresh")
    

    element = driver.find_element(By.ID, "click-to-delete")
    
   
    element = driver.find_element(By.ID, "click-to-refresh")
    
   
    element = driver.find_element(By.ID, "click-to-delete")
    

    element = driver.find_element(By.ID, "click-to-refresh")
    sleep(2)
    driver.get("https://generadordenombres.online/")
    driver.set_window_size(814, 824)
    driver.find_element(By.ID, "nombreGenerado").click()
    driver.find_element(By.LINK_TEXT, "Generar otro").click()
    driver.find_element(By.LINK_TEXT, "Generar otro").click()
    driver.find_element(By.LINK_TEXT, "Generar otro").click()
    
    driver.find_element(By.LINK_TEXT, "Mujer").click()
    sleep(5)
    driver.find_element(By.LINK_TEXT, "Generar otro").click()
    
    driver.find_element(By.LINK_TEXT, "Generar otro").click()
    driver.find_element(By.LINK_TEXT, "Generar otro").click()
    sleep(5)
      
    df = pd.read_excel('C:/Users/Acer/Desktop/Contacto.xlsx')
    print(df)
    
def imagen():
   
    now = datetime.now()
    anio = str(now.year)
    mes = str(now.month)
    hora = str(now.hour)
    minu = str(now.minute)
    segundo = str(now.second)
    
    dia = str(now.day)
    dato = anio+"/"+mes+"/"+dia+"   "+hora+":"+minu+":"+segundo
    image = Image.open("C:/Users/Acer/Downloads/yaku.png")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 30)
     
    draw.text((80, 50), dato , font=font,fill="black")
    image.save("C:/Users/Acer/Desktop/yaku.png")
    
def enviar():
    
    driver = webdriver.Firefox(executable_path=r'C:\dirverFirefox\geckodriver.exe')
    
    driver.get("https://login.live.com/")
    elem = driver.find_element_by_id("i0116")
    elem.send_keys("tata-1995.yo@hotmail.com")
    driver.find_element_by_id("idSIButton9").click()
    sleep(2)
    elem = driver.find_element_by_id("i0118")
    elem.send_keys("jhon12345")
    driver.find_element_by_id("idSIButton9").click()
    sleep(5)
    driver.get("https://outlook.live.com/mail/0/inbox")
    sleep(5)
    driver.find_element_by_id("id__5").click()
    sleep(5)
    elem1 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/input").click()
    
    df = pd.read_excel('C:/Users/Acer/Desktop/Contacto.xlsx')
    print(df.correo)
    
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/input").send_keys(df.correo+",")
    
    sleep(5)
    elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[3]/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/button/span/div/div/img").click()
    driver.find_element_by_xpath("/html/body/div[12]/div/div/div/div/div/div/ul/li[6]/button/div/span").click()
    
    pyautogui.write("yaku")
    pyautogui.press("enter")
    sleep(10)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[3]/div[2]/div[1]/div/span/button[1]").click()
    driver.find_element_by_id("ok-1").click()
    
if __name__ == '__main__':    
    correo()
    imagen()
    facebook()
    enviar()
