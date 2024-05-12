from bs4 import BeautifulSoup;

with open('D:\\Python\\Beautiful_Soup\\index.html','r') as file:
          content=file.read();
          
          soup=BeautifulSoup(content,'lxml');
          #Using find it only finds the first element from the file 
          h_tags=soup.find('h1');
          for items in h_tags: 
               print(items.text);
          only_h5=soup.find_all('h5');
          for items in only_h5:
               print(items.text);
          
          