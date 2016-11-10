import numpy as np
import numpy.ma as ma

pixel_counts = {}

for i in range(1,874):
	print(i)
	fn = 'filtered_arrays/' + str(i) + '.txt'
	map_matrix = np.loadtxt(fn)
	map_matrix = [list(x) for x in map_matrix]
	count = sum(x.count(255) for x in map_matrix)
	pixel_counts[str(i)] = count
