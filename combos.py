import numpy as np
from bitstring import BitArray
import itertools
import pandas as pd
import operator
import math
import functools
import seaborn as sns
import matplotlib.pyplot as plt
import random
import csv


def top_n(n):
	pixel_counts = pd.read_csv("k_filtered_pixel_counts.csv")
	pixel_counts = pixel_counts.sort_values("pixels",axis=0,ascending=False)
	return list(pixel_counts["region"])[:n]


# fn = 'binary_arrays/' + str(437) + '.txt'
# with open(fn, 'r') as bits:
# 	bits_string = bits.read()

# bits_string1 = BitArray(bin=bits_string)

# fn = 'binary_arrays/' + str(322) + '.txt'
# with open(fn, 'r') as bits:
# 	bits_string = bits.read()

# bits_string2 = BitArray(bin=bits_string)

# combo = bits_string1 | bits_string2

# print(combo.count("1"))



top_num = 100
sample_n = 10000
choose = 10
regions_list = top_n(top_num)
regions_dict = {}
random_samples = []
for i in regions_list:
	fn = 'binary_arrays/' + str(i) + '.txt'
	with open(fn, 'r') as bits:
		bits_string = bits.read()
	regions_dict[i] = BitArray(bin=bits_string)

combos = {}

iter = 1

for i in range(sample_n+1):
	random_samples.append(random.sample(regions_list, choose))

for i in random_samples:
	print(str(iter) + " / " + str(sample_n))
	#all_or = regions_dict[i[0]] | regions_dict[i[1]] | regions_dict[i[2]] | regions_dict[i[3]] | regions_dict[i[4]]
	all_or = regions_dict[i[0]]
	for j in range(1,choose):
		all_or = all_or | regions_dict[i[j]]
	combos["_".join(str(x) for x in list(i))] = all_or.count("1")
	iter = iter + 1

sorted_combos = sorted(combos.items(), key=operator.itemgetter(1),reverse=True)
# print(dict(sorted_combos))

csv = pd.DataFrame(index=range(sample_n+1), columns=["regions","coverage"])
csv["regions"] = list(dict(sorted_combos).keys())
csv["coverage"] = list(dict(sorted_combos).values())
# print(csv)
plt.figure(figsize=(10, 5))
sns.distplot(csv["coverage"],bins=100, rug=False)
plt.savefig("coverage_figures/t" + str(top_num) + "c" + str(choose) + "n" + str(sample_n) + ".png")
csv.to_csv("coverage_data/t" + str(top_num) + "c" + str(choose) + "n" + str(sample_n) + ".csv", sep=',')

