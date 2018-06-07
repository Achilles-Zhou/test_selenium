from selenium import webdriver
from time import sleep

# 访问百度
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 设置浏览器窗口大小
driver.set_window_size(500, 500)
sleep(2)
# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").submit()
sleep(5)

# 通过javascript设置浏览器窗口的滚动条位置
js = "window.scrollTo(100,450);"
driver.execute_script(js)
sleep(3)

driver.quit()
