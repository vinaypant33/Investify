
## Setting Fonts for the texts : 
super_small_font  = ("Times" , "8")
super_small_font_bold  = ("Times", "8", "bold")
small_font  = ('Times' , "10")
small_font_bold = ("Times" , "10" , "bold")
medium_font  = ("Times" , "12")
medium_font_bold = ("Times" , "12" , "bold")
large_font = ("Times" , "16")
large_font_bold  = ("Times" , "16" , "bold")




import tkinter as tk

# Dummy part whcih will be deleted later

# root = tk.Tk()
# main = tk.Entry(root).pack()

# hehe  = tk.Button(root)
# root.mainloop()


class login_page_design():

    def __init__(self) -> None:
        pass

    def frame_styles(self , frame_name  , width , height ,  bg_color):
        frame_name.configure(width=width , height=height , background=bg_color)
    
    def button_styles_close(self,  button_name , width  , height , bg_color,  fg_color , active_bg , active_fg):
        button_name.configure(height=height , width=width , background=bg_color , foreground=fg_color , bd=0  , relief=tk.SUNKEN,
                       activebackground=active_bg , activeforeground=active_fg)
    
    def text_box_configure(self , master  , bg_color , fg_color):
        master.configure( background=bg_color , foreground=fg_color  , font = large_font_bold,
               bd = 0  , justify = 'center')
        



class Dashboard_design():

    def __init__(self) -> None:
        pass

    def label_marking(self , master ):
        pass

    def button_style(self , master):
        # hehe.configure(bd = 0 , )
        pass
    
    def Button_hover_enter(self,  master , bg_color):
        hehe.configure(background=bg_color)

    