import numpy as np
from scipy import signal
import librosa
import sounddevice as sd

def peaking(G, fc, Q, fs):

    K = np.tan((np.pi * fc)/fs)
    V0 = 10 ** (G/20)

    if V0 < 1:
        V0 = 1/V0
    if G > 0:
        b0 = (1 + ((V0/Q)*K) + K ** 2) / (1 + ((1/Q)*K) + K ** 2)
        b1 =        (2 * (K ** 2 - 1)) / (1 + ((1/Q)*K) + K ** 2)
        b2 = (1 - ((V0/Q)*K) + K ** 2) / (1 + ((1/Q)*K) + K ** 2)
        a1 = b1
        a2 =  (1 - ((1/Q)*K) + K ** 2) / (1 + ((1/Q)*K) + K ** 2)
    else:
        b0 = (1 + ((1/Q)*K) + K ** 2) / (1 + ((V0/Q)*K) + K ** 2)
        b1 =       (2 * (K ** 2 - 1)) / (1 + ((V0/Q)*K) + K ** 2)
        b2 = (1 - ((1/Q)*K) + K ** 2) / (1 + ((V0/Q)*K) + K ** 2)
        a1 = b1
        a2 = (1 - ((V0/Q)*K) + K ** 2) / (1 + ((V0/Q)*K) + K ** 2)

    a = [1, a1, a2]
    b = [b0, b1, b2]
    return b,a

def equilizer(x, Fs ,g):
    Q = 4
    fcp = [31.6,63.2,123.4,247.1,490,983,1975,4000,8000,16000]
    y=0;
    for i in range(1,9) :
        b,a = peaking(g[i], fcp[i], Q, Fs)
        yl = signal.filtfilt(b , a, x.T)
        y=y+yl
    y=y/9
    y=y/np.max(y)
    return y

    if __name__ == '__main__':
        g=[[0,0,0,3,5,5,5,3,2,2],
         [0,4,4,2,0,0,0,0,1,2],
         [0,3,4,2,-1,-1,-1,0,4,5],
         [0,1,2,3,0,0,3,3,1,3]]
        """
    0 vocal 1 classic 2 pop 3 rock
        """
        case=0
        t0=time.time()
        y=equilizer(x,fs,g[case]*4)
        print(time.time()-t0)
