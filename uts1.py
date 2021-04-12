import pandas as pd
import matplotlib.pylab as plt
from scipy.signal import butter, lfilter, filtfilt

dataGyro = pd.DataFrame(pd.read_csv('gyro.csv').rolling(window=1).mean())
dataAcel = pd.DataFrame(pd.read_csv('acel.csv').rolling(window=1).mean())

def plotRawdata():
    l = ['x','y','z']
    for i in range(1, 4):
        plt.subplot(3,2,(2*i)-1)
        plt.plot(dataAcel.iloc[:,i], label=l[i-1])
        plt.xlabel(l[i-1])
        plt.legend(loc='upper left');
        plt.subplot(3,2,2*i)
        plt.plot(dataGyro.iloc[:,i], label=l[i-1])
        plt.xlabel(l[i-1])
        plt.legend(loc='upper left');
        print(i)
    plt.show();

fs = 100; # nilai frequents
nyq = 0.5 * fs # nilai nyqusit
wn = 1/nyq; 

def lowpass(col): # lowpass filter untuk data acelometer
    b, a = butter(2, wn, btype='low');
    return filtfilt(b, a, dataAcel.iloc[:,col]);

plotRawdata();