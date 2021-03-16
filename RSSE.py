import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver

path = r"/Users/leandroajo/Desktop/chromedriver"
option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(path, options=option)

page = driver.get("https://www.roblox.com/games#/")
soup = BeautifulSoup(driver.page_source, "html.parser")
games = soup.find_all("div", class_="game-card-container")

gameData = {}

for links in games:
	apipage = requests.get("https://games.rprxy.xyz/v1/games?universeIds="+links.find("a")["id"])
	jsonPage = BeautifulSoup(apipage.content, "html.parser")

	jsonPage = str(jsonPage)
	jsonPage = jsonPage.replace('{"data":[', "")
	jsonPage = jsonPage.replace(']}', "")

	jsonPage = json.loads(jsonPage)

	gameid = jsonPage["id"]
	playing = jsonPage["playing"]

	gameData[name] = playing