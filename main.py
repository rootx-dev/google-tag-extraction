import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.google.com/search?q="






outputList = []
with open("vorodi.txt" , encoding="utf8") as names:
    reader = csv.reader(names)
    for eachName in reader:
        furl = url + str(eachName)
        res = requests.get(furl)
        soup = BeautifulSoup(res.text, 'html.parser')
        print(str(res) + "fetched successfully for the word:" + str(eachName))
        MyList = soup.find_all(['span'], attrs={'dir': ['rtl']})
        MyList = MyList[len(MyList) - 8:]

        for each in MyList:
            outputList.append(each.text)

for eachtag in outputList:
    output1 = open("output.txt", "a" , encoding="utf8")
    output1.writelines(str(eachtag) + '\n')
    output1.close()


print('اتمام استخراج تگ ها')