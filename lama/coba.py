import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("9.csv")
df = pd.DataFrame(data)

# for i in range(1):
#     name = "X_SMA_" + str(i)
#     df[name] = df.iloc[:,0].rolling(window=i).mean()

df['X_SMA_1'] = df.iloc[:,0].rolling(window=1).mean()

plt.figure()

# for i in range(1):
#     name = "X_SMA_" + str(i)
#     plt.plot(df[name],label=name)

plt.plot(df['X_SMA_1'],label='X_SMA_1')
plt.legend(loc=1)
plt.show()
