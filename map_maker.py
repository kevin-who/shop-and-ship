import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bitstring import BitArray

with tf.Graph().as_default():
	with tf.Session() as sess:
		map_string = "484_561_459_322_64_158_41_315_384_437_192_510_504_534_308_334_487_128_207"
		region_ids = [int(x) for x in map_string.split("_")]
		print(region_ids)

		fn = 'binary_arrays/' + str(region_ids[0]) + '.txt'
		with open(fn, 'r') as bits:
			bits_string = bits.read()
			map_bin = BitArray(bin=bits_string)

		all_or = map_bin

		for i in region_ids:
			fn = 'binary_arrays/' + str(i) + '.txt'

			with open(fn, 'r') as bits:
				bits_string = bits.read()
				bit_array = BitArray(bin=bits_string)

			all_or = all_or | bit_array


		print(all_or.count("1"))

		bit_array = [int(x) for x in list(str(all_or.bin))]
		bit_array = np.array(bit_array)*255
		tensor = bit_array.astype(np.uint8)
		tensor = tf.reshape(tensor,[353,546,1])
		output_image = tf.image.encode_png(tensor)
		init_op = tf.initialize_all_variables()
		#save the output
		f = open("map_maker/" + "final_" + map_string + ".png", "wb+")
		f.write(output_image.eval())
		f.close()