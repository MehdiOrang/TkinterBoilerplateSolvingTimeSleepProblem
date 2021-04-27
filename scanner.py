import tkinter.font as tkFont
import tkinter as tk
import threading
import time
import os
from tkinter import messagebox as mb

class Transix(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
#         tk.Tk.wm_title(self,"Smart University")
        tk.Tk.overrideredirect(self,True)
        screen_width = tk.Tk.winfo_screenwidth(self)
        screen_height = tk.Tk.winfo_screenheight(self)
        window_height = 580
        window_width = 400
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        tk.Tk.geometry(self,"{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        frame = StartPage(container,self)
        self.frames[StartPage] = frame
        frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        label = tk.Label(
                    self,
                    text= "WELCOME TO TRANSIX",
                    foreground="orange",  # Set the text color to white
                    background="black" ,  # Set the background color to black
                    width=50,
                    height=5,
                    )
        label.pack()

        label_main = tk.Label(
                    self,
                    text="Please Tap Your Card",
                    foreground="Black",  # Set the text color to white
                    background="SteelBlue1" ,  # Set the background color to black
                    width=50,
                    height=20,
                    font=fontStyle
            )
        label_main.pack()
        
        myEntry = tk.Entry(self, show='*')
        myEntry.focus()
        myEntry.bind("<Return>",lambda x: returnEntry())
        myEntry.pack()
        def make_it_blue():
            label_main.config(background='SteelBlue1')
            fontStyle.configure(size=20)
            label_main.config(text="PLEASE TAP YOUR CARD")

        def returnEntry(arg=None):
            """Gets the result from Entry and return it to the Label"""
            t2 = threading.Timer(2, make_it_blue)

            id_number = myEntry.get()
            myEntry.delete(0,'end')
            if int(id_number) == 1:
                os.system("afplay beep-06.wav&")
                label_main.config(background='Green2')
                label_main.config(text='✅')
                fontStyle.configure(size=90)
            else: 
                os.system("afplay beep-05.wav&")
                label_main.config(background='Red2')
                label_main.config(text='⛔')
                fontStyle.configure(size=90)
            t2.start()

if __name__ == "__main__":
    app = Transix()
    app.overrideredirect(0)
    app.mainloop()