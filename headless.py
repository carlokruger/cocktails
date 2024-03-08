# Mossein~King(hi i'm here to help)
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chromium import options


from bs4 import BeautifulSoup

from selenium import webdriver
    
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# create a new instance of the Firefox driver
# driver = webdriver.Chromium

# navigate to the login page
driver.get("https://iba-world.com/alexander/")

# locate the "Sign In" button by its text and click on it
# driver.find_element_by_xpath("/html/body/div[8]/p[2]/button[1]").click()


#this.is.for.headless.This.will.save.you.a.bunch.of.research.time(Trust.me)
# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Firefox(firefox_options=options)

#for.graphical(you.need.gecko.driver.for.firefox)
# driver = webdriver.Firefox()

url = 'https://iba-world.com/alexander/'
driver.get(url)

#get.the.link.to.clicking
#exaple if<a class='MosseinKing'>
# if <button class="yes">YES</button>
# driver.find_element_by_xpath("/html/body/div[8]/p[2]/button[1]").click()
driver.find_element_by_class("yes").click()


#wait.1.secong.in.case.of.transitions
time.sleep(1)

pagesource = driver.page_source
soup = BeautifulSoup(pagesource)

#you.can.now.enjoy.soup
print(soup)