""" Hello I want to web scrape data from a site with an age verification pop-up using python 3.x and beautifulsoup. I can't get to the underlying text and images without clicking "yes" for "are you over 21". Thanks for any support.

EDIT: Thanks, with some help from a comment I see that I can use the cookies but am not sure how to manage/store/call cookies with the requests package.

So with some help from another user I am using selenium package so that it will work also in case it's a graphical overlay (I think?). Having trouble getting it to work with the gecko driver but will keep trying! Thanks for all the advice again, everyone.

EDIT 3: OK I have made progress and I can get the browser window to open, using the gecko driver!~ Unfortunately it doesn't like that link specification so I'm posting again. The link to click "yes" on the age verification is buried on that page as something called mlink...

EDIT 4: Made some progress, updated code is below. I managed to find the element in the XML code, now I just need to manage to click the link.

# """
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

msg = f"Unable to obtain driver for {options.capabilities['browserName']} using Selenium Manager."

driver = webdriver.Firefox('/usr/bin/firefox') # Optional argument, if not specified will search path.
driver.get('https://iba-world.com/alexander/');

url = 'https://iba-world.com/alexander/'
driver.get(url)

#
driver.find_element_by_class_name("yes").click()

#wait.1.second
time.sleep(1)

pagesource = driver.page_source
soup = BeautifulSoup(pagesource)

#you.can.now.enjoy.soup
print(soup.prettify())
""" Edit new: Stuck again, here is the current code. I seem to have isolated the element "mBtnYes" but I get an error when running the code : ElementClickInterceptedException: Message: Element is not clickable at point (625,278.5500030517578) because another element obscures it

 import time
 import selenium
 from selenium import webdriver
 from selenium.webdriver.common.keys import Keys
 from selenium.webdriver.support.ui import WebDriverWait
 from bs4 import BeautifulSoup

 driver = webdriver.Firefox(executable_path=r'/Users/jeff/Documents/geckodriver') # Optional argument, if not specified will search path.
 driver.get('https://www.shopharborside.com/oakland/#/shop/412');

 url = 'https://www.shopharborside.com/oakland/#/shop/412'
 driver.get(url)

 #

 driver.find_element_by_id('myBtnYes').click()

 #wait.1.second
 time.sleep(1)

 pagesource = driver.page_source
 soup = BeautifulSoup(pagesource)

 #you.can.now.enjoy.soup
 print(soup.prettify()) """