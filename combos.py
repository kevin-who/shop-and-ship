import numpy as np
from bitstring import BitArray

fn = 'binary_arrays/' + str(437) + '.txt'
with open(fn, 'r') as bits:
	bits_string = bits.read()

bits_string1 = BitArray(bin=bits_string)

fn = 'binary_arrays/' + str(322) + '.txt'
with open(fn, 'r') as bits:
	bits_string = bits.read()

bits_string2 = BitArray(bin=bits_string)

combo = bits_string1 | bits_string2

print(combo.count("1"))
