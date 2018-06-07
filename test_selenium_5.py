from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 鼠标悬停至“设置”链接
link = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(link).perform()

# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
time.sleep(3)

print('now save window!')
# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(3)
# 接受警告框
driver.switch_to.alert.accept()
time.sleep(3)
driver.quit()