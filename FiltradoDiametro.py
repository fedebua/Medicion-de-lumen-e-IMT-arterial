import numpy as np 
from scipy import signal 
import csv
import matplotlib.pyplot as plt 
from scipy import ndimage


with open('Diam.csv', 'r') as Diam_f:
	data_diam = list(csv.reader(Diam_f, delimiter=';'))
with open('IntInf.csv', 'r') as IntInf_f:
	data_intInf = list(csv.reader(IntInf_f, delimiter=';'))
with open('IntSup.csv', 'r') as IntSup_f:
	data_intSup = list(csv.reader(IntSup_f, delimiter=';'))

data_diam = np.array(data_diam)
x_diam = np.linspace(0,len(data_diam) , len(data_diam) )

data_intInf = np.array(data_intInf)
x_intInf = np.linspace(0,len(data_intInf) , len(data_intInf) )

data_intSup = np.array(data_intSup)
x_intSup = np.linspace(0,len(data_intSup) , len(data_intSup) )

#### RAW DATA
fig1=plt.figure("RAW")
plt.subplot(311)
data_diam = np.float64(data_diam)
mean = np.mean(data_diam)
for i in range(len(data_diam)):
	data_diam[i] = data_diam[i] - mean
plt.plot(x_diam,data_diam.astype(float))

plt.subplot(312)
data_intInf = np.float64(data_intInf)
mean = np.mean(data_intInf)
for i in range(len(data_intInf)):
	data_intInf[i] = data_intInf[i] - mean
plt.plot(x_intInf,data_intInf.astype(float))

plt.subplot(313)
data_intSup = np.float64(data_intSup)
mean = np.mean(data_intSup)
for i in range(len(data_intSup)):
	data_intSup[i] = data_intSup[i] - mean
plt.plot(x_intSup,data_intSup.astype(float))

### APLICANDO UN FILTRO DE MEDIANA
#fig2 = plt.figure("Mediana")

plt.subplot(311)



data_diam_median = ndimage.median_filter(data_diam, 5)

plt.plot(x_diam,data_diam_median)

plt.subplot(312)



data_intInf_median = ndimage.median_filter(data_intInf, 5)

plt.plot(x_intInf,data_intInf_median)

plt.subplot(313)



data_intSup_median = ndimage.median_filter(data_intSup, 5)

plt.plot(x_intSup,data_intSup_median)

###### FILTRO GAUSIANO
#fig2 = plt.figure("Gausiano")

plt.subplot(311)

data_diam_gaussian = ndimage.gaussian_filter(data_diam, sigma=1)

plt.plot(x_diam,data_diam_gaussian)

plt.subplot(312)

data_intInf_gaussian = ndimage.gaussian_filter(data_intInf, sigma=1)

plt.plot(x_intInf,data_intInf_gaussian)

plt.subplot(313)

data_intSup_gaussian = ndimage.gaussian_filter(data_intSup,sigma=1)

plt.plot(x_intSup,data_intSup_gaussian)

fig4 =plt.figure("superposicion")
#plt.subplot(211)
plt.plot(x_diam,data_diam_gaussian,label="Diametro interno")
plt.plot(x_intInf,data_intInf_gaussian,label="Int Inf")
plt.plot(x_intSup,data_intSup_gaussian,label="Int Sup")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
# ####### con pasabajos ( fs = 25 samples/seg , supongo Fdigital = Fs/2)
# plt.subplot(313)
# fs = 25
# fa = fs / len(data_diam)
# fdig=fa/fs
# print(fdig)
# b,a = signal.butter(5,1, analog= False,fs=25)

# data_diam_lowpass = signal.filtfilt(b,a,np.ravel(data_diam))
# plt.plot(x_diam,data_diam_lowpass)

plt.show()


