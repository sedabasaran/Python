import requests
from bs4 import BeautifulSoup
toplamfilm = 0
for sayfaNo in range(1,6):

    url = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"+ str(sayfaNo) 
    r = requests.get(url)
   
    soup = BeautifulSoup(r.content,"lxml")
    filmler = soup.find_all("div",attrs={"class":"lister-item-content"})
    for film in filmler:
        filmadı = film.find("h3",attrs={"class":"lister-item-header"}).text
        toplamfilm +=1
        print(filmadı)
        print("*"*40)
        
print("Toplam {} kadar film bulundu.".format(toplamfilm))        
           
