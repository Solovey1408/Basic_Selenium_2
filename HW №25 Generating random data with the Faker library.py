from faker import Faker #Импорт библиотеки Faker

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless") #Браузер открывается в headless режиме

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

fake = Faker("en_US") #Cоздание переменной для установки языка библиотеки

name = fake.first_name() #Cоздание переменной имя и с помощью .fake делаем фейковое имя
user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(name) #Вводим фейковый логин в поле для логина
print('Input Login')

