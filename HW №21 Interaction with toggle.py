import time

from selenium import webdriver
from selenium.webdriver import ActionChains
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

base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Двигаем ползунок
actions = ActionChains(driver)
slider = driver.find_element(By.XPATH, "//input[@class='slider-color']")
time.sleep(3)
actions.click_and_hold(slider).move_by_offset(50,0).release().perform()

#Сообщение при передвижении ползунка
message_slider = driver.find_element(By.XPATH, "//span[@id='f']")
value_message_slider = message_slider.text


#Проверка сообщения при выполнении двойного клика
assert value_message_slider == '54', 'Error: Info Slider Not Correct!'
print('Info Slider Correct!')
