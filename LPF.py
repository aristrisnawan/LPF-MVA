import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

#LPF
fl = pd.read_csv('4.csv')
X = fl.iloc[:, 1]

def lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def lowpassFilter(data, cutoff, fs, order=5):
    b, a = lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

ord = 6
z = 30.0
cutoff = 3.667

b, a = lowpass(cutoff, z, ord)

y = lowpassFilter(X, cutoff, z, ord)
plt.plot(X, label='B', alpha = 0.5)
plt.plot(y, linewidth=2, label='filtered data')