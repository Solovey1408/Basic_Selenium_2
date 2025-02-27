import glob
import os
import time
from sys import path_hooks

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Указываем путь куда нужно скачать файл
path_download = "C:\\Users\\songf\\Desktop\\EduIT\\BasicPython\\1\\Basic_Selenium_2\\downloads\\"

options = webdriver.ChromeOptions()
prefs = {'download.default_directory': path_download}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)
options.add_argument("--headless") #Браузер открывается в headless режиме

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Нажимаем на кнопку скачивания файла на сайте
click_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
click_button.click()

time.sleep(3)

file_name = "LambdaTest.pdf"
file_path = path_download + file_name

assert os.access(file_path, os.F_OK) == True, 'File not in directory'
print('File in directory')

files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    a = os.path.getsize(file)
    if a > 10:
        print('File is not empty')
    else:
        print('File Empty')

files = glob.glob(os.path.join(path_download, "*.*"))

# for file in files:
#     os.remove(file)