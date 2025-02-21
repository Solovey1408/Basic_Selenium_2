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

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys("standard_user")
print('Input login')

user_password = driver.find_element(By.XPATH, '//input[@id="password"]')
user_password.send_keys("secret_sauce")
print('Input password')

button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print('Click login button')

#Название товара №1
product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

#Название товара №2
product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']")
value_product_2 = product_2.text
print(value_product_2)

#Цена товара №1
price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

#Цена товара №2
price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)

#Добавление в корзину товара №1
select_product_1 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print('Select Product 1')

#Добавление в корзину товара №2
select_product_2 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
select_product_2.click()
print('Select Product 2')

#Открываем корзину
cart = driver.find_element(By.XPATH,"//*[@class='shopping_cart_link']")
cart.click()
print('Enter Cart')

#Наличие товара №1 в корзине
cart_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)

#Наличие товара №2 в корзине
cart_product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']")
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)

#Проверка, что название товара №1 в каталоге равно названию товара №1 в корзине
assert value_product_1 == value_cart_product_1, 'Error: Info Cart Product 1 Not Good'
print('Info Cart Product 1 Good')

#Проверка, что название товара №2 в каталоге равно названию товара №1 в корзине
assert value_product_2 == value_cart_product_2, 'Error: Info Cart Product 2 Not Good'
print('Info Cart Product 2 Good')

#Цена товара №1 в корзине
price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)

#Цена товара №2 в корзине
price_cart_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_cart_price_product_2 = price_cart_product_2.text
print(value_cart_price_product_2)

#Проверка, что цена товара №1 в каталоге равно цене товара №1 в корзине
assert value_price_product_1 == value_cart_price_product_1, 'Error: Info Cart Price Product 1 Not Good'
print('Info Cart Price Product 1 Good')

#Проверка, что цена товара №2 в каталоге равно цене товара №2 в корзине
assert value_price_product_2 == value_cart_price_product_2, 'Error: Info Cart Price Product 2 Not Good'
print('Info Cart Price Product 2 Good')

#Оформление заказа
checkout = driver.find_element(By.XPATH, "//*[@id='checkout']")
checkout.click()
print('Click Checkout')

#Заполнение формы заказа. Ввод имени
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Mike')
print('Input First Name')

#Заполнение формы заказа. Ввод фамилии
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Fix')
print('Input Last Name')

#Заполнение формы заказа. Ввод индекса почты
postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys(123456)
print('Input Postal Code')

#Нажимаем кнопку продолжить в форме заполнения личной информации
button_continue = driver.find_element(By.XPATH, "//*[@id='continue']")
button_continue.click()
print('Click Continue')

#Имя продукта 1 на странице покупки
finish_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)

#Имя продукта 2 на странице покупки
finish_product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']")
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)

#Сравнение Имя продукта 1 на странице покупки и на странице каталога
assert value_product_1 == value_finish_product_1, 'Error: Info Finish Product 1 Not Good'
print('Info Finish Product 1 Good')

#Сравнение Имя продукта 2 на странице покупки и на странице каталога
assert value_product_2 == value_finish_product_2, 'Error: Info Finish Product 2 Not Good'
print('Info Finish Product 2 Good')

#Цены продукта 1 на странице покупки
price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)

#Цены продукта 2 на странице покупки
price_finish_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_finish_price_product_2 = price_finish_product_2.text
print(value_finish_price_product_2)

#Сравнение Цены продукта 1 на странице покупки и на странице каталога
assert value_price_product_1 == value_finish_price_product_1, 'Error: Info Finish Price Product 1 Not Good'
print('Info Finish Price Product 1 Good')

#Сравнение Цены продукта 2 на странице покупки и на странице каталога
assert value_price_product_2 == value_finish_price_product_2, 'Error: Info Finish Price Product 2 Not Good'
print('Info Finish Price Product 2 Good')

#Сумма денег за товары
summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)

#Проверка суммированием цены 1 и 2 товара
item_total = "Item total: $" + str((float(value_finish_price_product_1[1:])) + (float(value_finish_price_product_2[1:])))
print(item_total)

#Проверка, что суммы равны
assert value_summary_price == item_total, 'Error: Total Summary Price Not Good'
print('Total Summary Price Good')

#Нажимаем кнопку оформления
button_finish = driver.find_element(By.XPATH, "//*[@id='finish']")
button_finish.click()
print('Click Button Finish')

#Текст успешного оформления заказа
checkout_complete = driver.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)

#Проверяем текст успешного оформления заказа
assert value_checkout_complete == 'Thank you for your order!', 'Error: Info Order Crash!'
print('Info Order Complete!')