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
import fonts


class Dashboard():

    def __init__(self , width , height) -> None:
        self.dashboard  = tk.Tk()
        self.dashboard.configure(background=colors.white_color)
        self.width  = width 
        self.height  = height
        self.current_width  = self.dashboard.winfo_screenwidth()
        self.current_height  =self.dashboard.winfo_screenheight()
        self.x_location  = (self.current_width //2 ) - (self.width // 2)
        self.y_location  = (self.current_height //2) - (self.height //2)
        self.dashboard.geometry(f'{self.width}x{self.height}+{self.x_location}+{self.y_location}')
        self.dashboard.overrideredirect(True)
        self.sidebar_current_width  = 0

        ## Variables for the app min max 
        self.zoomed  = False
        self.minimized  = False

        # Importing image for the buttons and icons
        self.dashboard.wm_iconbitmap(r'Views\app_icon.ico')
        home_icon  = Image.open(r'Assets\icons\home.png')
        home_icon_red  = Image.open(r'Assets\icons\home_red.png')
        settings_icon  = Image.open(r'Assets\icons\settings.png')
        settings_icon_red = Image.open(r'Assets\icons\settings_red.png')
        history_icon = Image.open(r'Assets\icons\history.png')
        history_icon_red  = Image.open(r'Assets\icons\history_red.png')
        betting_icon  = Image.open(r'Assets\icons\betting.png')
        betting_icon_red = Image.open(r'Assets\icons\betting_red.png')
        betting_resized   = betting_icon.resize((15,15))
        home_resized  = home_icon.resize((20,20))
        history_resized  = history_icon.resize((15,15))
        settings_resized = settings_icon.resize((15,15))
        self.home_icon  = ImageTk.PhotoImage(home_resized)
        self.settings_icon  = ImageTk.PhotoImage(settings_resized) # using the unicode character for settings now will be replaced later.
        self.history_icon  =ImageTk.PhotoImage(history_resized)
        self.betting_icon  = ImageTk.PhotoImage(betting_resized)


        # Import the white images and resize them for the images : 
        white_home  = Image.open(r'Assets\icons\home_white.png')
        white_betting  = Image.open(r'Assets\icons\betting_white.png')
        white_history  = Image.open(r'Assets\icons\history_white.png')

        white_home_resized = white_home.resize((20,20))
        white_betting_resized  = white_betting.resize((20,20))
        white_history_resized  = white_history.resize((20,20))


        self.white_home = ImageTk.PhotoImage(white_home_resized)
        self.white_betting  = ImageTk.PhotoImage(white_betting_resized)
        self.white_history  = ImageTk.PhotoImage(white_history_resized)



        home_resized_large  = home_icon_red.resize((25 , 25))
        history_resized_large  = history_icon_red.resize((25 , 25))
        betting_resized_large  = betting_icon_red.resize((25 , 25))
        self.home_icon_large = ImageTk.PhotoImage(home_resized_large)
        self.betting_icon_large  = ImageTk.PhotoImage(betting_resized_large)
        self.history_icon_large  = ImageTk.PhotoImage(history_resized_large)
       
        ## Images for the User Icon : Default Icon 
        image_icon  = Image.open(r'Assets\user_avatars\panda.png')
        image_icon_resized_30  = image_icon.resize((30,30))
        self.username_imgae_icon_30  = ImageTk.PhotoImage(image_icon_resized_30)
        image_icon_resized_50 = image_icon.resize((50,50))
        self.username_image_icon_50 = ImageTk.PhotoImage(image_icon_resized_50)

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
            self.main_contents_frame.destroy()
            self.reducing_width = 100
            self.calling_dashboard(self.reducing_width)
        else:
            self.zoomed = False
            self.dashboard.state('normal')
            self.main_contents_frame.destroy()
            self.max_button.configure(text=u"\U0001F5D6")
            self.reducing_width = 100
            self.calling_dashboard(self.reducing_width)

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


    # Most important function for now : will have modify the same for now : 
    def open_Close_sidebar(self):
        
        if self.sidebar_frame.winfo_width() == 60:
            self.sidebar_frame.configure(width=120 , background=colors.dark_color_grey)
            self.reducing_width  = 120
            self.open_close_button.configure(text="\u00AB")
            self.sidebar_current_width = 120
            self.main_contents_frame.destroy()
            self.calling_dashboard(120)

            # Destroying the controls from sidebar large : 
            self.side_home_button.destroy()
            self.side_history_button.destroy()
            self.side_betting_button.destroy()

            self.sidebar_user_frame.destroy()
            # Calling the buttons and otehr controls here : 
            self.sidebar_user_frame   =tk.Frame(self.sidebar_frame , background=colors.dark_color_grey)
            self.user_image  = tk.Label(self.sidebar_user_frame , image=self.username_image_icon_50 , background=colors.dark_color_grey)
            self.user_image_name  = tk.Label(self.sidebar_user_frame , text="Username" , background=colors.dark_color_grey , foreground=colors.white_color)
            
            ## Creating seperate Frames with the Images and Buttons inside the Sidebar Frame : Dashboard to history buttons etc.

            self.dashboard_frame  = tk.Frame(self.sidebar_frame , width=120 , height=30 , background=colors.light_grey_color)
            self.dashboard_frame.pack_propagate(0)
            self.betting_frame  = tk.Frame(self.sidebar_frame , width=120 , height=30 , background=colors.light_grey_color)
            self.history_frame  = tk.Frame(self.sidebar_frame, width=120 , height=30 , background=colors.light_grey_color)
            self.betting_frame.pack_propagate(0)
            self.history_frame.pack_propagate(0)

            self.home_icon_label  = tk.Label(self.dashboard_frame , image=self.white_home , background=colors.light_grey_color)
            self.betting_icon_label  = tk.Label(self.betting_frame , image=self.white_betting ,  background=colors.light_grey_color)
            self.history_icon_label  =tk.Label(self.history_frame ,image=self.white_history ,  background=colors.light_grey_color)


            self.dashboard_button  = tk.Button(self.dashboard_frame , text="Dashboard")
            self.betting_button  = tk.Button(self.betting_frame , text="Betting")
            self.history_button  = tk.Button(self.history_frame , text="History")

            self.dashboard_button.configure(styles.login_page_design.button_styles_close(self , self.dashboard_button ,130 , None  , colors.light_grey_color , colors.white_color , colors.grey_color_2 , colors.red_color))
            self.betting_button.configure(styles.login_page_design.button_styles_close(self , self.betting_button ,130 , None  , colors.light_grey_color , colors.white_color , colors.grey_color_2 , colors.red_color))
            self.history_button.configure(styles.login_page_design.button_styles_close(self , self.history_button ,130 , None  , colors.light_grey_color , colors.white_color , colors.grey_color_2 , colors.red_color))


            # Packing the controls : 
            self.sidebar_user_frame.pack(side='top' , pady=(10,0))
            self.user_image.pack()
            self.user_image_name.pack(side='top' , pady=(10,0))
            # Placing the Frames and the Buttons inside the sidebar :  
    
            self.dashboard_frame.pack(side='top' , pady=(20,0)) 
            self.home_icon_label.pack(side='left' , padx=(3,3))
            self.dashboard_button.pack(side='right' , padx=(3,3))

            self.betting_frame.pack(side='top' , pady=(0,0))
            self.betting_icon_label.pack(side='left' , padx=(3,3))
            self.betting_button.pack(side='right' , padx=(3,3))

            self.history_frame.pack(side='top')
            self.history_icon_label.pack(side='left' , padx=(3,3))
            self.history_button.pack(side='right' , padx=(3,3))

            
        else:
            self.sidebar_frame.configure(width=60 , background=colors.dark_color_grey)
            self.sidebar_current_width = 60
            self.open_close_button.configure(text="\u00BB")
            self.main_contents_frame.destroy()
            self.reducing_width  = 60
            self.calling_dashboard(60)

            self.dashboard_frame.destroy()
            self.history_frame.destroy()
            self.betting_frame.destroy()
            self.sidebar_user_frame.destroy()

            self.sidebar_user_frame   =tk.Frame(self.sidebar_frame , background=colors.dark_color_grey)
            self.user_image  = tk.Label(self.sidebar_user_frame , image=self.username_image_icon_50 , background=colors.dark_color_grey)

            self.sidebar_user_frame.pack(side='top' , pady=(10,0))
            self.user_image.pack()

            self.side_home_button = tk.Button(self.sidebar_frame , image=self.home_icon_large)
            self.side_betting_button  = tk.Button(self.sidebar_frame , image=self.betting_icon_large )
            self.side_history_button  = tk.Button(self.sidebar_frame , image=self.history_icon_large)
            self.side_home_button.configure(styles.login_page_design.button_styles_close(self , self.side_home_button , 50 , 50 , colors.dark_color_grey , None , colors.grey_color_2 , None))
            self.side_betting_button.configure(styles.login_page_design.button_styles_close(self , self.side_betting_button , 50 , 50 , colors.dark_color_grey , None , colors.grey_color_2 , None))
            self.side_history_button.configure(styles.login_page_design.button_styles_close(self , self.side_history_button , 50 , 50 , colors.dark_color_grey , None , colors.grey_color_2 , None))

            self.side_home_button.bind("<Enter>" , lambda event : self.side_home_button.configure(background=colors.light_grey_color))
            self.side_home_button.bind("<Leave>" , lambda event  : self.side_home_button.configure(background=colors.dark_color_grey ))

            self.side_betting_button.bind("<Enter>" , lambda event : self.side_betting_button.configure(background=colors.light_grey_color ))
            self.side_betting_button.bind("<Leave>" , lambda event  : self.side_betting_button.configure(background=colors.dark_color_grey))

            self.side_history_button.bind("<Enter>" , lambda event : self.side_history_button.configure(background=colors.light_grey_color))
            self.side_history_button.bind("<Leave>" , lambda event  : self.side_history_button.configure(background=colors.dark_color_grey ))

            self.side_home_button.pack(side='top' , pady=(20 , 0))
            self.side_betting_button.pack(side='top' , pady=(0 , 0))
            self.side_history_button.pack(side='top' , pady=(0 , 0))
        

    def name(self):
        print(self.app_height)
        print(self.app_width)

    
    def calling_dashboard(self , reducing_height):
        # getting the height of the form and the width of the form : 
        self.app_height  = self.dashboard.winfo_height()
        self.app_width  = self.dashboard.winfo_width()
        self.main_contents_frame  = tk.Frame(self.dashboard , background=colors.light_grey_color  , height=self.app_height , width  = self.app_width)
        self.main_contents_frame.pack_propagate(0)
        self.current_dashboard  = ui_functions.Dashboard_controls(self.main_contents_frame , self.app_width, self.app_height , width_to_reduce=reducing_height)
        self.current_dashboard.configuring()
        self.current_dashboard.packing()

        self.main_contents_frame.pack(side='left' , padx=(0,0) , pady=(0,0))
        

    ## UI Design part
    def defining_controls(self):
        ## Titlebar and close button 
        self.titlebar = tk.Frame(self.dashboard , height=15 , background=colors.dark_color_grey)
        self.close_button  = tk.Button(self.titlebar  , text='\u2716', command=self.close_app)
        self.max_button  = tk.Button(self.titlebar , text=u"\U0001F5D6" , command=self.max_app)
        self.min_button = tk.Button(self.titlebar , text=u'\u2014', command=self.min_app)
        # Sidebar and open Close button
        self.sidebar_frame  = tk.Frame(self.dashboard , width=60 , background=colors.dark_color_grey)
        self.sidebar_frame.pack_propagate(0)
        # Controls inside sidebar
        # Open close button and settings button  : 
        self.open_close_button = tk.Button(self.sidebar_frame , text="\u00BB" , command=self.open_Close_sidebar , font=fonts.small_font_bold)
        self.settings_button  = tk.Button(self.sidebar_frame , text="\u2699" , font=fonts.small_font_bold)
        ## Upper frame where the user icon with the username and the arrow icon will be shown : 
        self.upper_frame  = tk.Frame(self.dashboard )
        self.upper_frame_shadow  = tk.Frame(self.dashboard)
        self.upper_frame.pack_propagate(1)
        self.username_frame  = tk.Frame(self.upper_frame , background=colors.light_grey_color)
        self.user_image_label = tk.Label(self.username_frame , image=self.username_imgae_icon_30 , background=colors.light_grey_color) # Will be used to show the dummy image for the user for now : Will be changed with the database later 
        self.user_name_label = tk.Label(self.username_frame , text="Username" , background=colors.light_grey_color ,foreground=colors.white_color)
        self.down_button  =tk.Button(self.username_frame , text=u"\u25BC")
        ## controls for the dashboard : They will be loaded in the default and then will be changed dynamically as the button works 
        # Frame in the dashboard with the color and under that frame the contents to be loaded : 
        # getting the height of the form and the width of the form : 
        self.app_height  = self.dashboard.winfo_height()
        self.app_width  = self.dashboard.winfo_width()
        self.main_contents_frame  = tk.Frame(self.dashboard , background=colors.light_grey_color  , height=self.app_height , width  = self.app_width)
        self.main_contents_frame.pack_propagate(0)
        self.current_dashboard  = ui_functions.Dashboard_controls(self.main_contents_frame , self.app_width, self.app_height )
        self.current_dashboard.configuring()
        self.current_dashboard.packing()
        self.sidebar_user_frame   =tk.Frame(self.sidebar_frame , background=colors.dark_color_grey)
        self.user_image  = tk.Label(self.sidebar_user_frame , image=self.username_image_icon_50 , background=colors.dark_color_grey)
        self.side_home_button = tk.Button(self.sidebar_frame , image=self.home_icon_large)
        self.side_betting_button  = tk.Button(self.sidebar_frame , image=self.betting_icon_large )
        self.side_history_button  = tk.Button(self.sidebar_frame , image=self.history_icon_large)
    
        # Configuring the controls : 
        # The upper controls and Upper titleba : 
        self.close_button.configure(styles.login_page_design.button_styles_close(self ,  self.close_button , 4, None , colors.dark_color_grey , colors.red_color , colors.red_color , colors.black_color))
        self.max_button.configure(styles.login_page_design.button_styles_close(self ,  self.max_button , 4, None , colors.dark_color_grey , colors.red_color , colors.red_color , colors.black_color))
        self.min_button.configure(styles.login_page_design.button_styles_close(self ,  self.min_button , 4, None , colors.dark_color_grey , colors.red_color , colors.red_color , colors.black_color))
        desired_height  = int(self.dashboard.winfo_height() * 0.05)
        self.upper_frame.configure(background=colors.light_grey_color  , height=desired_height)
        self.down_button.configure(background=colors.light_grey_color , relief='flat' , foreground=colors.red_color , bd=0 , activebackground=colors.light_grey_color , activeforeground=colors.white_color)
        self.settings_button.configure(styles.login_page_design.button_styles_close(self , self.settings_button , None , 1  , colors.dark_color_grey , colors.red_color, colors.dark_color_grey , colors.red_color))
        self.open_close_button.configure(styles.login_page_design.button_styles_close(self , self.open_close_button , 2 , 1  , colors.dark_color_grey , colors.red_color, colors.dark_color_grey , colors.red_color))
        self.side_home_button.configure(styles.login_page_design.button_styles_close(self , self.side_home_button , 50 , 50 , colors.dark_color_grey , None , colors.grey_color_2 , None))
        self.side_betting_button.configure(styles.login_page_design.button_styles_close(self , self.side_betting_button , 50 , 50 , colors.dark_color_grey , None , colors.grey_color_2 , None))
        self.side_history_button.configure(styles.login_page_design.button_styles_close(self , self.side_history_button , 50 , 50 , colors.dark_color_grey , None , colors.grey_color_2 , None))
        
        # Binding Controls 
        self.titlebar.bind("<ButtonPress-1>" , self.mouse_click)
        self.titlebar.bind("<B1-Motion>" , self.mouse_move)
        self.close_button.bind("<Enter>" , lambda event : self.close_button.configure(background=colors.grey_color_2))
        self.close_button.bind("<Leave>" , lambda event  : self.close_button.configure(background=colors.dark_color_grey))
        self.max_button.bind("<Enter>" , lambda event : self.max_button.configure(background=colors.grey_color_2))
        self.max_button.bind("<Leave>" , lambda event  : self.max_button.configure(background=colors.dark_color_grey))
        self.min_button.bind("<Enter>" , lambda event : self.min_button.configure(background=colors.grey_color_2))
        self.min_button.bind("<Leave>" , lambda event  : self.min_button.configure(background=colors.dark_color_grey))
        self.settings_button.bind("<Enter>" , lambda event : self.settings_button.configure(background=colors.light_grey_color , foreground=colors.white_color))
        self.settings_button.bind("<Leave>" , lambda event  : self.settings_button.configure(background=colors.dark_color_grey , foreground=colors.red_color))
        self.open_close_button.bind("<Enter>" , lambda event : self.open_close_button.configure(background=colors.light_grey_color , foreground=colors.white_color))
        self.open_close_button.bind("<Leave>" , lambda event  : self.open_close_button.configure(background=colors.dark_color_grey , foreground=colors.red_color))
        # Configure the buttons for sidebar : 
        self.side_home_button.bind("<Enter>" , lambda event : self.side_home_button.configure(background=colors.light_grey_color))
        self.side_home_button.bind("<Leave>" , lambda event  : self.side_home_button.configure(background=colors.dark_color_grey ))
        self.side_betting_button.bind("<Enter>" , lambda event : self.side_betting_button.configure(background=colors.light_grey_color ))
        self.side_betting_button.bind("<Leave>" , lambda event  : self.side_betting_button.configure(background=colors.dark_color_grey))
        self.side_history_button.bind("<Enter>" , lambda event : self.side_history_button.configure(background=colors.light_grey_color))
        self.side_history_button.bind("<Leave>" , lambda event  : self.side_history_button.configure(background=colors.dark_color_grey ))


    def placing_controls(self):
        # Placing the titlebar close min and max button
        self.titlebar.pack(side='top' , fill='x')
        self.close_button.pack(side='right' , pady=(1,1))
        self.max_button.pack(side='right' , pady=(1,1))
        self.min_button.pack(side='right' , pady=(1,1))
        self.dashboard.after(10, lambda: self.set_appwindow(self.dashboard))


        # Placing sidebar 
        self.sidebar_frame.pack(side='left' , fill='y')

        self.sidebar_user_frame.pack(side='top' , pady=(10,0))
        self.user_image.pack()
        # self.user_image_name.pack(side='top' , pady=(10,0))
        

       # Placing the upper control : 
        self.upper_frame.pack(side='top' , fill='x')
       # Settings and Open close button :
        self.open_close_button.pack(side='bottom' ,  anchor=tk.SE , padx=(2,2) , pady=(0,2))
        self.settings_button.pack(side='bottom' , anchor=tk.SE , padx=(2,2) , pady=(0 ,2))

        # Placing the upper Frame usernmae Imgae and username text :
        self.username_frame.pack(side='right' , padx=(5,15))
        self.down_button.pack(side='right' , padx=(5,5))
        self.user_name_label.pack(side='right' , padx=(0 , 0))
        self.user_image_label.pack(side='right' , padx=(0,0))

        self.main_contents_frame.pack(side='left' , padx=(0,0) , pady=(0,0))
        
        self.side_home_button.pack(side='top' , pady=(20 , 0))
        self.side_betting_button.pack(side='top' , pady=(0 , 0))
        self.side_history_button.pack(side='top' , pady=(0 , 0))
        
        ## Calling the main app
        self.dashboard.mainloop()



if __name__ == '__main__':
    main_dashb = Dashboard(1000 ,700)
    main_dashb.defining_controls()
    main_dashb.placing_controls()
