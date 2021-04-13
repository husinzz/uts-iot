import pandas as pd;
import matplotlib.pyplot as plt;
import math;
from scipy.integrate import quad;
import numpy as np;
from scipy.signal import butter, filtfilt;

dataGyro = pd.DataFrame(pd.read_csv('gyro.csv').rolling(window=1).mean())
dataAcel = pd.DataFrame(pd.read_csv('acel.csv').rolling(window=1).mean())

fs = 100; # nilai frequents
nyq = 0.5 * fs # nilai nyqusit
wn = 2/nyq; 

def plotRawdata(): # Soal 3
    l = ['x','y','z']
    for i in range(1, 4):
        plt.subplot(3,2,(2*i)-1)
        plt.plot(dataAcel.iloc[:,i], label=l[i-1])
        plt.legend(loc='upper left');

        plt.subplot(3,2,2*i)
        plt.plot(dataGyro.iloc[:,i], label=l[i-1])
        plt.legend(loc='upper left');
    plt.show();

def findAtan(): # Soal 4
    atan = []
    for i in range(len(dataAcel)):
        atan.append(math.atan2(dataAcel.iloc[i]['Linear Acceleration z (m/s^2)'], dataAcel.iloc[i]['Linear Acceleration y (m/s^2)']))
    return atan

# Bagian soal 4
def integrals():
    gral = []
    for i in range(len(dataGyro)):
        ans, err = quad(lambda x : dataAcel.iloc[i]['Linear Acceleration z (m/s^2)'],0,1)
        gral.append(ans)
    return gral

def buatgait():
    gait = []
    gral = integrals()
    cel = findAtan()
    for i in range(len(dataGyro)):
        val = (gral[i] * 0.8) + (cel[i] * 0.2)
        gait.append(val)
    return  gait

def lowpass(var): # lowpass filter untuk data acelometer
    b, a = butter(2, wn, btype='low');
    return filtfilt(b, a, var);

def highpass(var): # Highpass filter untuk data gyro
    b,a = butter(2, wn, btype='high'); # highpass filter untuk data gyroscop
    return filtfilt(b, a, var); #dataGyro.iloc[:,3]

# END SOAL 4

# plt.plot(lowpass(findAtan()), label="RHO")
# plt.plot(highpass(integrals()), label="Gyro Z")

plt.plot(buatgait())

plt.legend(loc='upper right')
plt.show()

