import requests
import numpy as np
import numpy.ma as ma
import pandas as pd

def pad(num):
	if len(str(num))<5:
		return "0" * (5-len(str(num))) + str(num)

zips = pd.read_csv("zip_codes.csv")["ZIP"]
for zip_code in zips:
	print(zip_code)
	url = "https://www.ups.com/maps/results?usmDateCalendar=11%2F10%2F2016&zip={0}&stype=O"
	url = url.format(pad(zip_code))
	request = requests.post(url)
	# print(request)
	# print(request.text)
