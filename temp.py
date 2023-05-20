import tkinter
import customtkinter  # <- import the CustomTkinter module

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")
customtkinter.set_appearance_mode("Dark") # Other: "Light", "System" (only macOS)

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=root_tk,
                                 fg_color=("black", "lightgray"),  # <- tuple color for light and dark theme
                                 text="CTkButton",
                                 command=button_function)

root_tk.mainloop()