import tensorflow as tf
import numpy as np

fn = 'rbg_arrays/1.txt'

with tf.Graph().as_default():
	tensor = np.loadtxt(fn)
	tensor = tf.reshape(tensor,[546,353,3])
	output_image = tf.image.encode_png(tensor)
	init_op = tf.initialize_all_variables()
	with tf.Session() as sess:
		sess.run(init_op)
		#save the output
		f = open("outputs/rubiks_output.png", "wb+")
		f.write(output_image.eval())
		f.close()

