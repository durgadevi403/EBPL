

import pandas as pd

import matplotlib.pyplot as plt



# Load the CSV file

df = pd.read_csv("Historical_Tornado_Tracks.csv")



# Bar Chart: Number of Tornadoes per Year

plt.figure(figsize=(10, 5))

df['YR'].value_counts().sort_index().plot(kind='bar', color='red')

plt.title('Number of Tornadoes per Year')

plt.xlabel('Year')

plt.ylabel('Number of Tornadoes')

plt.tight_layout()

plt.savefig('bar_chart.png')

plt.close()



# Scatter Plot: Length vs Width of Tornadoes

plt.figure(figsize=(8, 5))

plt.scatter(df['LEN'], df['WID'], alpha=0.3)

plt.title('Tornado Path Length vs Width')

plt.xlabel('Length (miles)')

plt.ylabel('Width (yards)')

plt.tight_layout()

plt.savefig('scatter_plot.png')

plt.close()




