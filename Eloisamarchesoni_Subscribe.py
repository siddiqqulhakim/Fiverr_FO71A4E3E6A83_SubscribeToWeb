from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import csv
from time import sleep
import pandas as pd

def option_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--incognito")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("prefs",{'credentials_enable_service': False, 'profile': {'password_manager_enabled': False}})

    return options

def subscribe(email):
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=option_driver())
        print("Opening web page")
        driver.get("https://eloisamarchesoni.substack.com/?utm_source=homepage_recommendations&utm_campaign=1141658")
        sleep(2)
        
        WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="email"]'))).send_keys(email)
        sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        sleep(3)
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="button subscribe-to-more"]'))))
        sleep(3)
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="button maybe-later"]'))))
        sleep(7)

        driver.quit()

    except Exception as e:
        print("ERROR HAPPEN" + str(e))
        subscribe(email)

df = pd.read_csv("email_list.txt", delimiter=" ", header=None)

for index, row in df.iterrows():
    print("Processing Row " + str(index) + " Email " + row[0])
    subscribe(row[0])

k = input("\nPress enter to exit...")