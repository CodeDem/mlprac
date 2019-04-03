import pandas as pd
import numpy as np
a = np.array([['apple','pie'],['apple','juice'],['orange','pie'],['strawberry','cream'],['strawberry','candy']])

df = pd.DataFrame(a)
# Find the frequency of first word and divide by the total number of rows
df['probability1']=df[0].map(df[0].value_counts())/df.shape[0]
# Divide 1 by the total repetion 
df['probability2']=1/(df[0].map(df[0].value_counts()))
# Multiply the probabilities 
df['probability1 * probability2']= df['probability1']*df['probability2']
print(df)
df = pd.DataFrame(a)
df['probability1']=((df[0].map(df[0].value_counts())/df.shape[0]) * (1/(df[0].map(df[0].value_counts()))))