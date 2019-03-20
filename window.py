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
def fun2(f1,h):
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
  f=open(h+'9.txt','r');
  filter_data_string=f.read();
  filter_data9=np.fromstring(filter_data_string,dtype=np.float,sep=',');
  f=open(h+'10.txt','r');
  filter_data_string=f.read();
  filter_data10=np.fromstring(filter_data_string,dtype=np.float,sep=',');
  f=open(h+'11.txt','r');
  filter_data_string=f.read();
  filter_data11=np.fromstring(filter_data_string,dtype=np.float,sep=',');
  f=open(h+'12.txt','r');
  filter_data_string=f.read();
  filter_data12=np.fromstring(filter_data_string,dtype=np.float,sep=',');
  f=open(h+'13.txt','r');
  filter_data_string=f.read();
  filter_data13=np.fromstring(filter_data_string,dtype=np.float,sep=',');
  f=open(h+'14.txt','r');
  filter_data_string=f.read();
  filter_data14=np.fromstring(filter_data_string,dtype=np.float,sep=',');
  f=open(h+'15.txt','r');
  filter_data_string=f.read();
  filter_data15=np.fromstring(filter_data_string,dtype=np.float,sep=',');
  f=open(h+'16.txt','r');
  filter_data_string=f.read();
  filter_data16=np.fromstring(filter_data_string,dtype=np.float,sep=',');
  f=open(h+'17.txt','r');
  filter_data_string=f.read();
  filter_data17=np.fromstring(filter_data_string,dtype=np.float,sep=',');
  f=open(h+'18.txt','r');
  filter_data_string=f.read();
  filter_data18=np.fromstring(filter_data_string,dtype=np.float,sep=',');
  f=open(h+'19.txt','r');
  filter_data_string=f.read();
  filter_data19=np.fromstring(filter_data_string,dtype=np.float,sep=',');
  f=open(h+'20.txt','r');
  filter_data_string=f.read();
  filter_data20=np.fromstring(filter_data_string,dtype=np.float,sep=',');  


  original_data=np.array([original_data[0,:],original_data[1,:],original_data[0,:]-original_data[1,:],original_data[1,:]-original_data[0,:],(original_data[0,:]+original_data[1,:])*0.707]);

  output1=np.convolve(original_data[0,:],filter_data1);
  output1=output1/output1.max();

  output2=np.convolve(original_data[0,:],filter_data2);
  output2=output2/output2.max();

  output3=np.convolve(original_data[0,:],filter_data3);
  output3=output3/output3.max();

  output4=np.convolve(original_data[0,:],filter_data4);
  output4=output4/output4.max();


  output5=np.convolve(original_data[1,:],filter_data5);
  output5=output5/output5.max();

  output6=np.convolve(original_data[1,:],filter_data6);
  output6=output6/output6.max();

  output7=np.convolve(original_data[1,:],filter_data7);
  output7=output7/output7.max();

  output8=np.convolve(original_data[1,:],filter_data8);
  output8=output8/output8.max();


  output9=np.convolve(original_data[2,:],filter_data9);
  output9=output9/output9.max();

  output10=np.convolve(original_data[2,:],filter_data10);
  output10=output10/output10.max();

  output11=np.convolve(original_data[2,:],filter_data11);
  output11=output11/output11.max();

  output12=np.convolve(original_data[2,:],filter_data12);
  output12=output12/output12.max();


  output13=np.convolve(original_data[3,:],filter_data13);
  output13=output13/output13.max();

  output14=np.convolve(original_data[3,:],filter_data14);
  output14=output14/output14.max();

  output15=np.convolve(original_data[3,:],filter_data15);
  output15=output15/output15.max();

  output16=np.convolve(original_data[3,:],filter_data16);
  output16=output16/output16.max();


  output17=np.convolve(original_data[4,:],filter_data17);
  output17=output17/output17.max();

  output18=np.convolve(original_data[4,:],filter_data18);
  output18=output18/output18.max();

  output19=np.convolve(original_data[4,:],filter_data19);
  output19=output19/output19.max();

  output20=np.convolve(original_data[4,:],filter_data20);
  output20=output20/output20.max();



  sink1=output1+output5+output9+output17;
  sink2=output2+output6+output10+output18;
  sink3=output3+output7+output11+output19;
  sink4=output4+output8+output12+output20;
  global output
  output=np.array([sink1,sink2,sink3,sink4]);
  output=output.T;









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
def h3():
    fun2(e_inputfile.get(),'VS')

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
    text='VS',      
    width=15, height=2, 
    command=h3)     
b3.pack()   

window.mainloop()

