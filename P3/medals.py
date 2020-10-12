
# 3) Write python code that loads any dataset (example Game_medal.csv), and plot the graph.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('india_olympic.csv')
#print(df)

df[['Gold','Silver','Bronze']].plot(kind='bar',stacked=True)
plt.title('India Olympics Medal')
plt.xlabel('Years')
plt.ylabel('Medals')
n = len(df['Games'])
labels = df.Games.str.slice(0,4)
plt.xticks(np.arange(n),labels,rotation='horizontal')
plt.show()
