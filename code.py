# Python program to demonstrate
# selenium
from selenium.webdriver.chrome.options import Options 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import re
import os
from time import sleep
from selenium import webdriver
from discord_webhook import DiscordWebhook


def send_discord_notification(message):
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1101950163892838470/0F0QCt5iXRHpjQAERpiT_GsnN7Z_Vs3Tbl76rATtG8w7niw3VRvYWWjas2eHOyvq7P1d', content=message)
    webhook.execute()



email="xxxx@gmail.com"
Firstname="xxxx"
Lastname="xxxx"
address="xxxx"
phoneno="xxxxxxxxxxx"
city="xxx"
province="xxx"
zip="xxxx"
shoe="Shoe Size(UK) "
cardNum="xxxxxxxxxxxxxxxx"
card_holder_name="xxxx xxxxx"
card_date="xx/xx"
cvv1="xxx"
#cvv1="1234"
text_to_click = "New Arrivals"
#driver = webdriver.Firefox()

options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(1)
driver.get("https://www.superkicks.in/?utm_source=google&utm_medium=CPC&utm_campaign=DM_Search_Brand&gclid=CjwKCAjwuqiiBhBtEiwATgvixIdqweWAAP5u6xBLGugZKaVc6TAcTovg7mfyHNsfB9BsS_p97U0xHBoCVIUQAvD_BwE")
element1 = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='{text_to_click}']")))

element1.click()


sleep(2)

# elements = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT,"AIR MAX TW 'WHITE/BLACK'")))
# elements.click()

print("\n\n\n### Please select the pair ###")
print("\n\n\nThe bot is waiting for 60 seconnds so that you can select the pair\n\n\n")
sleep(60)



# # Split the input string into an array



elements = driver.find_elements(By.XPATH,'/html/body/main/section[1]/section/div[1]/div[2]/div/div[5]/div')


os.system('cls' if os.name == 'nt' else 'clear')

print("\nInput Instructions and example:\nEnter the sizes you want with spaces like '7 8 10',\nthen the bot will select size 7,8 and 10. \nNow select QUANTITY of each size like '3 1 5'.\nThe bot will select 3 pairs of size 7, 1 pair of size 8 and 5 pairs of size 10.\n\n")
input_string = input("Enter the Shoe sizes by space: ")
shoe_size  = [int(x) for x in input_string.split()]
input_string = input("Enter the quantity of shoe sizes by space: ")
Quantity = array = [int(x) for x in input_string.split()]


if len(elements)==0:
    print(len(elements))
else:
    print(elements[0].text)
    
    time_str = elements[0].text
    time_match = re.search(r'(\d+)d (\d+)h (\d+)m (\d+)s', time_str)
    days, hours, minutes, seconds = map(int, time_match.groups())
    total_seconds = days*24*60*60 + hours*60*60 + minutes*60 + seconds
    print("\nThe bot will continue working after: ",total_seconds,"seconds\n")
    sleep(total_seconds)



# /html/body/main/section[1]/section/div[1]/div[2]/div/div[5]/div
sleep(2)

for j in range(0,len(shoe_size)):

     label_element = driver.find_elements(By.XPATH, "//label[text()={}]".format(shoe_size[j]))
     if len(label_element)==0:
           print(len(label_element))
     else:
           driver.execute_script("arguments[0].click();", label_element[0]) 
           addtocart_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section[1]/section/div/div[2]/div/div[5]/product-form/form/div/button')))    
           driver.execute_script("arguments[0].click();", addtocart_btn)
           sleep(4)
           for i in range(0,(Quantity[j]-1)):
                 quantity_increment = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME,'plus')))
                 driver.execute_script("arguments[0].click();", quantity_increment)
                 sleep(1)
           if j!=len(shoe_size)-1:     
                try: 
                    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/cart-drawer/div/div[2]/div[1]/button')))
                    driver.execute_script("arguments[0].click();", element)
                except:
                     pass
              

addtocart_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section[1]/section/div/div[2]/div/div[5]/product-form/form/div/button')))    
driver.execute_script("arguments[0].click();", addtocart_btn)
message = 'Item has been added to cart!'
send_discord_notification(message)
# # Click on the label
#    driver.execute_script("arguments[0].click();", label_element)
#    sleep(2)
#    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section[1]/section/div/div[2]/div/div[5]/product-form/form/div/button')))    
#    driver.execute_script("arguments[0].click();", element)
#    sleep(3)
#    for i in range(0,(Quantity[j]-1)):
#             my_element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME,'plus')))
#             driver.execute_script("arguments[0].click();", my_element)
#    sleep(2)



#    button_element = driver.find_element(By.XPATH,"/html/body/cart-drawer/div/div[2]/div[1]/h2")
#    driver.execute_script("arguments[0].click();", button_element)
# label_element = driver.find_element(By.XPATH, "//label[text()={}]".format(shoe_size[len(shoe_size)-1]))


# # Click on the label
# driver.execute_script("arguments[0].click();", label_element)
   
# element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section[1]/section/div/div[2]/div/div[5]/product-form/form/div/button')))    
# driver.execute_script("arguments[0].click();", element)

# for i in range(0,(Quantity[len(shoe_size)-1]-1)):
#        my_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME,'plus')))
#        driver.execute_script("arguments[0].click();", my_element)



Checkout_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="CartDrawer-Checkout"]')))

driver.execute_script("arguments[0].click();", Checkout_button)
#  driver.execute_script("arguments[0].click();", but1)
try:
    cont = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/main/div[1]/form/div/button')))
    cont.click()
except:
    pass

email_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='checkout_email']")))
sleep(3)
email_box.send_keys(email)
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"checkout_shipping_address_country")))
inputElement.send_keys('India')
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"checkout_shipping_address_first_name")))
inputElement.send_keys(Firstname)
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"checkout_shipping_address_last_name")))
inputElement.send_keys(Lastname)
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"checkout_shipping_address_address1")))
inputElement.send_keys(address)
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"checkout_shipping_address_phone")))
inputElement.send_keys(phoneno)
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"checkout_shipping_address_city")))
inputElement.send_keys(city)
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"checkout_shipping_address_zip")))
inputElement.send_keys(zip)
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"checkout_shipping_address_province")))
inputElement.send_keys(province)
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"continue_button")))
inputElement.click()
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"continue_button")))
inputElement.click()
# but2=driver.find_elements_by_xpath("//*[contains(text(), 'Continue to shiping')]")
# driver.execute_script("arguments[0].click();", but2)
sleep(3)


inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"checkout_payment_gateway_85576745211")))
inputElement.click()
# switch back to the main content

inputElement= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"continue_button")))
inputElement.click()
sleep(15)

inputElement=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Skip')]")))
inputElement.click()
# driver.execute_script("arguments[0].click();", but1)
sleep(2)
but1=driver.find_elements(By.XPATH,"//*[contains(text(), 'Card')]")[0]
driver.execute_script("arguments[0].click();", but1)
sleep(3)
inputElement = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID,"CardNumber1")))
inputElement.send_keys(cardNum)
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"CardHolderName1")))
inputElement.send_keys(card_holder_name)
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"CardDate1")))
inputElement.send_keys(card_date)
inputElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"CVVFormatter1")))
inputElement.send_keys(cvv1)
payNow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[1]/div[3]/div[2]/div[2]/div/div/form/div[9]/div/button")))
payNow.click()
#/html/body/div[1]/main/div[1]/div[3]/div[2]/div[2]/div/div/form/div[9]/div/button
sleep(200)