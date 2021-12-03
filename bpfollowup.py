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
leads_btn = driver.find_element_by_link_text('Leads')
leads_btn.click()

time.sleep(8)
# lead_followup_btn = driver.find_elements_by_css_selector("[mat-align-tabs=center] .mat-tab-labels")
lead_followup_btn = driver.find_element_by_id('mat-tab-label-0-3')
print(lead_followup_btn,'++')
# lead_followup_btn[2].click()
lead_followup_btn.click()

time.sleep(5)
leadphone_box = driver.find_elements_by_class_name('searchdiv')
leadphone_box[0].click()
search_by_lead_phone = '504-621-8928'
time.sleep(1)
leadphone_box[0].send_keys(search_by_lead_phone)

val = driver.find_element_by_id('mat-input-18')
val.send_keys(username)
leadphone_box[1].send_keys(username)

# print(leadphone_box, 'search data')
# search_button = driver.find_elements_by_css_selector('searchbtncls')

# search_button.click()

