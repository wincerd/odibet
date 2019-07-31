from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time 
from config import  conf

class scraper():
    def connect(self):
        url ="https://odibets.com/"
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.implicitly_wait(3) 
        self.driver.find_element_by_link_text("Login").click()
        number= conf["username"]
        password=conf["password"]
        self.driver.find_element_by_name("msisdn").send_keys(number)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element(By.XPATH, '//button[text()="Login"]').click()
    def main(self):
        self.connect()
if __name__ == "__main__":
    new = scraper()
    new.main()