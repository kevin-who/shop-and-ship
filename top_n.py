import numpy as np
import math
import pandas as pd

n = 10

pixel_counts = pd.read_csv("k_filtered_pixel_counts.csv")
pixel_counts = pixel_counts.sort_values("pixels",axis=0,ascending=False)
print(list(pixel_counts["pixels"])[:n])