import numpy as np
from bitstring import BitArray
import itertools
import pandas as pd
import operator
import math
import functools
import seaborn as sns
import matplotlib.pyplot as plt


max_covered = []


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

for i in range(1, 150):

	top_num = i
	choose = i

	regions_list = top_n(top_num)
	regions_dict = {}
	for i in regions_list:
		fn = 'binary_arrays/' + str(i) + '.txt'
		with open(fn, 'r') as bits:
			bits_string = bits.read()
		regions_dict[i] = BitArray(bin=bits_string)

	combos = {}

	iter = 1

	for i in itertools.combinations(regions_list, choose):
		print(str(iter) + " / " + str(math.factorial(top_num)/math.factorial(top_num-choose)/math.factorial(choose)))
		#all_or = regions_dict[i[0]] | regions_dict[i[1]] | regions_dict[i[2]] | regions_dict[i[3]] | regions_dict[i[4]]
		all_or = regions_dict[i[0]]
		for j in range(1,choose):
			all_or = all_or | regions_dict[i[j]]
		combos["_".join(str(x) for x in list(i))] = all_or.count("1")
		iter = iter + 1

	sorted_combos = sorted(combos.items(), key=operator.itemgetter(1),reverse=True)
	sorted_combos = dict(sorted_combos)
	print(list(sorted_combos.values())[0])
	max_covered.append(list(sorted_combos.values())[0])

plt.figure(figsize=(10, 5))
plt.plot(max_covered)
plt.savefig("warehouses.png")

