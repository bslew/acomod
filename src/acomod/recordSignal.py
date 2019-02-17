'''
Created on Feb 11, 2019

@author: blew
'''

from PyQt5 import QtCore
# from PyQt5.QtCore import QThread,QTimer

import sounddevice as sd
import numpy as np
import random
import time
from scipy.signal import periodogram
from acomod import global_settings
import sys

class newSample(QtCore.QThread):
    newSampleSignal = QtCore.pyqtSignal(list,list)
    
    
#     def __init__(self, update_time=0.5, sampling_freq=44100, soundSpeed=343, parent=None):
    def __init__(self, update_time=0.5, sampling_freq=44100, soundSpeed=343, parent=None):
        '''
        update_time [s] - time after which new sample will be generated
        '''
        super(newSample,self).__init__(parent)
        settings=global_settings.mySettings(self)

        self.update_time=1.0/settings.value('plotRefreshRate',type=float)
        self.sampling_freq=settings.value('sampling',type=float)
        self.soundSpeed=settings.value('soundSpeed',type=float)
        self.plotPointsCount=settings.value('plotPointsCount',500,type=int)
        self.generateNew=True
#         self.timer=QtCore.QTimer(self)
#         print('update time: {}'.format(int(update_time*1000)))
#         self.timer.setInterval(int(update_time*1000))
#         self.timer.timeout.connect(self.sendNewSample)
        
    
    def run(self):
        print("New thread")

#         self.timer.start()
        while self.generateNew:
#             print("data thread")
            self.sendNewSample()
            settings=global_settings.mySettings(self)
            time.sleep(1./settings.value("plotRefreshRate",type=float))
#             time.sleep(1000)
        
    
    
    def getFFT(self,y,sampling=1,maxPoints=1000):
#         ft=np.fft.fft(y)
#         n=len(y)
#         L=1.0/(sampling*n)
#         p=ft.real*ft.real+ft.imag*ft.imag
#         print(len(y))
#         print(len(p))
#         f=[1.0/L for x in range(n)]
#         print(p)

        p=periodogram(y, fs=sampling,nfft=maxPoints)
#         print(p)
        x=p[0][1:] # drop 0th frequency
        y=p[1][1:]
        return x,y


    def getNewData(self,n):
        x=np.arange(n, dtype=float)
        noise=np.asarray([random.random() for _ in range(n)],dtype=float)
        y=np.sin(x)+noise*0.1
        return x,y


    def getSoundData(self,n):
        duration=self.update_time
        fs=self.sampling_freq
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)        
        myrecording=np.mean(myrecording,axis=1)
        t=np.arange(0.0,duration,1.0/fs)
        print(myrecording)
        return t,myrecording

    
    @QtCore.pyqtSlot()
    def sendNewSample(self):
        n=500
#         x,y=def.getNewData(n)
        x,y=self.getSoundData(n)

        
        x,y=self.getFFT(y,self.sampling_freq,maxPoints=self.plotPointsCount)
        
#         print("Emitting new sample")
        self.newSampleSignal.emit(list(x),list(y))
        
        


class newSoundSample(QtCore.QThread):
    newSampleSignal = QtCore.pyqtSignal(list,list)
    
    
    def __init__(self, update_time=0.5, sampling_freq=44100, soundSpeed=343, recordingLength=1.0, soundFile=None, parent=None):
        '''
        update_time [s] - time after which new sample will be generated
        '''
        if sys.version_info[0] < 3:
            super(newSoundSample,self).__init__(parent)
        else:
            super().__init__(parent)
        settings=global_settings.mySettings(self)

        self.update_time=1.0/settings.value('plotRefreshRate',type=float)
        self.sampling_freq=settings.value('sampling',type=float)
        self.soundSpeed=settings.value('soundSpeed',type=float)
        self.plotPointsCount=settings.value('plotPointsCount',500,type=int)
        self.recordingLength=recordingLength
        
        self.generateNew=True
        self.soundFile=soundFile
        

        

        
    def callback(self,indata, frames, time, status):
        fftsize=500
#         gain=1.0
#         if status:
#             text = ' ' + str(status) + ' '
#             print('\x1b[34;40m', text.center(40, '#'),
#                   '\x1b[0m', sep='')
#         if any(indata):
#             magnitude = np.abs(np.fft.rfft(indata[:, 0], n=fftsize))
#             magnitude *= gain / fftsize
#             print(magnitude)
#         print(indata)
#         print(np.shape(indata))
        x,y=self.getFFT(indata[:,0],self.sampling_freq,maxPoints=self.plotPointsCount)

