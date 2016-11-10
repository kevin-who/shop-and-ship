import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

pixel_counts = pd.read_csv("k_pixel_counts.csv")
plt.figure(figsize=(60, 30))
sns.distplot(pixel_counts["pixels"],bins=100, rug=False)
plt.savefig("histogram.png")