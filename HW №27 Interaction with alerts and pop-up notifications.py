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

base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Нажимаем кнопку Алерт с кнопкой подтверждения
click_alert_button = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
click_alert_button.click()
print('Click Alert Button')

time.sleep(3)

#Нажимаем кнопку подтверждения в Алерте
driver.switch_to.alert.accept()

#Нажимаем кнопку Алерт с кнопками подтверждения и отменой
click_confirm_button = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
click_confirm_button.click()
print('Click JS Confirm Button')

time.sleep(3)

#Нажимаем кнопку отмены в Алерте
driver.switch_to.alert.dismiss()

#Нажимаем кнопку Алерт с вводом текста
click_alert_input_button = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
click_alert_input_button.click()
print('Click JS Prompt Button')

time.sleep(3)

driver.switch_to.alert.send_keys("Hello") #Вводим текст в алерте
driver.switch_to.alert.accept() #Нажимаем подтвердить в алерте