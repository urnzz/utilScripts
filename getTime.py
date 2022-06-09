from bs4 import BeautifulSoup
import requests

url = 'https://www.calendardate.com/todays.htm'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser').text
b = str(soup).split('\n') 
c = []
for x in b:
    if 'YYYY-MM-DD' in x:
        c.append(x)
for x in c:
    date=x.split(':')[1].strip()
url = 'https://dateandtime.info/pt/city.php?id=3470451'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')
hour = str(soup.find('time').text).split('h')[0]+":"+str(soup.find('time').text).split('h')[1][0]+str(soup.find('time').text).split('h')[1][1]
print(date+' '+hour)
################

#url = 'https://www.google.com/search?q=time+date+{zo}%2F{ne}'.format(zo = 'america', ne = 'sao_paulo')
#page = requests.get(url).text
#soup = BeautifulSoup(page, 'html.parser')
#b = soup.find_all(class_="gsrt vk_bk FzvWSb YwPhnf")[0].text
#print(soup)
