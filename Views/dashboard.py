import tkinter as tk 
from tkinter import ttk 
import customtkinter as ctk
from PIL import Image , ImageTk

## importimg file to show the application in the taskbar : 
from ctypes import windll


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
        self.dashboard.overrideredirect(True)

        ## Variables for the app min max 
        self.zoomed  = False
        self.minimized  = False
        self.dashboard.wm_iconbitmap(r'Views\app_icon.ico')


        
    # using this function for making the icon in the taskbar : 
    def set_appwindow(self ,root):
        GWL_EXSTYLE=-20
        WS_EX_APPWINDOW=0x00040000
        WS_EX_TOOLWINDOW=0x00000080
        hwnd = windll.user32.GetParent(root.winfo_id())
        style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        style = style & ~WS_EX_TOOLWINDOW
        style = style | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
        root.wm_withdraw()
        root.after(10, lambda: root.wm_deiconify())

    def close_app(self):
        self.dashboard.destroy()
    
    def max_app(self):
        if self.zoomed  == False:
            self.dashboard.state('zoomed')
            self.zoomed = True
            self.max_button.configure(text=u"\U0001F5D7")
        else:
            self.zoomed = False
            self.dashboard.state('normal')
            self.max_button.configure(text=u"\U0001F5D6")

    def min_app(self):
        self.dashboard.overrideredirect(False)
        self.dashboard.wm_iconify()
        self.dashboard.bind('<FocusIn>' , self.on_deiconify)
        

    def on_deiconify(self, event):
        if self.dashboard.wm_state() =='normal' and self.dashboard.overrideredirect() != True:
            self.dashboard.overrideredirect(True)
            self.set_appwindow(self.dashboard)

    def mouse_click(self, event):
        self.x  = event.x
        self.y = event.y
    
    def mouse_move(self ,  event ):
        self.deltax = event.x - self.x 
        self.deltay = event.x   - self.y
        self.dashboard.geometry(f'{self.width}x{self.height}')

    def defining_controls(self):
        ## titlebar and close button 
        self.titlebar = tk.Frame(self.dashboard , height=15 , background=colors.black_color)
        self.close_button  = tk.Button(self.titlebar  , text='\u2716', command=self.close_app)
        self.max_button  = tk.Button(self.titlebar , text=u"\U0001F5D6" , command=self.max_app)
        self.min_button = tk.Button(self.titlebar , text='\u2014', command=self.min_app)
        ## Side bar and Icon for sidebar ( Avatar )



    def placing_controls(self):
        # Placing the titlebar close min and max button
        self.titlebar.pack(side='top' , fill='x')
        self.close_button.pack(side='right')
        self.max_button.pack(side='right')
        self.min_button.pack(side='right')
        self.dashboard.after(10, lambda: self.set_appwindow(self.dashboard))
        ## Calling the main app
        self.dashboard.mainloop()



if __name__ == '__main__':
    main_dashb = Dashboard(1200 ,600)
    main_dashb.defining_controls()
    main_dashb.placing_controls()



