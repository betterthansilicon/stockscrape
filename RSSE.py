import requests
import json
from bs4 import BeautifulSoup

RBXIds = [
	245662005, # JAILBREAK
	383310974 # ADOPT ME
]

gameData = {}

for n in RBXIds:
	page = requests.get("https://games.rprxy.xyz/v1/games?universeIds="+str(n))
	soup = BeautifulSoup(page.content, "html.parser")
	pagetext = soup.text
	pagetext = pagetext.replace('{"data":[', "")
	pagetext = pagetext.replace(']}', "")
	pagetext = json.loads(pagetext)

	gameData[str(pagetext["id"])] = str(pagetext["playing"])
print(gameData)