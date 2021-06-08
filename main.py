import cv2
import pytesseract
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Uemail = "" #Your email of the account you wish to pass the anticheat test
Upasswd = "" ##Your password of the account you wish to pass the anticheat test

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path = PATH, options=options)
driver.get("https://10fastfingers.com/typing-test/english")
sleep(2.5) #If you have slow internet please make this a little higher like 3-4 seconds.
driver.find_element_by_id('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
driver.find_element_by_xpath('/html/body/div[3]/div/nav/div[2]/ul[4]/li[2]/a').click()
sleep(1)

email = driver.find_element_by_id("UserEmail")
email.send_keys(Uemail)
passwd = driver.find_element_by_id("UserPassword")
passwd.send_keys(Upasswd)
loginButton = driver.find_element_by_id('login-form-submit').click()
sleep(1)

driver.get("https://10fastfingers.com/anticheat/view/1/1") #change this with the link of the typing test you want to pass.
driver.find_element_by_id("start-btn").click()
sleep(0.5) #If you have slow internet please make this a little higher like 2 seconds.

TextImage = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[3]/div[1]/img')
TextImage.screenshot("C:\\Users\\ksd12\\scripts\\anticheatBypass\\text.png") #taking screenshot of the text

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread("C:\\Users\\user\\scripts\\anticheatBypass\\text.png") #this should be the same path you saved the program + \\text.png
text = pytesseract.image_to_string(img) #converting the img to string so we can use it

input = driver.find_element_by_id("word-input")  
for words in text.split(): #writing the words
    input.send_keys(words)
    input.send_keys(Keys.SPACE)
    sleep(0) #change this if you dont want to go over 300 wpm (migh get you banned) around 0.3 and 0.5 should be good
submit = driver.find_element_by_id("submit-anticheat").click()
