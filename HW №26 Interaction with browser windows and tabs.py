import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #Браузер открывается в headless режиме

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Нажимаем на кнопку для открытия новой вкладки
new_tab = driver.find_element(By.XPATH,"//button[@id='tabButton']")
new_tab.click()

driver.switch_to.window(driver.window_handles[1]) #Переключаемся на вторую вкладку
time.sleep(2)
driver.switch_to.window(driver.window_handles[0]) #Переключаемся обратно на первую вкладку

#Нажимаем на кнопку для открытия нового окна
new_window = driver.find_element(By.XPATH,"//button[@id='windowButton']")
new_window.click()

driver.switch_to.window(driver.window_handles[1]) #Переключаемся на новое окно
time.sleep(2)
driver.switch_to.window(driver.window_handles[0]) #Переключаемся обратно на старое окно

