from PIL import Image , ImageTk

def sidebar_size_controls():
    pass



name_image  = Image.open(r'Assets\user_avatars\avataer_man.png')
name_resized = name_image.resize((50 , 50))
name_image  = ImageTk.PhotoImage(name_resized)