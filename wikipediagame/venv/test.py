import wikipedia
import time

#print (wikipedia.page("Battlestar_Galactica"))
#minpage=wikipedia.page("https://en.wikipedia.org/wiki/Abhishek Bachchan")
print(wikipedia.page("Comedy film").links.__contains__("21 Jump Street (film)"))
print(wikipedia.search("Salmaan Khan",results=1))
#for p in wikipedia.page("https://en.wikipedia.org/wiki/Aamir Khan",auto_suggest=True).links:
testinglink="15th National Film Awards"
pages=wikipedia.page(testinglink)
print(type(pages))
a=pages.links
print(a)
article={ str(wikipedia.page("Abhishek Bachchan").title):wikipedia.page("Salman Khan").links}
print(article)
#print(a)
#rint(article["Amitabh Bachchan"].links.__contains__("Abhishek Bachchan"))

for test in a:
       print(test)
       article[wikipedia.page(test).title]=wikipedia.page(test).links

       if wikipedia.page(test).links.__contains__("Abhishek Bachchan"):

           print("hello")
           break


print("Abhishek Bachchan" in article.values())
#pas=wikipedia.search("https://en.wikipedia.org/wiki/COBOL")
#print(minpage.links)
