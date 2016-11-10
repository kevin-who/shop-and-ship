import tensorflow as tf
import numpy as np



with tf.Graph().as_default():
	with tf.Session() as sess:
		for i in range(1,874):
			print(i)
			length = 546
			width = 353
			fn = 'png_maps/' + str(i) + '.png'
			image_contents = tf.read_file(fn)
			image = tf.image.decode_png(image_contents, channels=3)
			tensor = tf.convert_to_tensor(image)
			input = tf.reshape(tensor,[length*width,3])
			init_op = tf.initialize_all_variables()
			sess.run(init_op)
			np.savetxt('rbg_arrays/' + str(i) + '.txt', input.eval(), fmt='%d')
