# from tkinter import ttk 
# import tkinter as tk 
# from PIL import Image , ImageTk



# root  = tk.Tk()




# # class custom_button( tk.Button):

# #     def __init__(self , master  = None, height  = 1 ,  width  = 10) -> None:

# #         self.meri_image  = Image.open(r'Assets\user_avatars\panda.png')
# #         self.merii_image  = ImageTk.PhotoImage(self.meri_image)
# #         super().__init__(master = master , text="behen ki chut" , height=height , width=width , image=self.merii_image)



# # class BTN_IMG_TXT(tk.Button):
# #     def __init__(self, master=None, cnf={}, **kw):
# #         # Merged both cnf and kw dictionaries.
# #         kw = tk._cnfmerge((kw, cnf)) 
# #         # make static size
# #         if kw.get('image'):
# #             img = Image.open(kw['image'])
# #             image = img.resize((40,40), Image.ANTIALIAS)  
# #             self.photo1 = ImageTk.PhotoImage(image)
# #             kw['image'] = self.photo1
# #         # Aligns the image on top and text under it
# #         kw['compound'] = kw.get('compound', 'top') 
# #         super().__init__(master=master, **kw)


# def remove_item():
#     print("I am called")


# # frm_Main = tk.Frame(master=root, bg='#faeaea', borderwidth=2)
# # frm_Main.pack()
# # stp_btn = BTN_IMG_TXT(master=frm_Main, image=r"Assets\user_avatars\panda.png", text='STOP', command=remove_item)
# # del_btn= BTN_IMG_TXT(master=frm_Main, image=r"Assets\user_avatars\panda.png", text='DELETE', command=remove_item)
# # del_btn.pack(side="left", fill="both", expand=False)
# # stp_btn.pack(side="left", fill="both", expand=False)

# # main_button  = custom_button(root , 10  , 20)
# # main_button.pack()

# master_Image   = Image.open(r'c:\Users\Vinay\Downloads\download.gif')






# # def animation(i):
    
    
# #     master_Image.seek(i)
# #     global main_resized
# #     main_resized  = master_Image.resize((80,80))
# #     for i in range(31):
# #         root.after(10 , animation(i))
# #         global main_image
# #     main_image  = ImageTk.PhotoImage(main_resized )

# #     main_button  = ttk.Button(root , text="name mera vinay" , image=main_image , command=animation(1) )
# #     main_button.configure(compound="left" , padding=(100,10))

# #     main_button.pack(padx=(10,0))


# # main_other  = ttk.Button(root , text="name" and "vinay").pack()

# # animation(1)




# import tkinter as tk
# from PIL import Image, ImageTk

# def load_second_frame():
#     # Open the GIF image using PIL
#     gif_image = Image.open(r'c:\Users\Vinay\Downloads\download.gif')

#     # Get the second frame of the GIF
#     button  = ttk.Button(root)
#     for i in range(31):

#         gif_image.seek(1)

#         # Convert the PIL image to Tkinter-compatible format
#         tk_image = ImageTk.PhotoImage(gif_image)

#         # Update the button's image
#         button.config(image=tk_image)

# root = tk.Tk()

# # Create a button
# button = tk.Button(root, text="Load Second Frame", command=load_second_frame)
# button.pack()

# root.mainloop()



# root.mainloop()





from tkinter import ttk  
import tkinter as tk 
from PIL import Image , ImageTk


class frame_buton(tk.Button):

    def __init__(self , master,  image_link , function , height = 3 , width  = 100) -> None:
        self.frame  = tk.Frame(master)
        self.image  = ImageTk.PhotoImage(image=image_link)
        self.image_label  = tk.Label(image=self.image)
        self.frame_2 = tk.Frame(self.frame)
        self.button  = ttk.Button(self.frame_2 , text="I am a Button" ,command=function)

        self.frame.configure(background='black' , height=height  , width=width)
        self.frame_2.configure(background='red' , height=height , width=width)
        self.frame.pack_propagate(1)
        self.frame_2.pack_propagate(1)


        self.frame.pack()
        self.frame_2.pack(side='left')
        self.image_label.pack(side='right')
        self.button.pack(side='left')
        super().__init__(master = master)


root = tk.Tk()


def print_name():
    print("Name")


image  = Image.open(r'Assets\user_avatars\panda.png')
image  = image.resize((30 , 30))
main = frame_buton(root , image_link=image , function=print_name , height=100 , width  =100)








root.mainloop()

        