from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


contest_no=input("Enter the contest no.:")
dire = str(contest_no)
par_dir="./"

path=os.path.join(par_dir,dire)

os.mkdir(path)


PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://codeforces.com/problemset")

try:
    table_c = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "tbody"))
    )

    p=[]

    #here i will be storing all the questions
    #of the contest no. in the list p.
    #Please do not close the webdriver until
    #it closes itself
    
    while True:
        contests=table_c.find_elements_by_tag_name("tr")
        l2=len(contests)
        for i in contests:
            j=i.find_element_by_tag_name("a")
            l=len(j.text)
            s1=j.text[:l-1]
            s2=j.text[:l-2]
            if str(contest_no)==s1 or str(contest_no)==s2:
                p.append(j.text)
                if i==contests[l2-1] and j.text[l-1] != 'A':
                     below = WebDriverWait(driver, 10).until(
                     EC.presence_of_element_located((By.CLASS_NAME, "pagination"))
                     )
                     arrows=below.find_elements_by_tag_name("li")
                     y=len(arrows)
                     arrows[y-1].click()
                     table_c = WebDriverWait(driver, 10).until(
                     EC.presence_of_element_located((By.TAG_NAME, "tbody"))
                     )
            if i==contests[l2-1] and len(p)==0:
                below = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pagination"))
                )
                arrows=below.find_elements_by_tag_name("li")
                y=len(arrows)
                arrows[y-1].click()
                table_c = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "tbody"))
                )
        if len(p) != 0:
            x=p[len(p)-1]
            if x[len(x)-1] =='A':
                break


           
         
    driver.quit()        
    p.reverse()
    for i in p:
        k = len(i)
        let = i[k-1]
        if (let.isdigit()):
            let = i[k-2:]
        dire2=let
        par_dir2= "./" + str(contest_no) + "/"
        path2=os.path.join(par_dir2,dire2)
        os.mkdir(path2)
        webpage="https://codeforces.com/problemset/problem/" + str(contest_no) + "/" + let
        PATH="C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get(webpage)
        time.sleep(1)
        path3= "./" + str(contest_no) + "/" + let + "/"+ "problem.png"
        path4= "./" + str(contest_no) + "/" + let + "/"
        driver.save_screenshot(path3)
        main=driver.find_element_by_class_name("sample-test")
        inputs=main.find_elements_by_class_name("input")
        outputs=main.find_elements_by_class_name("output")
        u=len(inputs)
        t=1
        for j in range(0,u):
            in_put=inputs[j].find_element_by_tag_name("pre")
            z1=in_put.text
            out_put=outputs[j].find_element_by_tag_name("pre")
            z2=out_put.text
            file1=path4 + "input" + str(t) + ".txt"
            file2=path4 + "output" + str(t) + ".txt"
            f=open(file1,"w+")
            f.write(z1)
            f.close()
            f=open(file2,"w+")
            f.write(z2)
            f.close()
            t+=1
            
            
        driver.quit()
    
finally:
    print("done,the questions have been downloaded!")




