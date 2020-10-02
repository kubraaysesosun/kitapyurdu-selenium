from selenium import webdriver
import time


driver=webdriver.Firefox()
url="https://www.idefix.com/Kitap/Sineklerin-Tanrisi/Edebiyat/Roman/Dunya-Roman/urunno=0000000107800"

driver.get(url)
time.sleep(2)

commentAll=[]
allComment=driver.find_element_by_xpath("//*[@id='showAllComments']").click()
time.sleep(2)

comments=driver.find_elements_by_css_selector(".comment-content")
for comment in comments:
    commentAll.append(comment.text)

with open("comments.txt", "a", encoding = "UTF-8") as file:
    file.write("İDEFİX-COMMENTS")
    for comment in commentAll:
        file.write(comment+"\n")

driver.close()
