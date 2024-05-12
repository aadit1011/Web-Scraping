from bs4 import BeautifulSoup;

with open('D:\\Python\\Beautiful_Soup\\index.html','r') as file:
     content=file.read();
     soup=BeautifulSoup(content,'lxml');
     paragraph_contents=soup.find_all('p');
     for items in paragraph_contents:
          print(items.text);