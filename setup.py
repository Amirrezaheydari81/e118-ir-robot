from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from unidecode import unidecode
print("Please Link Category in e118.ir")
input_url = input()
print("Please Name File Save")
file_name_input = input()
print("Please Number Page Crawel")
z_number = input()
Url = str(input_url)
                        # a/w
f = open(str(file_name_input), "a")
driver = webdriver.Chrome()
driver.get(Url)

def start(newurl, newZ):
    z = newZ + 1
    if( z <= int(z_number)):
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

    else:
        f.close()
        driver.close()
        print("End Work Crawel And Save Numbers File")
              
        print("File name : " + str(file_name_input) )

start(Url,1)