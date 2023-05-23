import tkinter as tk 
from tkinter import ttk 
import customtkinter as ctk
from PIL import Image , ImageTk

# Importing Custom files  
import colors
import styles



class Dashboard():

    def __init__(self , width , height ) -> None:
        self.dashboard  = tk.Tk()
        self.width  = width 
        self.height  = height
        self.current_width  = self.dashboard.winfo_screenwidth()
        self.current_height  =self.dashboard.winfo_screenheight()
        self.x_location  = (self.current_width //2 ) - (self.width // 2)
        self.y_location  = (self.current_height //2) - (self.height //2)
        self.dashboard.geometry(f'{self.width}x{self.height}+{self.x_location}+{self.y_location}')
        # self.dashboard.overrideredirect(True)

    
    def defining_controls(self):
        pass

    def placing_controls(self):


        ## Calling the main app
        self.dashboard.mainloop()



if __name__ == '__main__':
    main_dashb = Dashboard(1200 ,600)
    main_dashb.defining_controls()
    main_dashb.placing_controls()



