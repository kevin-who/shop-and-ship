import numpy as np
import numpy.ma as ma
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pixel_counts = pd.read_csv("k_pixel_counts.csv")
percentiles = []

for i in range(1,1001):
	percentiles.append(np.percentile(pixel_counts["pixels"],i/10))

print(percentiles)

plt.figure(figsize=(10, 20))
plt.plot(percentiles)
plt.savefig("ojive.png")