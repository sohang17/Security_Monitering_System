from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import * 
import customtkinter
import mian_window
import test

w=customtkinter.CTk(fg_color='#153749')
w.title("security monitering")
# w.geometry('427x250')


width_of_window=600
height_of_window=175
screen_width=w.winfo_screenwidth()
screen_height=w.winfo_screenheight()
x_coordinate=(screen_width/2)-(width_of_window/2)
y_coordinate=(screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))


frame = customtkinter.CTkFrame(master=w,height=300,width=300,fg_color='#153749')
frame.pack(fill=X)

s=ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar",foreground='red',background='green')
progress=Progressbar(master=frame,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate')



# # main_window()
def bar():
    lab1 = customtkinter.CTkLabel(master=frame,fg_color='#153749',text="Scanning...",justify='center')
    lab1.pack(pady=(10,10))
  
   

    import time
    r=0
    for i in range(110):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
    w.destroy()
    mian_window.mainWindow()


# #lables

lab2 = customtkinter.CTkLabel(master=frame,text='Security Monitering',fg_color='#153749',bg_color='white',font=customtkinter.CTkFont('Calibri (body)',40))
lab2.pack()

lab3 = customtkinter.CTkLabel(master=frame,text='System',fg_color='#153749',bg_color='white',font=customtkinter.CTkFont('Calibri (body)',40))
lab3.pack()

getstart = customtkinter.CTkButton(master=frame,text='Start Scanning',command=bar)
getstart.pack(fill=Y)

progress.pack(fill= X)
w.mainloop()