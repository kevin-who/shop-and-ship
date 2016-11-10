import numpy as np
import math
import pandas as pd

regions1 = list(set(pd.read_csv("regions_codes/part1.csv")["region"]))
regions2 = list(set(pd.read_csv("regions_codes/part2.csv")["region"]))
regions3 = list(set(pd.read_csv("regions_codes/part3.csv")["region"]))
regions4 = list(set(pd.read_csv("regions_codes/part4.csv")["region"]))
regions5 = list(set(pd.read_csv("regions_codes/part5.csv")["region"]))

unique_regions = list(set(regions1+regions2+regions3+regions4+regions5))

unique_regions = [x[4:8] for x in unique_regions]


def pad(num):
	if len(str(num))<4:
		return "0" * (4-len(str(num))) + str(num)

bad_regions = []

for region_id in range(1,874):
	if pad(region_id) not in unique_regions:
		bad_regions.append(region_id)

print(len(bad_regions))