import pandas as pd
import matplotlib.pylab as plt
from scipy.signal import butter, lfilter, filtfilt

dataGyro = pd.DataFrame(pd.read_csv('gyro.csv').rolling(window=1).mean())
dataAcel = pd.DataFrame(pd.read_csv('acel.csv').rolling(window=1).mean())

fs = 100; # nilai frequents
nyq = 0.5 * fs # nilai nyqusit
wn = 20/nyq; 



def lowpass(col): # lowpass filter untuk data acelometer
    b, a = butter(2, wn, btype='low');
    return lfilter(b, a, dataAcel.iloc[:,col]);

def highpass(col):
    b,a = butter(2, wn, btype='high'); # highpass filter untuk data gyroscop
    return lfilter(b, a, dataGyro.iloc[:,col]);

plt.xlabel('t/s')
plt.ylabel('')


low = lowpass(1);
plt.plot(low, label="acel")

high = highpass(1)
plt.plot(high, label='gyro')

plt.legend();
plt.show();