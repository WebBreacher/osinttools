import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

query  = 'webbreacher'

driver = webdriver.Chrome(executable_path='c:/Users/micah/chromedriver/chromedriver.exe')
url    = 'http://www.google.com'
driver.get(url)

time.sleep(1)

# find the search box
search_box = driver.find_element_by_name('q')

# now enter your query
search_box.send_keys(query)

# hit the ENTER key
search_box.send_keys(Keys.ENTER)

print("[*] Google search results for: %s" % query)

time.sleep(2)

# find all of the results groups
search_results = driver.find_elements_by_class_name("r")

for result in search_results:
    
    # extract the link
    result_link_object = result.find_element_by_tag_name("a")
    
    # extract the link text and the website
    result_link = result_link_object.get_attribute("href")
    result_text = result_link_object.text
    
    print("%s - %s" % (result_link,result_text))

# kill the browser
driver.quit()