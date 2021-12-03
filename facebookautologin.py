from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.facebook.com/')

username = 'joshuagreen7890@gmail.com'
password = 'P@ss123'

username_box = driver.find_element_by_id('email')
pass_box = driver.find_element_by_id('pass')
login_btn = driver.find_element_by_name('login')

username_box.send_keys(username)
pass_box.send_keys(password)
login_btn.click()
