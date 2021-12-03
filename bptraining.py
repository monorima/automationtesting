from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window() 
driver.get('https://backoffice.betoparedes.com/login')

username = 'darnellrojas23@outlook.com'
password = 'P@ss1234'

username_box = driver.find_element_by_id('mat-input-0')
pass_box = driver.find_element_by_id('mat-input-1')
login_btn = driver.find_element_by_css_selector('.mat-raised-button')

username_box.send_keys(username)
pass_box.send_keys(password)
login_btn.click()

time.sleep(15)

training_nav = driver.find_element_by_class_name('submenu')
training_nav.click()

time.sleep(2)

# training_center = driver.find_element_by_name('training center')
# print(training_center,'print training data')

training_center_data = driver.find_element_by_css_selector('.submenu ul li')
# print(training_center_data,'print training data') 
training_center_data.click()

time.sleep(5)

training_lesson = driver.find_element_by_class_name('alllession_cls')
print(training_lesson, 'print training lesson data')

