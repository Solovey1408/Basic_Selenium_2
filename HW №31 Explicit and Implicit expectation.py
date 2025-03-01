from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless") #Браузер открывается в headless режиме

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

fake = Faker("en_US")
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Авторизация на сайте
driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("standard_user")
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauce")
driver.find_element(By.ID, 'login-button').click()

#Приветствие и выбор товара
print('''Приветствую тебя в нашем интернет - магазине!
Выбери один из следующих товаров и укажи его номер:
1 - Sauce Labs Backpack,
2 - Sauce Labs Bike Light,
3 - Sauce Labs Bolt T-Shirt,
4 - Sauce Labs Fleece Jacket,
5 - Sauce Labs Onesie,
6 - Test.allTheThings() T-Shirt (Red)''')

product_number = int(input("Enter the product number: "))

name_product = None
price_product = None
name_product_in_cart = None
price_product_in_cart = None
name_product_in_order = None
price_product_in_order = None

if product_number == 1:
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
    name_product = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']").text
    price_product = driver.find_element(By.XPATH,"//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div").text

elif product_number == 2:
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
    name_product = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']").text
    price_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div").text

elif product_number == 3:
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    name_product = driver.find_element(By.XPATH, "//*[@id='item_1_title_link']").text
    price_product = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div").text

elif product_number == 4:
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
    name_product = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']").text
    price_product = driver.find_element(By.XPATH,"//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div").text

elif product_number == 5:
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()
    name_product = driver.find_element(By.XPATH, "//*[@id='item_2_title_link']").text
    price_product = driver.find_element(By.XPATH,"//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div").text

elif product_number == 6:
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
    name_product = driver.find_element(By.XPATH, "//*[@id='item_3_title_link']").text
    price_product = driver.find_element(By.XPATH,"//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div").text

else:
    print('There is no such product')

if name_product and price_product:
    print(f"Product:{name_product} Price:{price_product} Added to Cart")

    #Открываем корзину
    driver.find_element(By.XPATH,"//*[@class='shopping_cart_link']").click()


    try:

        # Переменная, которая ищет продукт по имени на странице
        name_product_in_cart = driver.find_element(By.XPATH, f"//div[text()='{name_product}']").text

        # Переменная, которая ищет цену продукта на странице
        price_product_in_cart = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

        # Проверяем имя продукта в каталоге с именем продукта в корзине
        assert name_product == name_product_in_cart, 'Info Cart Product Not Correct'
        print('Info Cart Product Correct')

        # Проверяем цену продукта в каталоге с ценой продукта в корзине
        assert price_product == price_product_in_cart,'Info Cart Price Product Not Correct'
        print('Info Cart Price Product Correct')

    except NoSuchElementException:
        print('Product Not Find in Cart')

    # Подтверждаем продукты в корзине
    driver.find_element(By.XPATH, "//*[@id='checkout']").click()

    # Вводим фейковые данные в форму заполнения заказа
    driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys(fake.first_name())
    driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys(fake.last_name())
    driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys(fake.postalcode())

    # Подтверждаем форму заполнения
    driver.find_element(By.XPATH, "//*[@id='continue']").click()

    try:

        summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]").text

        # Переменная, которая ищет продукт по имени на странице
        name_product_in_order = driver.find_element(By.XPATH, f"//div[text()='{name_product}']").text

        # Переменная, которая ищет цену продукта на странице
        price_product_in_order = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

        # Проверяем имя продукта в каталоге с именем продукта в корзине
        assert name_product == name_product_in_order, 'Info Cart Product Not Correct'
        print('Info Order Product Correct')

        # Проверяем цену продукта в каталоге с ценой продукта в корзине
        assert price_product == price_product_in_order,'Info Cart Price Product Not Correct'
        print('Info Order Price Product Correct')

        price_product = float(price_product_in_order[1:])
        item_total = summary_price.split(": ")[-1]
        item_total = float(item_total[1:])

        assert price_product == item_total, 'Info Total Price Not Correct'
        print('Info Total Price Correct')

    except NoSuchElementException:
        print('Product Not Find in Order')

    #Нажимаем кнопку оформления
    driver.find_element(By.XPATH, "//*[@id='finish']").click()


    checkout_complete = driver.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")
    value_checkout_complete = checkout_complete.text

    # Проверяем текст успешного оформления заказа
    assert value_checkout_complete == 'Thank you for your order!', 'Order Failed!'
    print('Order Complete!')