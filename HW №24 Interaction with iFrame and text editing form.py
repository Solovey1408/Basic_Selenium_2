from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Переключаемся на iframe
iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)

#Находим текст в поле iframe
input_pole = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]")

#Меняем текст в поле iframe
input_pole.send_keys(Keys.CONTROL + 'a') #Выделяем старый текст
input_pole.send_keys(Keys.BACKSPACE) #Удаляем старый текст
input_pole.send_keys("Hello World!") #Вводим новый текст
input_pole.send_keys(Keys.CONTROL + 'a') #Выделяем новый текст
print('Input Hello World!')

#Переводим объект в поле iframe в формат текста
value_pole = input_pole.text
print(value_pole)

#Находим кнопку Bold и делаем новый текст жирным
click_editing_panel_bold = driver.find_element(By.XPATH, "//button[@title='Bold']")
click_editing_panel_bold.click()
print('Click editing panel Bold')

#Находим кнопку Italic и делаем новый текст под наклоном
click_editing_panel_italic = driver.find_element(By.XPATH, "//button[@title='Italic']")
click_editing_panel_italic.click()
print('Click editing panel Italic')

#Находим отредактированный текст в поле iframe
new_input_pole = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/b/i")
value_input_pole = new_input_pole.text

#Проверяем, что исходный введенный текст и отредактированный текст одинаковые
assert value_pole == value_input_pole, 'Input and Editing text Failed'
print('Input and Editing text Complete')