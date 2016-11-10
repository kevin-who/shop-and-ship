import numpy as np
from bitstring import BitArray

fn = 'binary_arrays/' + str(1) + '.txt'
with open(fn, 'r') as bits:
	bits_string = bits.read()

bits_string = BitArray(bin=bits_string)
print(bits_string)
