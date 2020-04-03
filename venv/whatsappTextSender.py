from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

choice=True
while(choice):
    driver = webdriver.Chrome('C:/Users/Trupti/PycharmProjects/whatsapp/venv/drivers/chromedriver')
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 700)

    target_person_Name = str(input('Please enter the contact name person or group name that u want to send message'))

    string_message = str(input('Please enter your  desired message: '))

    number = int(input('Enter number of times you want your message to be sent: '))




    x_arg = '//span[contains(@title, ' + '"' + target_person_Name + '"' + ')]'
    print(x_arg)
    person_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    print(person_title)
    person_title.click()
    inp_xpath = '//div[@class="_3u328 copyable-text selectable-text"]'
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))

    for i in range(number):
        input_box.send_keys(string_message + Keys.ENTER)
        time.sleep(0.20)
    driver.__exit__()
    input_value= input("do you want to text some one else Y yes or N for no")
    if(input_value!="Y"):
        choice=False