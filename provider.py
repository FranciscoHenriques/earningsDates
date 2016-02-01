from urllib2 import urlopen
from datetime import date, timedelta
import BSparser

def getDoc(date):
	"""d is a datetime.date object"""
	makeUrl=lambda d: "http://www.bloomberg.com/apps/ecal?date={}&strtpt=1&endpt=1000&c=US".format(d.strftime("%Y%m%d")) # assuming urlschema doesn't change and there's no more than 1000 US companies releasing earnings any given day
	return urlopen(makeUrl(date)).read()
	
def getData(date=date.today(), numDays=1):
	"""d is a datetime.date object"""
	data=dict()
	for n in range(numDays):
		d=date+timedelta(days=n)
		data[d] = BSparser.getData(getDoc(d))
	
	return data
	
#interface for client is:
#from provider import getData
#from pprint import pprint
#pprint(getData())
