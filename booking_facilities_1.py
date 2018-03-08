from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver.maximize_window()
# driver.set_window_size(1124, 850) # set browser size.
driver.get("https://members.myactivesg.com/facilities/quick-booking")

ActionChains(driver).move_to_element(driver.find_element_by_css_selector("chosen-container")).perform()

# select = Select(driver.find_element_by_name('activity_filter'))
# driver.execute_script("document.getElementById('activity_filter').style.display='inline-block';")
# select.select_by_visible_text('Basketball')

# select = Select(driver.find_element_by_name('venue_filter'))
# driver.execute_script("document.getElementById('venue_filter').style.display='inline-block';")
# select.select_by_visible_text('MOE (Evans) Sports Hall')

# size = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@name='activity_filter']"))).click()
# size = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='activity_filter']/option[@value='468']"))).click()
# driver.execute_script("document.querySelectorAll('label.boxed')[1].click()")
# size.click()
# size.send_keys("Basketball")

# elem = driver.find_element_by_xpath("//select[@name='activity_filter']")
# driver.execute_script('arguments[0].scrollIntoView();', elem)
# elem.click()

# browser.execute_script("arguments[0].scrollIntoView(true);", elem)
# elem.click()
# elem.send_keys("Basketball")
# browser.find_element_by_xpath("//select[@name='activity_filter']/option[@value='468']").click()

# driver.execute_script("document.getElementsByClassName('chosen-container chosen-container-single')[0].click()")
# print(select.options)


# elem = browser.find_element_by_name("activity_filter")
# elem.click()
# elem.send_keys("Basketball")

# elem = browser.find_element_by_name("venue_filter")
# elem.send_keys("MOE (Evans) Sports Hall")

# elem = browser.find_element_by_name("date_filter")
# elem.send_keys("Sun, 25 Feb 2018")