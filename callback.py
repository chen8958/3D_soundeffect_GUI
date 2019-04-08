import pyaudio
import wave
import time
import sys
import numpy as np

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

f = wave.open(sys.argv[1], 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()
output=np.array([]);
def fun(origianl_data):
    global filter_data1,filter_data2,filter_data3,filter_data4,filter_data5,filter_data6,filter_data7,filter_data8
    params=f.getparams();
    original_data_string=f.readframes(params[3]);
    original_data=np.fromstring(original_data_string,dtype=np.short);
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
    global output
    output=np.array([sink1,sink2,sink3,sink4]);
    output=output/np.absolute(output).max();
    output=output.T;


# define callback (2)
def callback(in_data, frame_count, time_info, status):
    data = f.readframes(frame_count)
    print(callback.i,pyaudio.paContinue);
    origianl_data=np.fromstring(data,dtype=np.short);
    fun(origianl_data);
    callback.i=callback;
    global output
    output.shape=1,-1
    b=bytearray(output)
    b=bytes(b)
    return (b, pyaudio.paContinue)
callback.i=0
# open stream using callback (3)
stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                channels=f.getnchannels(),
                rate=f.getframerate(),
                output=True,
                stream_callback=callback)

# start the stream (4)
#f=wave.open('Ring.wav','rb');
print('processing.....................................');
h='SW';

global filter_data1,filter_data2,filter_data3,filter_data4,filter_data5,filter_data6,filter_data7,filter_data8;
f=open(h+'1.txt','r');
filter_data_string=f.read();
filter_data1=np.fromstring(filter_data_string,dtype=np.float,sep=',');
f=open(h+'2.txt','r');
filter_data_string=f.read();
filter_data2=np.fromstring(filter_data_string,dtype=np.float,sep=',');
f=open(h+'3.txt','r');
filter_data_string=f.read();
filter_data3=np.fromstring(filter_data_string,dtype=np.float,sep=',');
f=open(h+'4.txt','r');
filter_data_string=f.read();
filter_data4=np.fromstring(filter_data_string,dtype=np.float,sep=',');
f=open(h+'5.txt','r');
filter_data_string=f.read();
filter_data5=np.fromstring(filter_data_string,dtype=np.float,sep=',');
f=open(h+'6.txt','r');
filter_data_string=f.read();
filter_data6=np.fromstring(filter_data_string,dtype=np.float,sep=',');
f=open(h+'7.txt','r');
filter_data_string=f.read();
filter_data7=np.fromstring(filter_data_string,dtype=np.float,sep=',');
f=open(h+'8.txt','r');
filter_data_string=f.read();
filter_data8=np.fromstring(filter_data_string,dtype=np.float,sep=',');
print('start stream \n')
stream.start_stream()


# wait for stream to finish (5)
while stream.is_active():
    time.sleep(0.1)

# stop stream (6)
stream.stop_stream()
stream.close()
f.close()

# close PyAudio (7)
p.terminate()
