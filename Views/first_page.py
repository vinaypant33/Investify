import tkinter as tk
from tkinter import ttk
from typing import Any
import customtkinter as ctk
from PIL import Image ,  ImageTk
import styles
import colors

class login_page():

    def __init__(self , width , height ) -> None:
        self.login_page  = tk.Tk()
        self.current_width  = self.login_page.winfo_screenwidth()
        self.current_height  = self.login_page.winfo_screenheight()
        self.width  = width
        self.height = height
        self.x_location  = (self.current_width //2 ) - (self.width // 2)
        self.y_location  = (self.current_height //2) - (self.height // 2)
        self.login_page.geometry(f'{self.width}x{self.height}+{self.x_location}+{self.y_location}')
        self.login_page.overrideredirect(True)

        # Importing the image and resizing it :  
        fingerprint = Image.open(r'Assets\fingerprint.png')
        fingerprint_1 = fingerprint.resize((50,50))
        self.fingerprint2 = ImageTk.PhotoImage(fingerprint_1)
        
    ## Functions for the basic working 

    def mouse_click(self , event):
        self.x  = event.x
        self.y = event.y
    
    def mouse_move(self, event):
        self.deltax = event.x - self.x
        self.deltay = event.y - self.y
        self.x_coordinate  = self.login_page.winfo_x() + self.deltax
        self.y_coordinate  = self.login_page.winfo_y() +  self.deltay
        self.login_page.geometry(f'{self.width}x{self.height}+{self.x_coordinate}+{self.y_coordinate}')

    def close_app(self):
        self.login_page.destroy()

    def defining_controls(self):
        self.titlebar = tk.Frame(self.login_page)
        self.close_button  = tk.Button(self.titlebar , text=' X ' , command=self.close_app)
        self.finger_print_image = tk.Label(self.login_page , image=self.fingerprint2 , background=colors.black_color)
        ## Configuring the Controls : 
        self.login_page.configure(background=colors.black_color)
        self.titlebar.configure(styles.login_page_design.frame_styles(self , self.titlebar , 100 , 16 , colors.black_color))
        self.close_button.configure(styles.login_page_design.button_styles_close(self , self.close_button , 2  , 1 , colors.red_color , colors.white_color ))
        ## Binding the controls  : 
        self.titlebar.bind("<ButtonPress-1>" , self.mouse_click)
        self.titlebar.bind("<B1-Motion>" , self.mouse_move)

    def placing_controls(self):
        self.titlebar.pack(side='top' , fill='x')
        self.close_button.pack(side='right' , padx=(5,0))
        self.finger_print_image.pack(side='top' , pady=(10,10))
        # Main App  : 
        self.login_page.mainloop()



if __name__ =='__main__':
    login = login_page(350 , 500)
    login.defining_controls()
    login.placing_controls()
