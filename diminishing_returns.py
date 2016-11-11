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


counts=[]
tops = top_n(438)

fn = 'binary_arrays/' + str(tops[0]) + '.txt'
with open(fn, 'r') as bits:
	bits_string = BitArray(bin=bits.read())

iter = bits_string
counts.append(iter.count("1"))
print(iter)

for i in range(1, 437):

	# top_num = i
	# choose = i

	# regions_list = top_n(top_num)
	# regions_dict = {}
	fn = 'binary_arrays/' + str(tops[i]) + '.txt'

	with open(fn, 'r') as bits:
		bits_string = bits.read()
		bit_array = BitArray(bin=bits_string)
	
	iter = iter | bit_array
	print(i)
	counts.append(iter.count("1"))

	# combos = {}

	# for i in itertools.combinations(regions_list, choose):
	# 	print(choose)
	# 	#all_or = regions_dict[i[0]] | regions_dict[i[1]] | regions_dict[i[2]] | regions_dict[i[3]] | regions_dict[i[4]]
	# 	all_or = regions_dict[i[0]]
	# 	for j in range(1,choose):
	# 		all_or = all_or | regions_dict[i[j]]
	# 	combos["_".join(str(x) for x in list(i))] = all_or.count("1")

	# sorted_combos = sorted(combos.items(), key=operator.itemgetter(1),reverse=True)
	# sorted_combos = dict(sorted_combos)
	# print(list(sorted_combos.values())[0])
	# max_covered.append(list(sorted_combos.values())[0])

# plt.figure(figsize=(10, 5))
# plt.plot(max_covered)
# plt.savefig("warehouses.png")
csv = pd.DataFrame(index=range(437), columns=["cumulative_regions","coverage"])
csv["regions"] = tops
csv["coverage"] = counts
print(csv)
csv.to_csv("diminishing_returns.csv", sep=',')

plt.figure(figsize=(10, 5))
plt.plot(csv["coverage"])
plt.savefig("warehouses.png")




