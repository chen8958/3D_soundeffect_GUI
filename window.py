import wave
import numpy as np
import sys
if sys.version_info.major==2:
  import Tkinter as tk
elif sys.version_info.major==3:
  import tkinter as tk
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
  original_data.shape=-1,params[0];
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
  #sd.play(output,44100);
  #scipy.io.wavfile.write(f2, 44100, output);
def fun2(f1,h):
  f=wave.open(f1,'rb');
  print('processing.....................................');
  params=f.getparams();
  original_data_string=f.readframes(params[3]);
  original_data=np.fromstring(original_data_string,dtype=np.short);
  original_data.shape=-1,params[0];
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


  original_data=np.array([original_data[0,:],original_data[1,:],original_data[0,:]-original_data[1,:],original_data[1,:]-original_data[0,:],(original_data[0,:]*0.5+original_data[1,:]*0.5)]);

  output1=np.convolve(original_data[0,:],filter_data1);

  output2=np.convolve(original_data[0,:],filter_data2);

  output3=np.convolve(original_data[0,:],filter_data3);


  output4=np.convolve(original_data[0,:],filter_data4);



  output5=np.convolve(original_data[1,:],filter_data5);


  output6=np.convolve(original_data[1,:],filter_data6);


  output7=np.convolve(original_data[1,:],filter_data7);


  output8=np.convolve(original_data[1,:],filter_data8);


  output9=np.convolve(original_data[2,:],filter_data9);


  output10=np.convolve(original_data[2,:],filter_data10);


  output11=np.convolve(original_data[2,:],filter_data11);


  output12=np.convolve(original_data[2,:],filter_data12);



  output13=np.convolve(original_data[3,:],filter_data13);


  output14=np.convolve(original_data[3,:],filter_data14);


  output15=np.convolve(original_data[3,:],filter_data15);


  output16=np.convolve(original_data[3,:],filter_data16);



  output17=np.convolve(original_data[4,:],filter_data17);


  output18=np.convolve(original_data[4,:],filter_data18);


  output19=np.convolve(original_data[4,:],filter_data19);


  output20=np.convolve(original_data[4,:],filter_data20);




  sink1=output1+output5+output9+output17+output13;
  sink2=output2+output6+output10+output18+output14;
  sink3=output3+output7+output11+output19+output15;
  sink4=output4+output8+output12+output20+output16;
  global output
  output=np.array([sink1,sink2,sink3,sink4]);
  output=output/np.absolute(output).max();
  output=output.T;

def fun3(eq):
  f=open(eq+'.txt','r');
  filter_data_string=f.read();
  filter_data=np.fromstring(filter_data_string,dtype=np.float,sep=',');
  global output
  if output.shape[1]==4:
	  output=output.T;
	  output=np.array([np.convolve(output[0,:],filter_data)\
	,np.convolve(output[1,:],filter_data),np.convolve(output[2,:],filter_data)\
	,np.convolve(output[3,:],filter_data)]);
  else:
	  output=output.T;
	  output=np.array([np.convolve(output[0,:],filter_data),np.convolve(output[1,:],filter_data)]);
  output=output.T;
  output=output/np.absolute(output).max();
  print(output);









window = tk.Tk()
window.title('Listening test')
window.geometry('500x250')





frm = tk.Frame(window)
frm.pack()
frm_1 = tk.Frame(window)
frm_2 = tk.Frame(window)
frm_3 = tk.Frame(window)
frm_1.pack()
frm_2.pack()
frm_3.pack()
tk.Label(frm_1, text='input_file name').pack()
e_inputfile = tk.Entry(frm_1)
e_inputfile.pack()
tk.Label(frm_1, text='effect').pack()
tk.Label(frm_2, text='equalization').pack()
tk.Label(frm_3, text=' ').pack()













#tk.Label(frm_l, text='output_file name').pack()
#e_outputfile = tk.Entry(frm_l)
#e_outputfile.pack()
def play():
    global output;
    sd.play(output,44100);
    print(output);
def stop():
    sd.stop();
