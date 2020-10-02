from selenium import webdriver
import time


    
driver = webdriver.Firefox()
pageCount=1
comments=[]
commentCount=1
while pageCount<=50:
    newUrl="https://www.kitapyurdu.com/index.php?route=product/product/reviewAll&product_id=10233&page="+str(pageCount)
    driver.get(newUrl)
    commentAll=driver.find_elements_by_css_selector(".review-text")

    for comment in commentAll:
        comments.append(comment.text)
        
    time.sleep(5)
    pageCount+=1
    
with open("comment.csv","a",encoding = "UTF-8") as file:
    for comment in comments:
        file.write(comment + "\n")
        pageCount+=1
                           
driver.close()


