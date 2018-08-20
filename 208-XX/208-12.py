import os
import sys
import time
from selenium import webdriver

# 偵測作業系統
if sys.platform == 'linux':
    driver = webdriver.Chrome(os.path.abspath('./webdriver/linux/chromedriver'))
elif sys.platform == 'win32':
    driver = webdriver.Chrome(os.path.abspath('./webdriver/windows/chromedriver.exe'))
elif sys.platform == 'darwin': # macOS
    driver = webdriver.Chrome(os.path.abspath('./webdriver/mac/chromedriver'))

driver.get("http://www.pchome.com.tw")
time.sleep(3)

# 找出所有圖片連結
imgs = driver.find_elements_by_tag_name("img")
for img in imgs:
    print(img.get_attribute("src"))

driver.close()
driver.quit()

input("Enter to exit")