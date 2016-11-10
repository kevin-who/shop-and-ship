import numpy as np

for i in range(1, 874):
	print(i)
	fn = 'filtered_arrays/' + str(i) + '.txt'
	raw = np.loadtxt(fn)
	raw = raw/255
	raw = raw.reshape([353*546])
	raw = raw.astype(np.uint8)
	binary_string = "".join(str(x) for x in list(raw))
	f = open('binary_arrays/' + str(i) + '.txt', 'w+')
	f.write(binary_string)