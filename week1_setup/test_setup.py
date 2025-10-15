import pandas as pd
import matplotlib.pyplot as plt

data = {'week:': [1, 2, 3, 4], 'Progress':[10,30,50,70]}

df = pd.DataFrame(data)
print(df)

df.plot(x='week:', y='Progress', kind='line'
, marker='o', title='Learning progress')
plt.show()