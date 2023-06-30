import tkinter as tk
from tkinter import ttk 
import customtkinter as ctk
from PIL import Image, ImageTk
import colors
import fonts



is_running  =False


class mini_menu():
    def __init__(self) -> None:
        self.main_app = tk.Tk()
        self.main_app.configure(height=300,  width=300)
        self.master_frame = tk.Frame(self.main_app) 

        # self.main_app.overrideredirect(True)
        
        # Importing Image's : 
        # User Image
        user_image  = Image.open(r'Assets\user_avatars\panda.png')
        user_image_resized  = user_image.resize((25,25))
        self.user_image_icon  = ImageTk.PhotoImage(user_image_resized)

        # Settings :  
        settings  = Image.open(r'Assets\icons\settings_white.png')
        settings_resized  = settings.resize((25,25))
        self.settings_icon  = ImageTk.PhotoImage(settings_resized)

        # Logout Icon : 
        logout  = Image.open(r'Assets\icons\logout_white.png')
        logout_resized  = logout.resize((25,25))
        self.logout_icon  = ImageTk.PhotoImage(logout_resized)


        # Master Frame for the main App: app size same as the frame size
        self.master_frame.configure(height=150 , width=120 , border=2 , borderwidth=2 , background=colors.white_color )
        self.master_frame.pack_propagate(0)


        # User name and the User Image Icon
        self.user_frame  = tk.Frame(self.master_frame , width=150 ,height=30  , background=colors.grey_color_2)
        self.user_frame.pack_propagate(0)
        self.user_image   =tk.Label(self.user_frame , image=self.user_image_icon  , background=colors.grey_color_2)
        self.user_name  = tk.Label(self.user_frame ,  text="Username"  , background=colors.grey_color_2 , foreground=colors.white_color)

        self.settings_frame  = tk.Frame(master=self.master_frame , width=150 , height=30 , background=colors.grey_color_2)
        self.settings_frame.pack_propagate(0)

        self.settings_image  = tk.Label(self.settings_frame , image=self.settings_icon , background=colors.grey_color_2)
        self.settings_name  = tk.Label(self.settings_frame , text="Settings" , background=colors.grey_color_2 , foreground=colors.white_color)

        self.logout_frame = tk.Frame(self.master_frame , width=150 , height=30 , background=colors.grey_color_2)
        self.logout_frame.pack_propagate(0)
        self.logout_image  = tk.Label(self.logout_frame  , image=self.logout_icon , background=colors.grey_color_2)
        self.logout_name  =tk.Label(self.logout_frame , text="Logout" , background=colors.grey_color_2 , foreground=colors.white_color)


        # Packing all controls : 

        self.master_frame.pack()


        self.user_frame.pack(pady=(10,0))
        self.user_image.pack(side='left' , padx=(5,5))
        self.user_name.pack(side='right' , padx=(5,5))

        self.settings_frame.pack(pady=(0,0))
        self.settings_image.pack(side='left' , padx=(5,5))
        self.settings_name.pack(side='right' , padx=(5,5))

        self.logout_frame.pack(pady=(0,0))
        self.logout_image.pack(side='left' , padx=(5,5))
        self.logout_name.pack(side='right' , padx=(5,5))

        ## Binding for closing the app  : later will change the code for closing the main Dashboard also  : 
        self.logout_frame.bind("<Button-1>" , self.closing_app)
        self.logout_image.bind("<Button-1>" , self.closing_app)
        self.logout_name.bind("<Button-1>" , self.closing_app)

        ## Binding to show Hover controls  : 

        self.logout_frame.bind("<Enter>" , lambda event : self.logout_name.configure(foreground=colors.red_color))
        self.logout_frame.bind("<Leave>" , lambda event : self.logout_name.configure(foreground=colors.white_color))
        self.settings_frame.bind("<Enter>" , lambda event : self.settings_name.configure(foreground=colors.red_color))
        self.settings_frame.bind("<Leave>" , lambda event : self.settings_name.configure(foreground=colors.white_color))
        self.user_frame.bind("<Enter>" , lambda event : self.user_name.configure(foreground=colors.red_color))
        self.user_frame.bind("<Leave>" , lambda event : self.user_name.configure(foreground=colors.white_color))

        
        self.main_app.mainloop()
    
    def closing_app(self , event):
        self.main_app.destroy()

        


if __name__  == '__main__':
    app = mini_menu()
