import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, filtfilt

dataGyro = pd.read_csv('gyro.csv')
dfGyro = pd.DataFrame(dataGyro)

dataAcel = pd.read_csv('acel.csv')
dfAcel = pd.DataFrame(dataAcel)

fs = 100 # 100hz sesuai soal
nyq = 0.5 * fs 
cut_off = 20 # 3 data(xyz) / 60 second jalan 
order = 2

def lowpass_filter(dataAcel, cut_off, fs, order):
    normal_cutoff = cut_off/nyq
    b, a = butter(order,normal_cutoff, btype="low")
    y = filtfilt(b, a, dataAcel, padlen=0)
    return y

def butter_highpass(cutoff,fs, order):
    normal_cutoff = cutoff / nyq
    b,a = butter(order,normal_cutoff, btype='high', analog=False)
    y = filtfilt(b,a,dataGyro, padlen=1)
    return y

def plotGambar():
    lowpassPlot = lowpass_filter(dataAcel, cut_off, fs, order)
    plt.plot(lowpassPlot, label='Acel')

    # highpssPlot = butter_highpass(cut_off,fs, order)
    # plt.plot(highpssPlot,label='Gyro')

    for i in range(1, 4):
        acel = dfAcel.iloc[:,i].rolling(window=4).mean()
        # gyro = dfGyro.iloc[:,i].rolling(window=4).mean()
        plt.plot(acel,label='acel')
        # plt.plot(gyro,label='gyro')

    plt.legend();
    plt.show();


plotGambar()