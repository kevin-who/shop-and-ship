import tensorflow as tf
import numpy as np

fn = 'rbg_arrays/1.txt'

with tf.Graph().as_default():
	length = 546
	width = 353
	image_contents = tf.read_file(fn)
	image = tf.image.decode_png(image_contents, channels=3)
	tensor = tf.convert_to_tensor(image)
	input = tf.reshape(tensor,[length*width*3])
	init_op = tf.initialize_all_variables()
	with tf.Session() as sess:
		sess.run(init_op)
		np.savetxt('png_maps/1.png', input.eval(), fmt='%d')
