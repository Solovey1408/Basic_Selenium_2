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

base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Отмечаем чек-бокс
check_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
check_box.click()

#Проверяем, что чек-бокс отмечен
check_box.is_selected()
print('Check Box Chosen')