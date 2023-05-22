import tkinter as tk
from tkinter import ttk
from typing import Any
import customtkinter as ctk
from PIL import Image ,  ImageTk
import styles
import colors


## Importing custom tkinter for the rounded buttons : 
import customtkinter as ctk



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
        fingerprint_1 = fingerprint.resize((60,60))
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

    def hoovering_textboxes(self , master):
        master.configure(foreground=colors.white_color)
        master.delete(0 , 'end')
        if master == self.password_text:
            master.configure(show="*")

        ## Functions for Hovering the controls : Button Controls
    def hover_in_controls_button(self , master):
        master.configure(background=colors.hoovered_red)
        
    def hover_out_controls_button(self , master):
        master.configure(background=colors.red_color)

    def hover_in_controls_foregorund(self, master ,  color):
        master.configure(foreground = color)
    
    def hover_out_controls_foreground(self, master , color):
        master.configure(foreground  = color)
    

    def defining_controls(self):
        self.titlebar = tk.Frame(self.login_page)
        self.close_button  = tk.Button(self.titlebar , text=' X ' , command=self.close_app)
        self.finger_print_image = tk.Label(self.login_page , image=self.fingerprint2 , background=colors.black_color)
        # Setting up the Username and Password : 
        self.username_text  = tk.Entry(self.login_page)
        self.username_bottom_border = tk.Frame(self.login_page , height=2 , background=colors.white_color)
        self.password_text  = tk.Entry(self.login_page)
        self.password_bottom_border = tk.Frame(self.login_page , height=2 , background=colors.white_color)
        self.login_button  = tk.Button(self.login_page , text="Login")
        self.forgot_password  = tk.Label(self.login_page , text="Forgot Password ?")
        self.sign_in_text  = tk.Label(self.login_page , text="Don't Have an account ?")
        self.sign_in_ = tk.Label(self.login_page , text="Sign In")

        ## Configuring the Controls : 
        self.login_page.configure(background=colors.black_color)
        self.titlebar.configure(styles.login_page_design.frame_styles(self , self.titlebar , 100 , 16 , colors.black_color))
        self.close_button.configure(styles.login_page_design.button_styles_close(self , self.close_button , 2  , 1 , colors.red_color , colors.white_color  , colors.black_color , colors.white_color))
        self.username_text.configure(styles.login_page_design.text_box_configure(self , self.username_text , colors.black_color , colors.grey_color))
        self.username_text.configure(cursor='circle')
        self.username_text.insert(0 , "Username")
        self.password_text.configure(styles.login_page_design.text_box_configure(self,  self.password_text , colors.black_color , colors.grey_color))
        self.password_text.insert(0 , "Password")
        self.password_text.configure(cursor='circle')
        self.login_button.configure(styles.login_page_design.button_styles_close(self , self.login_button , 100 , 1 , colors.red_color , colors.white_color , colors.white_color  , colors.black_color))
        self.login_button.configure(font = styles.large_font_bold)
        self.forgot_password.configure(background=colors.black_color , foreground=colors.white_color)
        self.sign_in_.configure(background=colors.black_color , foreground=colors.white_color)
        self.sign_in_text.configure(background=colors.black_color , foreground=colors.white_color)
        ## Binding the controls  : 
        self.titlebar.bind("<ButtonPress-1>" , self.mouse_click)
        self.titlebar.bind("<B1-Motion>" , self.mouse_move)
        self.username_text.bind("<FocusIn>" ,lambda event  :self.hoovering_textboxes(self.username_text))
        self.password_text.bind("<FocusIn>" , lambda event : self.hoovering_textboxes(self.password_text))
        self.login_button.bind("<Enter>" ,lambda event  :  self.hover_in_controls_button(self.login_button))
        self.login_button.bind("<Leave>" , lambda event :  self.hover_out_controls_button(self.login_button))
        self.sign_in_.bind("<Enter>" , lambda event :  self.hover_in_controls_foregorund(self.sign_in_ , colors.red_color))
        self.sign_in_.bind("<Leave>" , lambda event : self.hover_out_controls_foreground(self.sign_in_ , colors.white_color))
        self.forgot_password.bind("<Enter>" , lambda event : self.hover_in_controls_foregorund(self.forgot_password , colors.red_color))
        self.forgot_password.bind("<Leave>" , lambda event : self.hover_out_controls_foreground(self.forgot_password , colors.white_color))


    def placing_controls(self):
        self.titlebar.pack(side='top' , fill='x')
        self.close_button.pack(side='right' , padx=(5,0))
        self.finger_print_image.pack(side='top' , pady=(50,10))
        self.username_text.pack(side='top' , pady=(50,0) , fill='x' , padx=(15,15))
        self.username_bottom_border.pack(side='top' , padx=(15,15) , pady=(0 , 10) , fill='x')
        self.password_text.pack(side='top' , pady=(10,0) , fill='x' , padx=(15,15))
        self.password_bottom_border.pack(side='top' , padx=(15,15) , pady=(0 , 10) , fill='x')
        self.login_button.pack(side = 'top' , pady = (0 , 0) , padx = (15 , 15) , fill ='x')
        self.forgot_password.pack(side='left' , pady=(2,2) , padx=(10,10))
        self.sign_in_text.pack(side='left', pady=(2,2) , padx=(40,0))
        self.sign_in_.pack(side='left' , padx=(0,10) , pady=(0, 0))


        # Main App  : 
        self.login_page.mainloop()


class register_page():

    def __init__(self, width, height) -> None:
        self.register_page  = tk.Tk()
        self.height = height
        self.width = width
        self.current_width = self.register_page.winfo_screenwidth()
        self.current_height   = self.register_page.winfo_screenheight()
        self.x_location  = (self.current_width //2 ) - (self.width // 2)
        self.y_location  = (self.current_height //2) - (self.height // 2)
        self.register_page.geometry(f'{self.width}x{self.height}+{self.x_location}+{self.y_location}')
        self.register_page.overrideredirect(True)

    # basic Functions for the Movement 
    def mouse_click(self, event ):
        self.x = event.x
        self.y = event.y

    def move_window(self , event):
        self.deltax = event.x - self.x 
        self.deltay = event.y - self.y
        self.x_coordinate  = self.register_page.winfo_x() + self.deltax
        self.y_coordinate  = self.register_page.winfo_y() + self.deltay
        self.register_page.geometry(f'{self.width}x{self.height}+{self.x_coordinate}+{self.y_coordinate}')


    
    def defining_controls(self):
        # Upper Controls : Title bar and closing button
        self.titlebar  = tk.Frame(self.register_page , height=18)
        self.close_button  = tk.Button(self.register_page)

        # configuring the Controls
        self.titlebar.configure(background=colors.black_color)
        self.register_page.configure(background=colors.black_color)
        # Binding the controls 
        self.titlebar.bind("<ButtonPress-1>" , self.mouse_click)
        self.titlebar.bind("<B1-Motion>" , self.move_window)

    def placing_controls(self):
        ## Placing titlebar and closing button
        self.titlebar.pack(side='top' ,fill='x')

        ## Calling the Main register page 
        self.register_page.mainloop()

        

if __name__ =='__main__':
    # login = login_page(350 , 420)
    # login.defining_controls()
    # login.placing_controls()
    register =register_page(350 , 420)
    register.defining_controls()
    register_page.placing_controls(register)
