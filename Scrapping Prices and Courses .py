from bs4 import BeautifulSoup;

with open('D:\\Python\\Beautiful_Soup\\index.html', 'r') as file:
          content=file.read();
          soup=BeautifulSoup(content,'lxml');
          content_course=soup.find_all('span');
          print("The course contents in this site are=");
          for items in content_course:
               print(items.text);
          course_price=soup.find_all('button');
          print('And their respective prices are=')
          for items in course_price:
               print(items.text);
          