#         else:
#             print('no input')
  
        self.newSampleSignal.emit(list(x),list(y))
        
        
    def runSoundFileSample(self):
        print("New sound file thread")
        
        
#         import sounddevice as sd
        import soundfile as sf
        
        data, fs = sf.read(self.soundFile, dtype='float32')
        x=list(np.arange(0.0,self.update_time,1.0/fs))

        print("data size: ", len(data))        
        i=0
        n=len(x)
        while self.generateNew:
            data=data.reshape(len(data),1)
            sample=np.mean(np.roll(data,-n*i,axis=0)[0:n],axis=1)
#             print(sample)

#             x,y=self.getFFT(sample,fs,maxPoints=self.plotPointsCount)
            x,y=self.getFFT(sample,fs)
            self.newSampleSignal.emit(list(x),list(y))
            i+=1

#             settings=global_settings.mySettings(self)
            time.sleep(self.update_time)
        
        
#         import sounddevice as sd
#         import soundfile as sf
#         import queue
#          
#         self.device=7
#         blockSize=int(self.sampling_freq* self.update_time)
#         bufferSize=blockSize*1000
#         print(bufferSize)
#         print(blockSize)
#         q = queue.Queue(maxsize=bufferSize)
#         with sf.SoundFile(self.soundFile) as f:
#             for _ in range(bufferSize):
#                 data = f.buffer_read(int(blockSize), dtype='float32')
# #                 data = f.buffer_read(1, dtype='float32')
#                 if not data:
#                     break
#                 q.put_nowait(data)  # Pre-fill queue
# 
#      
#             stream = sd.RawOutputStream(
#                 samplerate=f.samplerate, blocksize=blockSize,
#                 device=self.device, channels=f.channels, dtype='float32',
#                 callback=self.callback, 
# #                 finished_callback=event.set
#                 )
#  
#             with stream:
#                 timeout = blockSize * bufferSize / f.samplerate
#                 while data:
#                     data = f.buffer_read(blockSize, dtype='float32')
#                     q.put(data, timeout=timeout)
# #                 event.wait()  # Wait until playback is finished    
#              
#                     if self.generateNew==False:
#                         break
    
    def runInputStreamSample(self):
        print("New input stream thread")
        self.device=7


            

        with sd.InputStream(
                            channels=1, 
#                             device=self.device, 
                            callback=self.callback,
                            blocksize=int(self.sampling_freq*self.recordingLength),
                            samplerate=self.sampling_freq):
            print(self.sampling_freq*self.recordingLength)
            while self.generateNew:
#                 print("generate new")
#                 settings=global_settings.mySettings(self)
#                 time.sleep(1./settings.value("plotRefreshRate",type=float))
                time.sleep(self.update_time)
        
    
    def run(self):
        
        if self.soundFile!=None:
            self.runSoundFileSample()
        else:
            self.runInputStreamSample()
    
    
    def getFFT(self,y,sampling=1,maxPoints=1000):
#         ft=np.fft.fft(y)
#         n=len(y)
#         L=1.0/(sampling*n)
#         p=ft.real*ft.real+ft.imag*ft.imag
#         print(len(p))
#         f=[1.0/L for x in range(n)]
#         print(p)

#         p=periodogram(y, fs=sampling,nfft=maxPoints)
        p=periodogram(y, fs=sampling)
#         print(p)
        x=p[0][1:] # drop 0th frequency
        Y=p[1][1:]
        print("FFT: %i, min./max.freq.: %f/%f" % (len(y),min(x),max(x)))
        return x,Y


    def getNewData(self,n):
        x=np.arange(n, dtype=float)
        noise=np.asarray([random.random() for _ in range(n)],dtype=float)
        y=np.sin(x)+noise*0.1
        return x,y


    def getSoundData(self,n):
        duration=self.update_time
        fs=self.sampling_freq
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)        
        myrecording=np.mean(myrecording,axis=1)
        t=np.arange(0.0,duration,1.0/fs)
        print(myrecording)
        return t,myrecording

    
    @QtCore.pyqtSlot()
    def sendNewSample(self):
        n=500
#         x,y=def.getNewData(n)
        x,y=self.getSoundData(n)

        
        x,y=self.getFFT(y,self.sampling_freq,maxPoints=self.plotPointsCount)
        
#         print("Emitting new sample")
        self.newSampleSignal.emit(list(x),list(y))
        
        

        
        