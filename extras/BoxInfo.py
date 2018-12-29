import requests
from bs4 import BeautifulSoup

r = requests.get("https://boardgamegeek.com/boardgame/1")
soup = BeautifulSoup(r.content, "html.parser")

#this link has the game name in it
address = soup.link.get('href')
address += "/versions"

print (address)

r = requests.get(address)
soup = BeautifulSoup(r.content, "html.parser")

versionInfo = soup.script
newInfo = str(versionInfo)

newInfo = newInfo.split("GEEK.geekitemPreload = ")[1].split("}};")[0]
gameEdition = newInfo.split("\"boardgameversion\":[")[1].split("]")[0]

gameEdition = eval("[" + gameEdition + "]")


for index in (gameEdition):
    print(gameEdition[index]["name"])


if "GEEK.geekitemPreload" in newInfo:
    print("exist")
else:
    print("doesn't exist")

#print (versionInfo)



