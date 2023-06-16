import tkinter as tk

root = tk.Tk()



def hehe():
    global width_name
    global height_name

    width_name  = input("Height")
    height_name  = input("Width")

    main(width_name , height_name)


def main(width , height ):
    main_frame  = tk.Frame(root , width=width_name , height = height_name , background='yellow')
    main_frame.pack()
    main_frame.pack()
    width = main_frame.winfo_width()
    height = main_frame.winfo_height()
    print("Width:", width_name)
    print("Height:", height_name)


# Get the width and height of the frame


main_button  = tk.Button(root , text="Name" , command=hehe)
main_button.pack()

root.mainloop()
