import numpy as np
import numpy.ma as ma
import csv

pixel_counts = []

for i in range(1,874):
	print(i)
	fn = 'filtered_arrays/' + str(i) + '.txt'
	map_matrix = np.loadtxt(fn)
	map_matrix = [list(x) for x in map_matrix]
	count = sum(x.count(255) for x in map_matrix)
	pixel_counts.append(count)

with open('k_pixel_counts.csv', 'w') as f:
	w = csv.DictWriter(f,["region","pixels"])
	w.writeheader()
	for i in range(0,873):
		w.writerow({"region":i+1,"pixels":pixel_counts[i]})