from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from unidecode import unidecode
Url = "https://e118.ir/main/category/43"
                        # a/w
f = open("numbers.txt", "a")
driver = webdriver.Chrome()
driver.get(Url)

def start(newurl, newZ):
    z = newZ + 1
    matchUrl = newurl + "/" + str(z)
    driver.get(str(matchUrl))
    start_range = int(1)
    end_range = int(41)
    for x in range(start_range, end_range):
        print(str(x))
        # time.sleep(2)

        listView = driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div/div[1]/div[1]/div/div[1]/a[2]')
        listView.click()

        path_numberMobile ="/html/body/section[2]/div/div/div/div[1]/div[1]/ul/li["+ str(x) +"]/a/div[2]/ul/li[2]"
        numberMobile = driver.find_element(By.XPATH,path_numberMobile)
        
        path_numberPhone = "/html/body/section[2]/div/div/div/div[1]/div[1]/ul/li["+ str(x) +"]/a/div[2]/ul/li[1]"
        numberPhone = driver.find_element(By.XPATH,path_numberPhone)

        EnMobile = unidecode(numberMobile.text)
        EnPhone = unidecode(numberPhone.text)
        if EnMobile != " " or ' ' or "" or '' : 
            f.write(EnMobile + '\n')
        else : 
            f.write("")
        if EnPhone != " " or ' ' or "" or '' :
            f.write(EnPhone + '\n')
        else : 
            f.write("")
    start(Url, int(z))

    f.close()
    driver.close()

start(Url,1)