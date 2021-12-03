from selenium import webdriver   #from selenium package import webdriver module
import time      #import time library
driver = webdriver.Chrome() 
driver.maximize_window()

driver.get('https://www.instagram.com/')   #.get is a method used to load the target url

username = '____.lily007___'  #variable
password = 'P@ss0987'         #variable

time.sleep(2)    #used for delay in execution of the process
username_input = driver.find_element_by_name('username')   #finding element by name of the targated page
username_input.send_keys(username)                      #
password_input = driver.find_element_by_name('password')
password_input.send_keys(password)

time.sleep(1)



login_btn = driver.find_element_by_css_selector('._4EzTm')



login_btn.click()

time.sleep(2)
notnow_btn = driver.find_element_by_css_selector('.yWX7d')
notnow_btn.click()

time.sleep(2)

turnon_btn = driver.find_element_by_css_selector('.bIiDR')
turnon_btn.click()


time.sleep(2)

my_account = driver.find_element_by_css_selector('._6q-tv')
my_account.click()

time.sleep(1)
next_btn = driver.find_element_by_class_name('coreSpriteRightChevron')
next_btn.click()
