# import wave
# import matplotlib.pyplot as plt
# import time
# import numpy as np
# y= []
# obj = wave.open('media/basic1note.wav','r')
# print( "Number of channels",obj.getnchannels())
# print ( "Sample width",obj.getsampwidth())
# print ( "Frame rate.",obj.getframerate())
# print ("Number of frames",obj.getnframes())
# print ( "parameters:",obj.getparams())
#
# for j in obj.readframes(obj.getnframes()):
#      y.append(j)
#
# print(len(y))
# obj.close()
#
#
#
# bpm = 100
# bps = bpm / 60
#
# time_per_frame = 1 / obj.getframerate()
# total_time = obj.getnframes() * time_per_frame
# print(total_time)
#
# x =  np.arange(0, total_time, time_per_frame/2)
#
# print(len(x))
#
# plt.plot(x, y)
#
# plt.show()
#
# https://towardsdatascience.com/music-in-python-2f054deb41f4
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')

sample_rate, bassDrum = wavfile.read('media/bassDrum1.wav')
#FFT
t = np.arange(bassDrum.shape[0])
freq = np.fft.fftfreq(t.shape[-1])*sample_rate
sp = np.fft.fft(bassDrum)

# Plot spectrum
plt.plot(freq, abs(sp.real))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Spectrum of Bass Drum')
plt.xlim((0, 1000))
plt.grid()


sample_rate2, crash = wavfile.read('media/crash1.wav')
t2 = np.arange(crash.shape[0])
freq2 = np.fft.fftfreq(t2.shape[-1])*sample_rate2
sp2 = np.fft.fft(crash)

plt.plot(freq2, abs(sp2.real))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Spectrum of Snare')
plt.xlim((0, 1000))
plt.grid()


sample_rate3, snare = wavfile.read('media/snare2.wav')
t3 = np.arange(snare.shape[0])  # how many elements have my array
freq3 = np.fft.fftfreq(t3.shape[-1])*sample_rate3  # -1 is the # of coluums but in this case is the same as [0]
# fft.fftfreq(n, d=1.0)
# f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (d*n)   if n is even
# f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (d*n)   if n is odd
#  for this code d = (1/sample_rate3) that why it is mutiplied later
#  1/sample_rate = unit of the sample spacing (inverse of the sampling rate)

sp3 = np.fft.fft(snare)

plt.plot(freq3, abs(sp3.real))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Spectrum of crash')
plt.xlim((0, 900))
plt.grid()
plt.show()

sample_rate4, song = wavfile.read('media/badumtss1.wav')

# t3 = np.arange(song.shape[0])
# freq4 = np.fft.fftfreq(t3.shape)

print(sample_rate3)
print(t3)
print(np.fft.fftfreq(t3.shape[0]))
print(np.fft.fftfreq(t3.shape[-1], d = (1/sample_rate3)))
print(abs(sp3.real))



