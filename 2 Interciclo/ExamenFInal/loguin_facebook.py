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

def main():

    usr = "jonatanuzhca@yahoo.com"
    pwd = "Patito.1234@1234"
    

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
    sleep(5)
    
    pyautogui.write("yaku")
    pyautogui.press("enter")
    
    sleep(5)
    elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div").click()



if __name__ == '__main__':
    main()
 