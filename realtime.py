
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

stream = p.open(format=p.get_format_from_width(4),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)
h='SW';

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

params=wf.getparams();
print('start stream \n')
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
    output=output[:,0:1024]
    print(output.dtype)
    output=output.T;
    output=output.reshape(1,-1);

    b=bytearray(output)
    b=bytes(b)
    stream.write(b)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()
