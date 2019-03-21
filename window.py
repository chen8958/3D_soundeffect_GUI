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

  output5=np.convolve(original_data[1,:],filter_data1);

  output6=np.convolve(original_data[1,:],filter_data2);

  output7=np.convolve(original_data[1,:],filter_data3);

  output8=np.convolve(original_data[1,:],filter_data4);


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




  sink1=output1+output5+output9+output17;
  sink2=output2+output6+output10+output18;
  sink3=output3+output7+output11+output19;
  sink4=output4+output8+output12+output20;
  global output
  output=np.array([sink1,sink2,sink3,sink4]);
  output=output/np.absolute(output).max();
  output=output.T;









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












#tk.Label(frm_l, text='output_file name').pack()
#e_outputfile = tk.Entry(frm_l)
#e_outputfile.pack()
def play():
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
buttom_width=9;
buttom_height=2;

original = tk.Button(frm_1, 
    text='origianl sound',      
    width = buttom_width, height = buttom_height, 
    command=play_original)     
original.pack(side='left') 
b_play = tk.Button(frm_3, 
    text='play',      
    width = buttom_width, height = buttom_height, 
    command=play)     
b_play.pack(side='left') 
b_stop = tk.Button(frm_3, 
    text='stop',      
    width = buttom_width, height = buttom_height, 
    command=stop)     
b_stop.pack(side='left')
b1 = tk.Button(frm_1, 
    text='source widely',      
    width = buttom_width, height = buttom_height, 
    command=h1)     
b1.pack(side='left')
b2 = tk.Button(frm_1, 
    text='source widely',      
    width = buttom_width, height = buttom_height, 
    command=h3)     
b2.pack(side='left')
b3 = tk.Button(frm_1, 
    text='XTC',      
    width = buttom_width, height = buttom_height, 
    command=h2)     
b3.pack(side='left')
b4 = tk.Button(frm_1, 
    text='VS',      
    width = buttom_width, height = buttom_height, 
    command=h3)     
b4.pack(side='left')

b_eq1 = tk.Button( frm_2 , text = 'Raw' , width = buttom_width , height = buttom_height , command= h1)
b_eq2 = tk.Button( frm_2 , text = 'Rock' , width = buttom_width , height = buttom_height , command= h1)
b_eq3 = tk.Button( frm_2 , text = 'Vocal' , width = buttom_width , height = buttom_height , command= h1)
b_eq4 = tk.Button( frm_2 , text = 'Classic' , width = buttom_width , height = buttom_height , command= h1)
b_eq5 = tk.Button( frm_2 , text = 'Jazz' , width = buttom_width , height = buttom_height , command= h1)
b_eq1.pack(side = 'left');
b_eq2.pack(side = 'left');
b_eq3.pack(side = 'left');
b_eq4.pack(side = 'left');
b_eq5.pack(side = 'left');


   

window.mainloop()

