from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
current_tabs = len(driver.window_handles)
WebDriverWait(driver, 600).until(EC.number_of_windows_to_be(current_tabs + 1))
