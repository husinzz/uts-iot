import pandas as pd;
import matplotlib.pyplot as plt;
import math;
from scipy.signal import butter, filtfilt;
import scipy.integrate as integral
import numpy as np

dataGyro = pd.DataFrame(pd.read_csv('gyro.csv').rolling(window=1).mean())
dataAcel = pd.DataFrame(pd.read_csv('acel.csv').rolling(window=1).mean())
dataAceltang = pd.DataFrame(pd.read_csv('acelwithtang.csv').rolling(window=1).mean())

fs = 100; # nilai frequents
nyq = 0.5 * fs # nilai nyqusit
wn = 2/nyq; 

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
    plt.show();

def lowpass(col): # lowpass filter untuk data acelometer
    b, a = butter(2, wn, btype='low');
    return filtfilt(b, a, dataAcel.iloc[:,col]);

def highpass(col):
    b,a = butter(2, wn, btype='high'); # highpass filter untuk data gyroscop
    return filtfilt(b, a, dataGyro.iloc[:,col]);

def findAtan():
    atan = []
    for i in range(len(dataAcel)):
        atan.append(math.atan2(dataAceltang.iloc[i]['Linear Acceleration z (m/s^2)'], dataAceltang.iloc[i]['Linear Acceleration y (m/s^2)']))
    return atan

def integralYaw():
    gral = []
    for i in range(len(dataGyro)):
        gral.append(lambda x : )
    return gral

def gait():
    gait = []
    gral = integralYaw()
    atan = findAtan();
    for i in range(len(gral)):
        gait.append(((gral[i])*0.8) + ((atan[i])*0.2))
    return gait

# plotRawdata(); # Bagian 2 
# plt.plot(findAtan(), label='Rho'); # Bagian rumurs archtan
# plt.plot(dataGyro.iloc[:,3], label='Gyro z') # buat di banding sama archtan


plt.legend(loc='upper right');
plt.show();