from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://backoffice.betoparedes.com/login')


forgot_password = driver.find_element_by_css_selector('.signupfooter')
forgot_password.click ()

email = 'monorima.influxiq@gmail.com'
email_box = driver.find_element_by_id('mat-input-2')

email_box.send_keys(email)

submit_forgotpasemail = driver.find_element_by_css_selector('.mat-raised-button')
submit_forgotpasemail.click()