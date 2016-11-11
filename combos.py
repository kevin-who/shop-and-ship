import numpy as np
from bitstring import BitArray
import itertools

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

for i in itertools.combinations([1,2,3,4,5,6], 4):
	print(list(i))
