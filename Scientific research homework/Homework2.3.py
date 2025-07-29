import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("flights").pivot_table(index="month", columns="year", values="passengers", observed=True)
plt.figure(figsize=(10, 6))
heatmap = sns.heatmap(df, annot=True, fmt=".0f", cmap="coolwarm", linewidths=0.5)

plt.title("Number of Airline Passengers (1949-1960)")
plt.xlabel("Year")
plt.ylabel("Month")

plt.colorbar(heatmap.collections[0])
plt.show()

