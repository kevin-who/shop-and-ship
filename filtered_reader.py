import tensorflow as tf
import numpy as np

with tf.Graph().as_default():
	with tf.Session() as sess:
		for i in range(1,874):
			print(i)
			fn = 'filtered_pngs/' + str(i) + '.png'
			image_contents = tf.read_file(fn)
			image = tf.image.decode_png(image_contents, channels=1)
			tensor = tf.convert_to_tensor(image)
			init_op = tf.initialize_all_variables()
			sess.run(init_op)
			np.savetxt('filtered_arrays/' + str(i) + '.txt', tensor.eval(), fmt='%d')