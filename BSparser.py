from BeautifulSoup import BeautifulSoup
from datetime import datetime

def parseDocument(doc):
	return BeautifulSoup(doc)

def parseSoup(soup):
	"""returns table"""
	return soup.find("table")
		
def parseTR(tr):
	"""returns relevant data from a row"""
	keys = ['name', 'period']
	data = map(lambda t:t.text, tr.findAll("td"))
	#data[1]=datetime.strptime(data[1], "%m/%d/%Y").date()
	return dict(zip(keys, data[0:3:2])) # ignore date since this dict will join a value that has the very same date as the key

def parseTable(table):
	return map(parseTR, table.findAll("tr")[1:-1])

def getData(doc):
	return parseTable(parseSoup(parseDocument(doc)))
