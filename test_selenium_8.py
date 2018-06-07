from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.youdao.com")

# 获得cookie信息
cookie = driver.get_cookies()
# 将获得cookie的信息打印
print(cookie)

# 向cookie的name 和value中添加会话信息
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})

# 遍历cookies中的name 和value信息并打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

driver.quit()
os.popen("taskkill /F /im " + "chromedriver.exe", 'r', -1)
os.popen("taskkill /F /im " + "chrome.exe", 'r', -1)
