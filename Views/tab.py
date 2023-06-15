import tkinter as tk 





class main_app_data():


    def __init__(self , master , function) -> None:
        self.main_button  = tk.Button(master  , text="Hello World" , command=function)
        self.other_button = tk.Button(master , text="Hehe Button" , command=function)

        self.main_button.pack()
        self.other_button.pack()


def main_print():
    print("Hello World")

root = tk.Tk()

hehe = main_app_data(root , main_print)

root.mainloop()