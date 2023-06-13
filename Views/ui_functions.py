import tkinter as tk 





class custom_button(tk.Button):

    def __init__(self , master , main_text  , function) -> None:
        super().__init__(master)


        # Frame for the button  : 
        self.frame  = tk.Frame(master , height=200 , width=200 , background='red')
        self.frame.pack_propagate(0)
        self.cbtn  = tk.Button(self.frame, text=main_text , command=function)

        self.frame.pack()
        self.cbtn.pack()



# root  = tk.Tk()


# def hello_print():
#     print("Hello world")

# cbtn = custom_button(root , main_text="Hello World" , function=hello_print)


# cbtn.configure(height=50 , width=50)
# # cbtn.pack()


# # hebtn  = custom_button(root , main_text="hehe haa holo" , function=hello_print)


# root.mainloop()