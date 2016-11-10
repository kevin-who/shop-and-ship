import tensorflow as tf
import numpy as np
import numpy.ma as ma

fn = 'rbg_arrays/1.txt'


with tf.Graph().as_default():
	with tf.Session() as sess:
		sess.run(init_op)
		tensor = np.loadtxt(fn)
		mask = tensor[:] == [255, 209, 36]
		print(mask)
		print(tensor)
		tensor = ma.masked_equal(tensor, 255)
		tensor = tensor.astype(np.uint8)
		tensor = tf.reshape(tensor,[353,546,3])
		output_image = tf.image.encode_png(tensor)
		init_op = tf.initialize_all_variables()
			#save the output
			f = open("filtered_pngs/1.png", "wb+")
			f.write(output_image.eval())
			f.close()

