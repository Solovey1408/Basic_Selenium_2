import time
from datetime import datetime, timedelta #Импорт Timedelta для изменения даты

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless") #Браузер открывается в headless режиме

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.set_window_size(1920, 1080)

date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
date_input.send_keys(Keys.CONTROL + 'a')
date_input.send_keys(Keys.DELETE)

time.sleep(1)

current_date = datetime.now() #Дата в настоящее время
future_date = current_date + timedelta(days=10) #С помощью timedelta прибавляем 10 дней
future_date_input = future_date.strftime("%d.%m.%Y") #Конвертируем дату для ввода

date_input.send_keys(future_date_input)