import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bitstring import BitArray


map_string = "484_241_431_442_109_561_519_390_346_216_209_444_322_506_168"
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

bit_array = [int(x) for x in list(str(all_or.bin))]
print(bit_array)