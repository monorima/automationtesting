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


# ActionChains(driver).move_to_element(driver.sl.find_element_by_id('my-id')).perform()


# time.sleep(15) 

# training_center = driver.find_element_by_link_text('Training Center')
# training_center.click()

# time.sleep(5)
# backtodashboard_btn = driver.find_element_by_class_name('back_to_dashbord')
# backtodashboard_btn.click()

time.sleep(15)
training_progressbar = driver.find_elements_by_css_selector(".progress_div_wrapper_body .progress_div_wrapper .ng-star-inserted")
print(training_progressbar,'++')
training_progressbar[4].click()

time.sleep(5)
frst_lesson = driver.find_element_by_id('6128c94c79643200083950e9')
frst_lesson.click()

time.sleep(2)
next_btn = driver.find_elements_by_css_selector('.training_center_wrapper .rowinner_block .markbtncls')
next_btn.click()





