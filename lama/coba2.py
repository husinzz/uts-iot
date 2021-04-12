import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter,filtfilt

data = pd.read_csv("9.csv")
df = pd.DataFrame(data)

def sampleWindow(num):
    for i in range(1, num+1):
        name = "X_Unfiltred" + str(i) # Melakukan increment pada nama dan window
        df[name] = df.iloc[:,0].rolling(window=i).mean() # Mencari sample window
        plt.plot(df[name],label=name) # Untuk mengambar
  

fs = 1000
x = np.arange(fs)
nyq = 0.5 * fs
cut_off = 5
order = 2

def lowpass_filter(data, cut_off, fs, order):
    normal_cutoff = cut_off/nyq
    b, a = butter(order,normal_cutoff, btype = "low")
    y = filtfilt(b, a, data)
    return y

def plotGambar():
    unfiltredDf = df.iloc[:,0].rolling(window=1).mean()
    plt.plot(unfiltredDf,label='X_Unfiltred')

    filtredDf = lowpass_filter(unfiltredDf, cut_off, fs, order)
    plt.plot(filtredDf, label='X_Filtred')




plotGambar() # Menggambar plot MVA dan LPF
# sampleWindow(3) # Untuk melakukan sampling windows

plt.legend();
plt.show()

# MVA : https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# MVA : https://www.datacamp.com/community/tutorials/moving-averages-in-pandas
# LPF : https://medium.com/analytics-vidhya/how-to-filter-noise-with-a-low-pass-filter-python-885223e5e9b7
# LPF : https://www.geeksforgeeks.org/noise-removal-using-lowpass-digital-butterworth-filter-in-scipy-python/
# Windows size : https://www.mathworks.com/matlabcentral/answers/315739-how-to-decide-window-size-for-a-moving-average-filter