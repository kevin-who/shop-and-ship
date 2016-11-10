import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import os

bad_regions = list(np.loadtxt("bad_regions.txt"))
bad_regions = [int(x) for x in bad_regions]
print(bad_regions)

for i in bad_regions:
	os.remove("filtered_binary_arrays/" + str(i) + ".txt")