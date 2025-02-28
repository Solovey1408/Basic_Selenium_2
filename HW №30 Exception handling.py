import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException #Импорт исключения из библиотеки

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless") #Браузер открывается в headless режиме

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.set_window_size(1920, 1080)


try: #Попытка произвести поиск и кликнуть по кнопке
    button_visible = driver.find_element(By.XPATH,"//button[@id='visibleAfter']")
    button_visible.click()
except NoSuchElementException: #Если выходит исключение NoSuchElementException
    print('Get NoSuchElementException')
    time.sleep(5) #Ждем 5 секунд
    driver.refresh() #Обновляем страницу
    time.sleep(5) #Ждем 5 секунд
    button_visible = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    button_visible.click() #Находим и делаем клик по кнопке
    print('Click Button Visible')