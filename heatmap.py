import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

full_health_data = pd.read_csv("cancerhackathon.csv", header=0, sep=",")
correlation_full_health = full_health_data.corr()

axis_corr = sns.heatmap(
correlation_full_health,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(50, 900, n=900),
square=True
)
plt.show()