from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
import requests

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://128.199.150.205/#")

# get the username and password text field
username_field = driver.find_element_by_id("id_username")
username_field.clear()
password_field = driver.find_element_by_id("id_password")
password_field.clear()

# enter search keyword and submit
username_field.send_keys("admin")
password_field.send_keys("4321dcba")
password_field.submit()

page = requests.get(driver.current_url)
tree = html.fromstring(page.content)
search_target= tree.xpath('//span[@class="hidden-xs"]/text()')
print (search_target)
"""
# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name  method
lists= driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print ("Found " + str(len(lists)) + " Searches: ")

# iterate through each element and print the text that is
# name of the search

for row in lists:
    print(row.text)


i=0
for listitem in lists:
    print(listitem)
    print(i, "- ", listitem.find_element_by_css_selector('a').get_attribute('href'))
    i=i+1
    if(i>10):
        break
"""
# close the browser window
#driver.quit()
