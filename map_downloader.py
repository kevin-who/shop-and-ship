import csv
from csv import DictReader
import urllib
from urllib.request import urlretrieve

def pad(num):
	if len(str(num))<4:
		return "0" * (4-len(str(num))) + str(num)

for region_id in range(1,874):
	
	url = "https://www.ups.com/using/services/servicemaps/maps25/map_{0}.gif"
	url = url.format(pad(region_id))
	urllib.request.urlretrieve(url, "maps/" + str(region_id) + ".gif")
	print(str(region_id) + " of " + str(873))