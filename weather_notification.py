import requests 
from bs4 import BeautifulSoup 
from plyer import notification
import time

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

# define a function 
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://weather.com/weather/today/l/77b8c0df98d948950f263b82be3a74d879939795a16d55f596a074024b9fd802") 

soup = BeautifulSoup(htmldata, 'html.parser') 
#soup=soup.prettify()

current_temp = soup.find_all("span", class_= "CurrentConditions--tempValue--MHmYY") 
temp = str(current_temp)
#print(temp)
a=temp.find('>')
b=temp.find('<span class="CurrentConditions--degr')
#print(temp[(a+1):(b)])
temp=(str(temp[(a+1):b]))

#print(temp)
for x in soup.find_all("div",attrs={ "class":"Column--precip--3JCDO" , "data-testid":"SegmentPrecipPercentage" }):
    chances_rain=x.find('span',class_='Column--precip--3JCDO')
temp_rain=str(chances_rain)
#print(chances_rain)
#print(temp_rain)
a=temp_rain.find('%')
#print(temp_rain[(a-2):a])

#print(chances_rain)

temp_rain = str(chances_rain) 

#print(chances_rain)

result = "current_temp " + temp + " Farenheit "+"  in Rewari" + "\n" + temp_rain[(a-2):a]+ "% " + "chance of rain"

if __name__ == "__main__":
    title = "Weather Notification"
    message = result
    send_notification(title, message)
    time.sleep(10)