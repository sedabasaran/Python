import urllib.request

url1 ='https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2019/07/python-library-1.jpg'
url2 ='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQNnDA9P7jkuoyBYoj3cN2svlH6G8yUBc3vqkhyzvYAyFCuMckH'

urlliste = [url1,url2] 
say = 1 
for url in urlliste:
    urllib.request.urlretrieve(url,'Resim'+str(say) + 'jpg')
    say +=1
    
