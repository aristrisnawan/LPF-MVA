import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

#MVA
fl = pd.read_csv('4.csv')
X = fl.iloc[:, 1]

def mvaFilter(data,window_size):
  result = data.rolling(window=window_size).mean()
  return result

mvaFilter(X,50).plot(label ='MVA')
plt.plot(X, label='X', alpha = 0.5)