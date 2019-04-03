import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()

df['color'] = ['Red','Green','Yellow','Black','Orange']
df['count'] = [5,8,6,2,9]

df['pmf'] = df['count']/df['count'].sum()

print(df['pmf'])

plt.bar(df['color'],df['pmf'])
plt.show()