import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

account  = 'automatingosint'

driver = webdriver.Chrome(executable_path='c:/Users/micah/chromedriver/chromedriver.exe')
url    = 'http://pastebin.com/u/' + account
driver.get(url)
print('[*] Visiting {} now'.format(url))
time.sleep(1)


paste = driver.find_element_by_class_name('i_p0')
# find the DIV tag that contains the visuallyhidden
visibility_span = driver.find_element_by_class_name("visuallyhidden")

# find the SPAN tag embedded within the DIV tag
#visibility_value = visibility_span.find_element_by_tag_name("span")

# print out the visibility value
print(visibility_span.text.replace("n",""))


for paste in pastes:
    test = paste.find_element_by_xpath('//href')
    for t in test:
        print(t)    

    continue
    # extract the link
    result_link_object = paste.find_element_by_tag_name("a")
    print(result_link_object)
    
    # extract the link text and the website
    result_link = result_link_object.get_attribute("href")
    result_text = result_link_object.text
    
    print("%s - %s" % (result_link,result_text))


# kill the browser
driver.quit()