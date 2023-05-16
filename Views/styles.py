import styles
import colors

from tkinter import *



## Dummy part whcih will be deleted later

# root = Tk()
# main = Button(root)
# root.mainloop()


class login_page_design():

    def __init__(self) -> None:
        pass

    def frame_styles(self , frame_name  , width , height ,  bg_color):
        frame_name.configure(width=width , height=height , background=bg_color)
    
    def button_styles_close(self,  button_name , width  , height , bg_color,  fg_color):
        button_name.configure(height=height , width=width , background=bg_color , foreground=fg_color , bd=0  , relief=SUNKEN,
                       activebackground=colors.black_color , activeforeground=colors.red_color)
    