
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://crypto.com/price'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url,headers=headers)
webpage= urlopen(req).read()
soup  = BeautifulSoup(webpage,'html.parser')
print(soup.title.text)

tables=soup.findAll('table')
crypto_table=tables[0]
tr=crypto_table.findAll('tr')



all_names=soup.findAll("p", {"class":{'chakra-text css-rkws3'}})
all_symbols=soup.findAll("span",{"class":{'chakra-text css-1jj7b1a'}})
all_prices=soup.findAll("p",{"class":{'chakra-text css-5a8n3t'}})
all_changes=soup.findAll("p",{"class":{"chakra-text css-1okxd"}})

should_sell=False
print("Top 5 Cryptos")
for i in range(0,5):
    print("-------------------------------------------------")
    print('#',i+1,sep='')
    print('Name:',all_names[i].text)
    print('Symbol:',all_symbols[i].text)
    print('Price:',all_prices[i].text)
    print('Change in Last 24 Hours:',all_changes[i].text)
    if all_names[i].text=='Ethereum':
        if float(all_prices[i].text.replace('$','').replace(',',''))>2000:
            should_sell=True

if should_sell==True:
    print('')
    print("Ethereum is over $2000 and you should sell!")