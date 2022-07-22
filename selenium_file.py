from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def linkedinUserProfile(username):
    url = "https://www.linkedin.com/login/"
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(executable_path = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe", options=options)
    driver.get(url)
    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@name = "session_key"]').send_keys("i.syedsalmanali@gmail.com")
    driver.find_element(By.XPATH,'//*[@name = "session_password"]').send_keys("Salman")
    driver.find_element(By.XPATH,'//button[@class="btn__primary--large from__button--floating"]').click()
    time.sleep(3)
    
    profile_url = f"https://www.linkedin.com/in/{username}"
    driver.get(profile_url)

    time.sleep(3) 
    
    return driver

