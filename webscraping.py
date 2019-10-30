import requests
from bs4 import BeautifulSoup
import pandas as pd
#import csv
res=requests.get('https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2')
soup=BeautifulSoup(res.text,'lxml')
products=[]
prices=[]
ratings=[]
for link in soup.find_all('a',href=True,attrs={'class':'_31qSD5'}):
  name=link.find('div', attrs={'class':'_3wU53n'})
  price=link.find('div' ,attrs={'class':'_1vC4OE _2rQ-NK'})
  rating=link.find('div' ,attrs={'class':'hGSR34'})
  products.append(name.getText())
  prices.append(price.getText())
  ratings.append(rating.getText())
# print(products)
# print(prices)
# print(ratings)
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products2.csv',index=False)
