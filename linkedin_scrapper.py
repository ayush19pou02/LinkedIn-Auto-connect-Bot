import selenium
from selenium import webdriver
import pyautogui as pyt
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
sleep(0.5)
driver.get("https://www.linkedin.com/")
sleep(5)

file = open('Desktop\c&c++\Ayush C++\config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]



elementId = driver.find_element(By.XPATH, "//input[@name = 'session_key']")
elementId.send_keys(username)

elementId = driver.find_element(By.XPATH, "//input[@name = 'session_password']")
elementId.send_keys(password)

elementId = driver.find_element(By.XPATH, "//button[@type = 'submit']").click()

sleep(5)

search_field=driver.find_element(By.XPATH,'//*[@id="global-nav-typeahead"]/input')
search_query =input('What profile do you want to scrap?')
search_field.send_keys(search_query)
search_field.send_keys(Keys.RETURN)
print('--Finish searching...')
sleep(5)
search_more_fields=driver.find_element(By.XPATH,"//*[@id='main']/div/div/div[1]/div[2]/a")

sleep(0.5)
search_more_fields.click()
sleep(5)
for i in range(0,2,1):
    allProfiles=driver.find_elements(By.XPATH,"//button[not (@aria-label='Follow') and @class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")
    sleep(2)
    for profile in allProfiles:
        profile_click= driver.find_element(By.XPATH,"//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']//span[@class='artdeco-button__text']")
        sleep(3)
        profile_click.click()
        sleep(1)
        addNote=driver.find_element(By.XPATH,"//button[@class='artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view mr1']")
        sleep(0.5)
        addNote.click()
        sleep(0.5)
        custom_message='Hello, I have found mutual interest area and I would like to connect with you'
        message =driver.find_element(By.XPATH,"//textarea[@id='custom-message']")
        message.send_keys(custom_message)
        send_message=driver.find_element(By.XPATH,"//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view ml1']")
        sleep(0.5)
        send_message.click()
        sleep(2)
    nextPage=driver.find_element(By.XPATH,"//button[@class='artdeco-pagination_button artdeco-pagination_button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view']")
    sleep(0.5)
    nextPage.click()
    sleep(2)

sleep(50)

driver.quit()