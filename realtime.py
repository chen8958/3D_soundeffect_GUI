#!/usr/bin/python
# -*- coding = utf-8 -*-
"""
@author : Tony Chen
"""
import pyaudio
import wave
import sys
import numpy as np
import sounddevice as sd

CHUNK = 1024

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()
##channel must be equall output channel (4) channels=wf.getnchannels()
stream = p.open(format=p.get_format_from_width(4),
                channels=4,
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)
h='XTC';

global filter_data1,filter_data2,filter_data3,filter_data4,filter_data5,filter_data6,filter_data7,filter_data8;
f=open(h+'1.txt','r');
filter_data_string=f.read();
filter_data1=np.fromstring(filter_data_string,dtype=np.float32,sep=',');
f=open(h+'2.txt','r');
filter_data_string=f.read();
filter_data2=np.fromstring(filter_data_string,dtype=np.float32,sep=',');
f=open(h+'3.txt','r');
filter_data_string=f.read();
filter_data3=np.fromstring(filter_data_string,dtype=np.float32,sep=',');
f=open(h+'4.txt','r');
filter_data_string=f.read();
filter_data4=np.fromstring(filter_data_string,dtype=np.float32,sep=',');
f=open(h+'5.txt','r');
filter_data_string=f.read();
filter_data5=np.fromstring(filter_data_string,dtype=np.float32,sep=',');
f=open(h+'6.txt','r');
filter_data_string=f.read();
filter_data6=np.fromstring(filter_data_string,dtype=np.float32,sep=',');
f=open(h+'7.txt','r');
filter_data_string=f.read();
filter_data7=np.fromstring(filter_data_string,dtype=np.float32,sep=',');
f=open(h+'8.txt','r');
filter_data_string=f.read();
filter_data8=np.fromstring(filter_data_string,dtype=np.float32,sep=',');
buffer=np.zeros((4,len(filter_data1)),'float32');
params=wf.getparams();
print('start stream \n')
i=0;
while data != '':
    original_data=np.fromstring(data,dtype=np.short);
    original_data.shape=-1,params[0];
    original_data=original_data.T;
    output1=np.convolve(original_data[0,:],filter_data1);
    output2=np.convolve(original_data[0,:],filter_data2);
    output3=np.convolve(original_data[0,:],filter_data3);
    output4=np.convolve(original_data[0,:],filter_data4);
    output5=np.convolve(original_data[1,:],filter_data5);
    output6=np.convolve(original_data[1,:],filter_data6);
    output7=np.convolve(original_data[1,:],filter_data7);
    output8=np.convolve(original_data[1,:],filter_data8);
    sink1=output1+output5;
    sink2=output2+output6;
    sink3=output3+output7;
    sink4=output4+output8;
    output=np.array([sink1,sink2,sink3,sink4]);
    output=output/np.absolute(output).max();
    output[:,0:len(buffer[0])]=output[:,0:len(buffer[0])]+buffer;
    buffer=output[:,1024:];
    output=output[:,0:1024];
    ##attention!! if two channels output may cause down sampling
    #print(output.dtype,output.shape,buffer.shape)
    print("callbacktime = %d"%(i));
    i=i+1;
    output=output.T;
    output=output.reshape(1,-1);

    b=bytearray(output)
    b=bytes(b)
    stream.write(b)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()
