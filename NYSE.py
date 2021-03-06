import requests
import json
from bs4 import BeautifulSoup

NYSEStocks = [
	"AA", 
	"ACRE",  
	"AMC", 
	"AMWL",  
	"BA", 
	"BABA",
 	"BAC",
 	"BB", 
 	"BKR",
 	"BMY",
 	"BORR",
 	"BP",
 	"C",
 	"CCIV",
 	"CCJ",
 	"CCL",
 	"CHPT",
 	"CIG",
 	"CLDR",
 	"CLF",
 	"CNP",
 	"COP",
 	"COTY",
 	"CPG",
 	"CPNG",
 	"CRM",
 	"CVE",
 	"CVX",
 	"CX",
 	"CYH",
 	"DAL",
 	"DDD",
 	"DIS",
 	"DM",
 	"DOW",
 	"DS",
 	"DVN",
 	"EDU",
 	"ENZ",
 	"EOG",
 	"EPD",
	"EQR",
	"ESGC",
	"ET",
	"EXK",
	"EXPR",
	"F",
	"FCX",
	"FINV",
	"FSR",
	"FTI",
	"FUBO",
	"GE",
	"GFI"
	"GGB",
	"GM",
	"GME",
	"GMRE",
	"GOLD",
	"GPS",
	"GSK",
	"GTT",
	"HAL",
	"HEXO",
	"HL",
	"HPE",
	"HPQ",
	"IAG",
	"IMAX",
	"INFY",
	"ING",
	"ITUB",
	"IVR",
	"JBL",
	"JE",
	"JILL",
	"JMIA",
	"JNJ",
	"JNPR",
	"JPM",
	"JWN",
	"KEY",
	"KGC",
	"KMI",
	"KO",
	"KODK",
	"KOS",
	"KR",
	"LC",
	"LLY",
	"LUMN",
	"LUV",
	"LVS",
	"LYG",
	"M",
	"MAC",
	"MBT",
	"MET",
	"MGM",
	"MO",
	"MOS",
	"MPC",
	"MRK",
	"MRO",
	"MS",
	"MT",
	"MUFG",
	"MUR",
	"MUX",
	"NCLH",
	"NEE",
	"NEM",
	"NFH",
	"NGL",
	"NIO",
	"NKE",
	"NLY",
	"NOK",
	"PCG",
	"PFE",
	"PG",
	"PINS",
	"PLTR",
	"PRTY",
	"QD",
	"QEP",
	"QS",
	"RBLX",
	"RCL",
	"RIG",
	"RKT",
	"RTX",
	"SAN",
	"SAVE",
	"SBSW",
	"SCHW",
	"SE",
	"SNAP",
	"SPCE",
	"SQ",
	"STPK",
	"SU",
	"SWN",
	"T",
	"TECK",
	"TEVA",
	"TFC",
	"TWTR",
	"U",
	"UAA",
	"UBER",
	"UMC",
	"UNH",
	"UNP",
	"USB",
	"V",
	"VALE",
	"VIPS",
	"VST",
	"VVR",
	"VZ",
	"WFC",
	"WMB",
	"WMT",
	"WTI",
	"X",
	"XL",
 ]

def scrape(URL):
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")

	txts = soup.find("div", class_="YMlKec fxKbKc")
	pricestr = str(txts)

	pricestr = pricestr.replace("<div class=\"YMlKec fxKbKc\">$", "")
	pricestr = pricestr.replace("</div>", "")

	return pricestr

objNYSE = {}
for s in NYSEStocks:
	objNYSE[s] = scrape("https://www.google.com/finance/quote/"+s+":NYSE")
objNYSE["BTC"] = scrape("https://www.google.com/finance/quote/BTC-USD")