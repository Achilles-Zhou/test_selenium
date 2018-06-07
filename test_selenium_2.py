from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)

# 定位一组元素
texts = driver.find_elements_by_xpath('//div/h3/a')

# 循环遍历出每一条搜索结果的标题
for t in texts:
    print(t.text)

driver.quit()