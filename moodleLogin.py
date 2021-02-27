from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

user_name=input("Enter your username:")
password=input("Enter your password:")

PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://moodle.iitd.ac.in/login/index.php")

try:
    user = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    user.send_keys(user_name)
    passw = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    passw.send_keys(password)
    login_d = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login"))
    )
    l=login_d.text.split("\n")
    s=l[3]
    l2=s.split()
   # print(l2)
    captcha=""
    if len(l2) == 6:
        if l2[1]=="add":
            num1=int(l2[2])
            num2=int(l2[4])
            ans = num1 + num2
            captcha=str(ans)
        else:
            num1=int(l2[2])
            num2=int(l2[4])
            ans = num1 - num2
            captcha=str(ans)
    else:
        if l2[2]=='first':
            captcha=l2[4]
        else:
            captcha=l2[6]
   # print(captcha)
    cap = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "valuepkg3"))
    )
    cap.clear()
    cap.send_keys(captcha)

    log_in = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loginbtn"))
    )

    log_in.click()
    
        
    #print(s)
    #captcha=login_d.find_element_by_id("valuepkg3")
    #print(captcha)
    
finally:
    print("done")

#user=driver.find_element_by_id("username")
#user.send_keys(user_name)

#passw=driver.find_element_by_id("password")
#passw.send_keys(password)


