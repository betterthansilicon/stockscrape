#!/usr/bin/env python
import requests
import json
from bs4 import BeautifulSoup

NASDAQStocks = [
	"AAPL",
	"ADBE",
	"ADSK",
	"AMD",
	"AMZN",
	"ATVI",
	"CMCSA",
	"COST",
	"CSCO",
	"DLTR",
	"DOCU",
	"EA",
	"EBAY",
	"FB",
	"FOX",
	"GOOGL",
	"INTC",
	"INTU",
	"KDP",
	"KHC",
	"MAR",
	"MSFT",
	"NFLX",
	"NVDA",
	"ORLY",
	"PEP",
	"PYPL",
	"QCOM",
	"ROST",
	"SBUX",
	"SIRI",
	"TMUS",
	"TSLA",
	"TXN",
	"ZM"
]

def scrape(URL):
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")

	txts = soup.find("div", class_="YMlKec fxKbKc")
	pricestr = str(txts.text)

	return pricestr

objNASDAQ = {}
for s in NASDAQStocks:
	objNASDAQ[s] = scrape("https://www.google.com/finance/quote/"+s+":NASDAQ")