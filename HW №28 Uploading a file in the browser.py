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

base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)
driver.set_window_size(1920, 1080)

#Переменная с ссылкой файла на устройстве
path_upload = "C:\\Users\\songf\\Desktop\\EduIT\\BasicPython\\1\\Basic_Selenium_2\\screenshots\\screenshot2025.02.19-14.19.57.png"

#Нажимаем кнопку загрузки файла и выбираем файл по пути path_upload
click_button = driver.find_element(By.XPATH, "//input[@id='file']")
click_button.send_keys(path_upload)
print('File Upload')

#Получение ссылки загруженного файла на сайте
uploaded_file_name = driver.find_element(By.XPATH, "//input[@id='file']").get_attribute("value")

uploaded_file_name = uploaded_file_name.split("\\")[-1] #Вытаскиваем имя файла который загрузили, с помощью метода split,
#разбиваем ссылку на список слов, где двойной слэш как разделитель элементов списка и с помощью [-1] делаем срез до
#последнего элемента в списке, который и будет именем файла

file_name = path_upload.split("\\")[-1] #Вытаскиваем имя файла из ссылки на устройстве, с помощью метода split, разбиваем
#ссылку на список слов, где двойной слэш как разделитель элементов списка и с помощью [-1] делаем срез до последнего
#элемента в списке, который и будет именем файла

assert uploaded_file_name == file_name, 'File names dont match'
print('Files names match')
