import time
import requests
import json

apiKey = 'bad4b5cf6b02470691c9b5da42ab9ca8'


folderPath = 'C:/Users/Ryan/CS361/pipe.txt'
while True:
    with open(folderPath, "r") as file:
        queryType = file.readline()
        query = file.readline()
    if len(queryType) != 0 :
       
        break 

    time.sleep(1)


with open(folderPath, "w") as f:
    f.truncate(0)

def writeToFile(content):
    with open(folderPath, "w") as file:
        file.write(content)

def popByLang(lang):
    
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'language': lang, 
        'apiKey': apiKey
    }


    response = requests.get(url, params=params)
    data = response.json()
   
    article = data['articles'][0]
    print("Popular article in " + lang +  " : "+ article['title'])
     #writeToFile(article['title'])

def popByCat(cat):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',
        'category': cat,
        'sortBy': 'popularity',
        'apiKey': apiKey
    }

    response = requests.get(url, params=params)
    data = response.json()
    article = data['articles'][0]
    print("article title: " + article['title'])
    #writeToFile(article['title'])

    

    
if queryType.strip() == 'lang':
    popByLang(query)
elif queryType.strip() == 'cat':
    popByCat(query)
else:
    print("Could not distinguish query")
    print(queryType)
