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

time.sleep(6)
leadphone = '74120589677'
leadphone_box = driver.find_element_by_id('mat-input-20')
leadphone_box.send_keys(leadphone)

time.sleep(5)
search_btn = driver.find_element_by_css_selector('.searchbtncls .add_button')
search_btn.click()

time.sleep(2)
eventtype = driver.find_element_by_css_selector('.mat-select-placeholder')
eventtype.click()

searchupcommingevent = driver.find_element_by_id('mat-option-6')
searchupcommingevent.click()