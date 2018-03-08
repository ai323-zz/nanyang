#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('/Users/allen/Documents/projects/personal/chromedriver')
browser.get('https://eappointment.ica.gov.sg/ibook/jsp/shared/home2.jsp')
# Select apply for PR
select = Select(browser.find_element_by_name('apptDetails.apptType'))
select.select_by_visible_text('Apply for PR')
# Fill out personal info
inputElement = browser.find_element_by_name('apptDetails.identifier1')
inputElement.send_keys('IC_NO')
inputElement = browser.find_element_by_name('apptDetails.identifier2')
inputElement.send_keys('1')
inputElement = browser.find_element_by_name('apptDetails.identifier3')
inputElement.send_keys('MOBILE_NO')
# Submit online form
inputElement.submit()
