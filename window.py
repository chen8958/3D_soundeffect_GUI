import Tkinter as tk
import wave
import numpy as np
import os
import scipy.io.wavfile
import sounddevice as sd
#open wav file
#filename=input('plese enter file name : \n');
def fun(f1,h):
  f=wave.open(f1,'rb');
  print('processing.....................................');
  params=f.getparams();
  original_data_string=f.readframes(params[3]);
  original_data=np.fromstring(original_data_string,dtype=np.short);
  original_data.shape=-1,2;
  original_data=original_data.T;
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
  

  output1=np.convolve(original_data[0,:],filter_data1);
  output1=output1/output1.max();

  output2=np.convolve(original_data[0,:],filter_data2);
  output2=output2/output2.max();

  output3=np.convolve(original_data[0,:],filter_data3);
  output3=output3/output3.max();

  output4=np.convolve(original_data[0,:],filter_data4);
  output4=output4/output4.max();

  output5=np.convolve(original_data[1,:],filter_data1);
  output5=output5/output5.max();

  output6=np.convolve(original_data[1,:],filter_data2);
  output6=output6/output6.max();

  output7=np.convolve(original_data[1,:],filter_data3);
  output7=output7/output7.max();

  output8=np.convolve(original_data[1,:],filter_data4);
  output8=output8/output8.max();

  sink1=output1+output5;
  sink2=output2+output6;
  sink3=output3+output7;
  sink4=output4+output8;
  global output
  output=np.array([sink1,sink2,sink3,sink4]);
  output=output.T;
  #sd.play(output,44100);
  #scipy.io.wavfile.write(f2, 44100, output);




window = tk.Tk()
window.title('Listening test')
window.geometry('500x250')
frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')
tk.Label(frm_l, text='input_file name').pack()
e_inputfile = tk.Entry(frm_l)
e_inputfile.pack()
#tk.Label(frm_l, text='output_file name').pack()
#e_outputfile = tk.Entry(frm_l)
#e_outputfile.pack()
def play():
    #sd.play(output,44100);
    print(output);
def stop():
    sd.stop();
def h1():
    fun(e_inputfile.get(),'SW')
def h2():
    fun(e_inputfile.get(),'XTC')

b_play = tk.Button(frm_l, 
    text='play',      
    width=15, height=2, 
    command=play)     
b_play.pack() 
b_stop = tk.Button(frm_l, 
    text='stop',      
    width=15, height=2, 
    command=stop)     
b_stop.pack()
b1 = tk.Button(frm_r, 
    text='source widely',      
    width=15, height=2, 
    command=h1)     
b1.pack()
b2 = tk.Button(frm_r, 
    text='XTC',      
    width=15, height=2, 
    command=h2)     
b2.pack()
b3 = tk.Button(frm_r, 
    text='h3',      
    width=15, height=2, 
    command=h1)     
b3.pack()   

window.mainloop()