def h1():
    fun(e_inputfile.get(),'SW')
def h2():
    fun(e_inputfile.get(),'XTC')
def h3():
    fun2(e_inputfile.get(),'VS')
def load_origin():
    f=wave.open(e_inputfile.get(),'rb');
    print('processing.....................................');
    params=f.getparams();
    original_data_string=f.readframes(params[3]);
    original_data=np.fromstring(original_data_string,dtype=np.short);
    original_data.shape=-1,params[0];
    original_data=original_data.astype('float');
    original_data=original_data/np.absolute(original_data).max();
    origianl_data=0.08*original_data;
    global output;
    if original_data.shape[1]==2:
       output=origianl_data;
    else:
        size=original_data[:,1].shape;
        original_data1=original_data[:,1]
        original_data1.shape=size[0],1;
        original_data2=original_data[:,2]
        original_data2.shape=size[0],1;
        original_data3=original_data[:,3]
        original_data3.shape=size[0],1;
        original_data0=original_data[:,0]
        original_data0.shape=size[0],1;
        temp1=np.concatenate((original_data2,original_data0),axis=1);
        temp2=np.concatenate((original_data1,original_data3),axis=1);
        output=np.concatenate((temp1,temp2),axis=1);
def play_original():
    f=wave.open(e_inputfile.get(),'rb');
    print('processing.....................................');
    params=f.getparams();
    original_data_string=f.readframes(params[3]);
    original_data=np.fromstring(original_data_string,dtype=np.short);
    original_data.shape=-1,params[0];
    original_data=original_data.astype('float');
    original_data=original_data/np.absolute(original_data).max();
    origianl_data=0.08*original_data;
    sd.play(original_data,44100);
button_width=9;
button_height=2;

original = tk.Button(frm_1,
    text='origianl sound',
    width = button_width, height = button_height,
    command=load_origin,bg='yellow')
original.pack(side='left')
b_play = tk.Button(frm_3,
    text='play',
    width = button_width, height = button_height,
    command=play,bg='red')
b_play.pack(side='left')
b_stop = tk.Button(frm_3,
    text='stop',
    width = button_width, height = button_height,
    command=stop,bg='red')
b_stop.pack(side='left')
b1 = tk.Button(frm_1,
    text='source widening',
    width = button_width, height = button_height,
    command=h1,bg='yellow')
b1.pack(side='left')
    text='source widely1',
    width = buttom_width, height = buttom_height,
    command=h1)
b1.pack(side='left')
b2 = tk.Button(frm_1,
    text='source widely2',
    width = buttom_width, height = buttom_height,
    command=h1)
b2.pack(side='left')
b3 = tk.Button(frm_1,
    text='XTC',
    width = button_width, height = button_height,
    command=h2,bg='yellow')
b3.pack(side='left')
b4 = tk.Button(frm_1,
    text='VS',
    width = button_width, height = button_height,
    command=h3,bg='yellow')
b4.pack(side='left')
def rock():
  fun3('rock');
def vocal():
  fun3('vocal');
def classic():
  fun3('classic');
def jazz():
  fun3('pop');
def raw():
  global output
  output=output/np.absolute(output).max();

b_eq1 = tk.Button( frm_2 , text = 'Raw' , width = button_width , height = button_height ,command=raw,bg='green')
b_eq2 = tk.Button( frm_2 , text = 'Rock' , width = button_width , height = button_height , command= rock,bg='green')
b_eq3 = tk.Button( frm_2 , text = 'Vocal' , width = button_width , height = button_height , command= vocal,bg='green')
b_eq4 = tk.Button( frm_2 , text = 'Classic' , width = button_width , height = button_height , command= classic,bg='green')
b_eq5 = tk.Button( frm_2 , text = 'Jazz' , width = button_width , height = button_height , command= jazz,bg='green')
b_eq1.pack(side = 'left');
b_eq2.pack(side = 'left');
b_eq3.pack(side = 'left');
b_eq4.pack(side = 'left');
b_eq5.pack(side = 'left');




window.mainloop()
