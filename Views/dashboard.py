import tkinter as tk 
from tkinter import ttk 
import customtkinter as ctk
from PIL import Image , ImageTk

# Importimg file to show the application in the taskbar : 
from ctypes import windll

# Importing Custom files  
import colors
import styles
import ui_functions


class Dashboard():

    def __init__(self , width , height) -> None:
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

        # Importing image for the buttons and icons
        self.dashboard.wm_iconbitmap(r'Views\app_icon.ico')
        home_icon  = Image.open(r'Assets\icons\home.png')
        settings_icon  = Image.open(r'Assets\icons\settings.png')
        history_icon = Image.open(r'Assets\icons\history.png')
        betting_icon  = Image.open(r'Assets\icons\betting.png')
        betting_resized   = betting_icon.resize((15,15))
        home_resized  = home_icon.resize((15,15))
        history_resized  = history_icon.resize((15,15))
        settings_resized = settings_icon.resize((15,15))
        self.home_icon  = ImageTk.PhotoImage(home_resized)
        self.settings_icon  = ImageTk.PhotoImage(settings_resized) # using the unicode character for settings now will be replaced later.
        self.history_icon  =ImageTk.PhotoImage(history_resized)
        self.betting_icon  = ImageTk.PhotoImage(betting_resized)

        ## Images for the User Icon : Default Icon 
        image_icon  = Image.open(r'Assets\user_avatars\panda.png')
        image_icon_resized  = image_icon.resize((50,50))
        self.imgae_icon  = ImageTk.PhotoImage(image_icon_resized)
        self.user_image_label = tk.Label(self.upper_frame , image=self.imgae_icon) # Will be used to show the dummy image for the user for now : Will be changed with the database later 
        
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

    def mouse_move(self, event):
        self.delta_x  = event.x  - self.x 
        self.delta_y =  event.y - self.y 
        self.new_x  = self.dashboard.winfo_x() + self.delta_x
        self.new_y = self.dashboard.winfo_y() + self.delta_y
        self.dashboard.geometry(f"{self.width}x{self.height}+{self.new_x}+{self.new_y}")

    def open_Close_sidebar(self):
        if self.sidebar_frame.winfo_width() == 100:
            self.sidebar_frame.configure(width=230)
            self.open_close_button.configure(text="\u00AB")
        else:
            self.sidebar_frame.configure(width=100)
            self.open_close_button.configure(text="\u00BB")


    

    ## UI Design part
    def defining_controls(self):
        ## Titlebar and close button 
        self.titlebar = tk.Frame(self.dashboard , height=15 , background=colors.black_color)
        self.close_button  = tk.Button(self.titlebar  , text='\u2716', command=self.close_app)
        self.max_button  = tk.Button(self.titlebar , text=u"\U0001F5D6" , command=self.max_app)
        self.min_button = tk.Button(self.titlebar , text='\u2014', command=self.min_app)
        # Sidebar and open Close button
        self.sidebar_frame  = tk.Frame(self.dashboard , width=100 )
        self.sidebar_frame.pack_propagate(0)
        
        # Controls inside sidebar
        self.application_label  = tk.Label(self.sidebar_frame , text="Investify")
        self.sidebar_user_frame   =tk.Frame(self.sidebar_frame)
        name_image  = Image.open(r'Assets\user_avatars\avataer_man.png')
        name_resized = name_image.resize((50 , 50))
        self.name_image  = ImageTk.PhotoImage(name_resized)
        self.user_image  = tk.Label(self.sidebar_user_frame , image=self.name_image)
        self.user_image_name  = tk.Label(self.sidebar_user_frame , text="Username")
        ## Creating seperate Frames with the Images and Buttons inside the Sidebar Frame : Dashboard to history buttons etc.
        self.dashboard_frame  = tk.Frame(self.sidebar_frame)
        self.betting_frame  = tk.Frame(self.sidebar_frame)
        self.history_frame  = tk.Frame(self.sidebar_frame)

        self.home_icon_label  = tk.Label(self.dashboard_frame , image=self.home_icon)
        self.betting_icon_label  = tk.Label(self.betting_frame , image=self.betting_icon)
        self.history_icon_label  =tk.Label(self.history_frame ,image=self.history_icon)


        self.dashboard_button  = tk.Button(self.dashboard_frame , text="Dashboard")
        self.betting_button  = tk.Button(self.betting_frame , text="Betting")
        self.history_button  = tk.Button(self.history_frame , text="History")


        
        # Open close button and settings button  : 
        self.open_close_button = tk.Button(self.sidebar_frame , text="\u00BB" , command=self.open_Close_sidebar)
        self.settings_button  = tk.Button(self.sidebar_frame , text="\u2699")


        ## Upper frame where the user icon with the username and the arrow icon will be shown : 
        self.upper_frame  = tk.Frame(self.dashboard)
        self.upper_frame_shadow  = tk.Frame(self.dashboard)
        self.upper_frame.pack_propagate(1)
        
        self.username_frame  = tk.Frame(self.upper_frame)



        # Configuring the controls : 
        self.sidebar_frame.configure(background='blue')
        desired_height  = int(self.dashboard.winfo_height() * 0.05)
        self.upper_frame.configure(background='red' ,height=desired_height)

        # Binding Controls 
        self.titlebar.bind("<ButtonPress-1>" , self.mouse_click)
        self.titlebar.bind("<B1-Motion>" , self.mouse_move)


    def placing_controls(self):
        # Placing the titlebar close min and max button
        self.titlebar.pack(side='top' , fill='x')
        self.close_button.pack(side='right')
        self.max_button.pack(side='right')
        self.min_button.pack(side='right')
        self.dashboard.after(10, lambda: self.set_appwindow(self.dashboard))


        # Placing sidebar 
        self.sidebar_frame.pack(side='left' , fill='y')

        self.application_label.pack(side='top' , pady=(10,0))
        self.sidebar_user_frame.pack(side='top' , pady=(10,0))
        self.user_image.pack()
        self.user_image_name.pack(side='top' , pady=(10,0))
        # Placing the Frames and the Buttons inside the sidebar :  
        
        self.dashboard_frame.pack(side='top' , pady=(10,0)) 
        self.home_icon_label.pack(side='left')
        self.dashboard_button.pack(side='right')

        self.betting_frame.pack(side='top' , pady=(0,0))
        self.betting_icon_label.pack(side='left')
        self.betting_button.pack(side='right')

        self.history_frame.pack(side='top')
        self.history_icon_label.pack(side='left')
        self.history_button.pack(side='right')

       # Placing the upper control : 
        self.upper_frame.pack(side='top' , fill='x')
       # Settings and Open close button :
        self.open_close_button.pack(side='bottom' ,  anchor=tk.SE , padx=(2,2) , pady=(0,2))
        self.settings_button.pack(side='bottom' , anchor=tk.SE , padx=(2,2) , pady=(0 ,2))

        
 
        
        ## Calling the main app
        self.dashboard.mainloop()



if __name__ == '__main__':
    main_dashb = Dashboard(1000 ,700)
    main_dashb.defining_controls()
    main_dashb.placing_controls()



