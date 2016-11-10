import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

region_counts = pd.read_csv("k_pixel_counts.csv")

bad_regions = list(np.loadtxt("bad_regions.txt"))

filtered_regions = region_counts[region_counts["region"].isin(bad_regions)==False]
print(filtered_regions)

plt.figure(figsize=(60, 30))
sns.distplot(filtered_regions["pixels"],bins=100, rug=False)
plt.savefig("real_histogram.png")

filtered_regions.to_csv("k_filtered_pixel_counts.csv", sep=',')