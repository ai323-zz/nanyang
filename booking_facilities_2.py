from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, datetime

driver = webdriver.Chrome()
driver.get("https://members.myactivesg.com/auth")

# Fill out login details
elem = driver.find_element_by_name("email")
elem.send_keys("G0954402Q")

elem = driver.find_element_by_name("password")
elem.send_keys("Aug201708")

elem.submit()

# Get the booking date
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
booking_date = str((datetime.datetime.now() + datetime.timedelta(days=14)).date()) + ' 00:00:00'
date_format='%Y-%m-%d %H:%M:%S'
os.environ['TZ']='Asia/Singapore'
epoch = int(time.mktime(time.strptime(booking_date,date_format)))

driver.get("https://members.myactivesg.com/facilities/view/activity/468/venue/318?time_from="+str(epoch))
