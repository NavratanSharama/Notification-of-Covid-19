from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):      #To flash notification
    notification.notify(
        title = title,
        message = message,
        app_icon = "C://Users//hp//PycharmProjects//CoronaNotification//Coronavirus.ico",
        timeout = 5          #flashing timeout setting in seconds
    )

def fetchData(url):     #fetching data from website
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    while True:
        #notifyMe("Yash", "Lets stop the spread of this virus together.")
        myHtmlData = fetchData('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(myHtmlData, 'html.parser')   #parsing the data
        #print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()     #Converting the Parsed Data to a String
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")
        #print(itemList)
        states = ['Delhi', 'Maharashtra', 'Uttar Pradesh', 'Madhya Pradesh', 'Rajasthan']    # Enter Your State Name Here (Dont Enter More Than 5 States)
        for item in itemList[0:32]:
            dataList = item.split("\n")
            #print(dataList)
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of Covid-19'
                nText = f"State : {dataList[1]},\nConfirm-Cases : {dataList[2]}, \nCured : {dataList[3]}, \nDeaths : {dataList[4]} "
                notifyMe(nTitle, nText)
                time.sleep(5)
        time.sleep(86400)     #Loop For 1 Hour (1 hour = 3600 seconds)