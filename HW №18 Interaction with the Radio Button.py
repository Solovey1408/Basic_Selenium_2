from selenium import webdriver
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

base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Нажимаем радиобаттон Impressive
radio_button = driver.find_element(By.XPATH, "(//label[@class='custom-control-label'])[2]")
radio_button.click()

#Проверяем радиобаттон Impressive
not radio_button.is_selected()
print('Radio Button Active')

#Сообщение при нажатии радиобаттона
message_radio_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Impressive')]")
value_message_radio_button = message_radio_button.text

#Проверка сообщения при нажатии радиобаттона
assert value_message_radio_button == 'Impressive', 'Error: Info Radio Button Failed!'
print('Info Radio Button Complete!')