import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:/Users/micah/chromedriver/chromedriver.exe")
url    = "http://www.theweathernetwork.com/weather/united-states/florida/miami"
driver.get(url)

time.sleep(1)

# find the DIV tag that contains the visuallyhidden
visibility_span = driver.find_element_by_class_name("visuallyhidden")

# find the SPAN tag embedded within the DIV tag
#visibility_value = visibility_span.find_element_by_tag_name("span")

# print out the visibility value
print(visibility_span.text.replace("n",""))

# close the browser
driver.quit()