from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window() 


driver.get('https://dev.bioenergetics.peceportal.com/login')

username = 'harry.bent@yopmail.com'
password = 'P@ss0987'

username_box = driver.find_element_by_id('mat-input-0')
pass_box = driver.find_element_by_id('mat-input-1')
login_btn = driver.find_element_by_css_selector('.mat-raised-button')

username_box.send_keys(username)
pass_box.send_keys(password)
login_btn.click()

time.sleep(15)

intakedropdown = driver.find_element_by_partial_link_text("Email Intake")

intakedropdown.click()
time.sleep(1)
email_intakedropdown_item = driver.find_elements_by_css_selector('.test .sub_menu .mat-menu-item')
# print(intakedropdown,'++++')
email_intakedropdown_item[0].click()


time.sleep(10)

patient_name = 'monorima saha'
patient_email = 'monorima.influxiq@gmail.com'

patient_name_input = driver.find_element_by_id('mat-input-7')
patient_email_input = driver.find_element_by_id('mat-input-8')

patient_name_input.send_keys(patient_name)
patient_email_input.send_keys(patient_email)

time.sleep(15)
selectlocation = driver.find_elements_by_id('mat-select-0')

selectlocation[0].click()

time.sleep(8)

select_location_dropdown = driver.find_elements_by_id('mat-option-0')
select_location_dropdown[0].click()

time.sleep(5)

select_tech = driver.find_elements_by_id('mat-select-1')

select_tech[0].click()

time.sleep(8)

select_tech_dropdown = driver.find_element_by_css_selector("mat-option[tabindex='0']")
select_tech_dropdown.click()

time.sleep(8)
submit_btn = driver.find_element_by_css_selector('.Addjobticket .form .form-element button:first-child')
submit_btn.click()

time.sleep(8)
copy_link = driver.find_element_by_css_selector('.bio_body .searchmodalnewdashboard button')
copy_link.click()