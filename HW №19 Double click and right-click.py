from selenium import webdriver
from selenium.webdriver import ActionChains
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

base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Выполняем двойной клик
action = ActionChains(driver)
double_click_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double_click_button).perform()
print('Made Double Click')

#Выполняем правый клик
right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click_button).perform()
print('Made Right Click Button')

#Сообщение при выполнении двойного клика
message_double_click_button = driver.find_element(By.XPATH, "//*[contains(text(), 'You have done a double click')]")
value_message_double_click_button = message_double_click_button.text

#Проверка сообщения при выполнении двойного клика
assert value_message_double_click_button == 'You have done a double click', 'Error: Info Double Click Failed!'
print('Info Double Click Complete!')

#Сообщение при выполнении правого клика
message_right_click_button = driver.find_element(By.XPATH, "//*[contains(text(), 'You have done a right click')]")
value_message_right_click_button = message_right_click_button.text

#Проверка сообщения при выполнении правого клика
assert value_message_right_click_button == 'You have done a right click', 'Error: Info Right Click Failed!'
print('Info Right Click Complete!')