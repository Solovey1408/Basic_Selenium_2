import time

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

base_url = 'https://lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)
driver.set_window_size(1920, 1080)\

input_message = driver.find_element(By.XPATH, "//input[@id='user-message']")
message = 'Hello World'
input_message.send_keys(message)

click_button = driver.find_element(By.XPATH, "//button[@id='showInput']")
click_button.click()
time.sleep(3)

your_message = driver.find_element(By.XPATH, "//p[@id='message']")
value_your_message = your_message.text

assert value_your_message == message, 'Message is Not Correct'
print('Message is Correct')

first_value = 125
second_value = 125
sum_result = first_value + second_value

input_first_value = driver.find_element(By.XPATH, "//input[@id='sum1']")
input_first_value.send_keys(first_value)

input_first_value = driver.find_element(By.XPATH, "//input[@id='sum2']")
input_first_value.send_keys(second_value)

click_button = driver.find_element(By.XPATH, "//*[@id='gettotal']/button")
click_button.click()
time.sleep(3)

result = driver.find_element(By.XPATH, "//p[@id='addmessage']")
value_result = result.text

assert value_result == str(sum_result), 'Values Is Not Equal'
print('Values are Equal')