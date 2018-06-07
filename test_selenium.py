from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

# go to the google home page
driver.get("http://www.baidu.com/")

# the page is ajaxy so the title is originally this:
print(driver.title)

# get cookie
cookie = driver.get_cookies()
print(cookie)
# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("wd")

# type in the search
inputElement.send_keys("cheese!")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.center("cheese!"))

    # You should see "cheese! - Google Search"
    print(driver.title)

finally:
    driver.quit()
