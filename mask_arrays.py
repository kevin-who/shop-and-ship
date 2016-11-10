import tensorflow as tf
import numpy as np
import numpy.ma as ma
from PIL import Image

with tf.device('/gpu:0'):
	with tf.Graph().as_default():
		with tf.Session() as sess:
			for i in range(1,874):
				fn = 'rbg_arrays/' + str(i) + '.txt'
				print(i)
				raw = np.loadtxt(fn)
				mask = []
				for values in list(raw):
					if np.any(values==36):
						mask.append([255, 255, 255])
					else:
						mask.append([0, 0, 0])
				black_white = np.asarray(mask)
				tensor = black_white.astype(np.uint8)
				tensor = tf.reshape(tensor,[353,546,3])
				output_image = tf.image.encode_png(tensor)
				init_op = tf.initialize_all_variables()
				sess.run(init_op)
				#save the output
				f = open("filtered_pngs/" + str(i) + ".png", "wb+")
				f.write(output_image.eval())
				f.close()


