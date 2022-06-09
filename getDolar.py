from bs4 import BeautifulSoup
import requests

url = 'https://dolarhoje.com'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser').text
lines = soup.split('\n')
lf = ''
for x in lines:
    if 'R$' in x:
        lf += x
st = lf.split('um dólar')[1]
print('R$ '+st[5]+st[6]+st[7]+st[8])
