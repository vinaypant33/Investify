import styles
import colors


## Setting Fonts for the texts : 

super_small_font  = ("Times", "18", "bold")




from tkinter import *



## Dummy part whcih will be deleted later

# root = Tk()
# main = Entry(root)





# root.mainloop()





class login_page_design():

    def __init__(self) -> None:
        pass

    def frame_styles(self , frame_name  , width , height ,  bg_color):
        frame_name.configure(width=width , height=height , background=bg_color)
    
    def button_styles_close(self,  button_name , width  , height , bg_color,  fg_color):
        button_name.configure(height=height , width=width , background=bg_color , foreground=fg_color , bd=0  , relief=SUNKEN,
                       activebackground=colors.black_color , activeforeground=colors.red_color)
    
    def text_box_configure(self , master  , bg_color , fg_color):
        master.configure( background=bg_color , foreground=fg_color  , font=super_small_font,
               bd = 0  , justify = 'center')