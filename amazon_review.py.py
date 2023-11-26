from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
import time

mail_url = 'https://www.amazon.com/'
SERACH_KEY = "smartphone"
MAX_PRICE = 1500 # usd


driver = webdriver.Chrome()
driver.get(mail_url)
driver.maximize_window()
time.sleep(3)

try:
    driver.find_element(By.XPATH,'/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[2]/div/div[2]').click()
    time.sleep(1)
except:
    pass


# search for smartphone
search = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search.send_keys(SERACH_KEY)
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()
time.sleep(2)




# max price filter
max_price_input = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul/span[8]/li/span/form/input[8]')
max_price_input.send_keys(MAX_PRICE)
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul/span[8]/li/span/form/span[3]/span/input').click()
time.sleep(2)



# click on item
i = 1
while True:

    search_result_url = driver.current_url

    product_div = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div')
    product_div_a = product_div.find_elements(By.XPATH,"//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
    product_urls = [a.get_attribute('href') for a in product_div_a]
    
    

    for link in product_urls: 
        try:
            driver.get(link)
            time.sleep(2)

            driver.execute_script(f"window.scrollTo(0,{1000});")

            title = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[10]/div[5]/div[4]/div[1]/div/h1/span').text.strip()
            item_discription  = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[10]/div[5]/div[4]/div[42]/div').text.strip()
            print(title)

            print(item_discription)

            print("\n")

            
        except Exception as e:
            print(str(e))
            pass

        # driver.get(search_result_url)
        # time.sleep(2)

