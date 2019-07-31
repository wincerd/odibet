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
    def page(self):
        test_elem = self.driver.find_elements_by_xpath("//div[@class='l-container m-pagination']//td")
        return (len(test_elem))
    def next_page(self,page):
        page =str(page)
        self.driver.get("https://odibets.com/sport/soccer?p="+page)
    def balance(self):
        bal=self.driver.find_element(By.XPATH, '//div[@class="l-account"]/a').text
        bal = float(str(bal).replace("Account: ",""))
        return bal
    def matches(self):
        links= self.driver.find_elements(By.XPATH,'//div[@class = "l-events"]//a[@href]')
        regex= re.compile ("(.*\w{3}\/\w{0,5}\?\w{2}=\d{0,10}$)")
        all_links=[]
        for link in links:
            all_linkz=link.get_attribute("href")
            if regex.search(all_linkz)  is not None:
                all_links.append(all_linkz)
        return all_links
    def match_details(self):
        "get match details"
        try:
            league =self.driver.find_element(By.XPATH,'//*[@id="cont"]/div[6]/div[1]/div/a[3]').text
            team_1 =self.driver.find_element(By.XPATH,'//*[@id="cont"]/div[6]/div[2]/div[1]').text
            team_2 =self.driver.find_element(By.XPATH,'//*[@id="cont"]/div[6]/div[2]/div[3]').text
            time =self.driver.find_element(By.XPATH,'//*[@id="cont"]/div[6]/div[3]/span[1]').text
            date =(str(time)[6:]+"/2019")
            time =(str(time)[:-5])
            home_win=self.driver.find_element(By.XPATH,'//div[@class="l-markets"]/div[2]/div[1]/div[2]/div/button[1]/span[2]').text
            draw=self.driver.find_element(By.XPATH,'//div[@class="l-markets"]/div[2]/div[1]/div[2]/div/button[2]/span[2]').text
            away_win=self.driver.find_element(By.XPATH,'//div[@class="l-markets"]/div[2]/div[1]/div[2]/div/button[3]/span[2]').text 
            d12=self.driver.find_element(By.XPATH,'//div[@class="l-markets"]/div[2]/div[2]/div[2]/div/button[1]/span[2]').text 
            dx2=self.driver.find_element(By.XPATH,'//div[@class="l-markets"]/div[2]/div[2]/div[2]/div/button[2]/span[2]').text 
            d1x=self.driver.find_element(By.XPATH,'//div[@class="l-markets"]/div[2]/div[2]/div[2]/div/button[3]/span[2]').text 
            return league,team_1,team_2,date,time,home_win,draw,away_win,d12,dx2,d1x
        except:
             print("not found")
             return (1)
    def withdraw(self):
        pass
    def nav(self):
        "navigation to start page"
        self.driver.find_element(By.XPATH,'//div[@class="l-menu"]/ul[1]/li[1]/a').click()
        self.driver.implicitly_wait(3)
        "navigation to today page"
        self.driver.find_element(By.XPATH,'//div[@class="l-events"]/div[1]/a[4]/span').click()
        self.driver.implicitly_wait(3)
    def bet(self,side,amount):
        if side == "1":
            print(amount)
            self.driver.find_element(By.XPATH,'//*[@id="cont"]/div[@class="l-markets"]/div[2]/div[1]/div[2]/div/button[1]/span[2]').click()
        elif side == "x":
            self.driver.find_element(By.XPATH,'//div[@class="l-markets"]/div[2]/div[1]/div[2]/div/button[2]/span[2]').click()
        elif side == "2":
            self.driver.find_element(By.XPATH,'//div[@class="l-markets"]/div[2]/div[1]/div[2]/div/button[3]/span[2]').click()
        elif side == "12":
            self.driver.find_element(By.XPATH,'//div[@class="l-markets"]/div[2]/div[2]/div[2]/div/button[1]/span[2]').click()
        elif side == "2x":
            self.driver.find_element(By.XPATH,'//div[@class="l-markets"]/div[2]/div[2]/div[2]/div/button[2]/span[2]').click()
        elif side == "1x":
            self.driver.find_element(By.XPATH,'//div[@class="l-markets"]/div[2]/div[2]/div[2]/div/button[3]/span[2]').click()
        self.driver.find_element(By.XPATH,'//div[@class="placebet"]/a').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH,'//div[@class="stake"]/input[2]').click()
        self.driver.find_element(By.XPATH,'//div[@class="stake"]/input[2]').clear()
        #enter bet amount
        self.driver.find_element(By.XPATH,'//div[@class="stake"]/input[2]').send_keys(amount)
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH,'//div[@class="stake"]/button[@class="update"]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,'//button[@class="l-betslip-cta-btn"]').click()
    def main(self):
        self.connect()
        self.balance()
        self.nav()
##        self.next_page()
        for i in self.matches():
            self.driver.get(i)
            self.driver.implicitly_wait(3)
            print(self.match_details())
            #self.bet("1",1)
            


if __name__ == "__main__":
    new = scraper()
    new.main()
