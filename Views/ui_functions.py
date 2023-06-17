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




class Dashboard_controls():

    def __init__(self , master_frame , app_current_width  ,  app_current_height , width_to_reduce = 100) -> None:
        self.current_width  = app_current_width - width_to_reduce
        self.current_height  = app_current_height
        # Defining frames for the application :
        self.current_balance_frame = tk.Frame(master_frame)
        self.current_balance_frame_shadow  = tk.Frame(master_frame)
        self.total_bets_frame =  tk.Frame(master_frame)
        self.total_bets_frame_shadow  = tk.Frame(master_frame)
        self.profit_loss_frame = tk.Frame(master_frame)
        self.profit_loss_frame_shadow = tk.Frame(master_frame)
        self.graph_frame  = tk.Frame(master_frame)
        self.graph_frame_shadow  = tk.Frame(master_frame)

        self.current_bets_label  = tk.Label(self.current_balance_frame , text="Current Bets")
        self.current_bets_value  = tk.Label(self.current_balance_frame , text="0")
        self.total_bets_label  = tk.Label(self.total_bets_frame , text="Total Bets")
        self.total_bets_value  = tk.Label(self.total_bets_frame , text="0")
        self.profit_loss_label  = tk.Label(self.profit_loss_frame , text="Profit / Loss")
        self.profit_loss_value  = tk.Label(self.profit_loss_frame , text="0")

    def configuring(self):
        self.current_balance_frame.configure(height=self.current_height*0.25 , width= (self.current_width - self.current_width * 0.04) / 3.20 , background='red')
        self.total_bets_frame.configure(height=self.current_height * 0.25 , width= (self.current_width - self.current_width * 0.04) / 3.20 , background='blue')
        self.profit_loss_frame.configure(height=self.current_height * 0.25 , width= (self.current_width - self.current_width * 0.04) / 3.20 , background='yellow')
        self.graph_frame.configure(height = self.current_height * 0.60 , width= self.current_width * 0.95 , background='pink')

        self.current_balance_frame.pack_propagate(0)
        self.total_bets_frame.pack_propagate(0)
        self.profit_loss_frame.pack_propagate(0)
        self.graph_frame.pack_propagate(0)

    def packing(self):
        ## Packing all in sequence : 
        self.initial_difference  = self.current_width * 0.01

        ## Calculating the final sifference here which will change into the code later 

        final_diff  = self.initial_difference*2
        self.x_loc = self.current_width - (final_diff * 2)

        # Placing frames wrt to the current height of the Dashboard : 
        self.current_balance_frame.place(x = self.initial_difference , y = self.current_height * 0.01)
        self.total_bets_frame.place(x = (((self.current_width - self.initial_difference) / 3 )+ self.initial_difference) , y  = self.current_height * 0.01)
        self.profit_loss_frame.place(x = (((self.current_width - self.initial_difference) / 3  + (self.current_width - self.current_width * 0.04) / 3.20 + final_diff)+ self.initial_difference) , y  = self.current_height * 0.01)


        self.graph_frame.place(x = (self.current_width * 0.05 / 3), y = self.current_height * 0.28)
        self.current_bets_label.pack(side="left" ,  anchor='nw' , padx=(10,10) , pady=(10,10))
        self.current_bets_value.place(relx = 0.5 , rely = 0.5  , anchor="center")
        self.total_bets_label.pack(side="left" ,  anchor='nw' , padx=(10,10) , pady=(10,10))
        self.total_bets_value.place(relx = 0.5 , rely = 0.5  , anchor="center")
        self.profit_loss_label.pack(side="left" ,  anchor='nw' , padx=(10,10) , pady=(10,10))
        self.profit_loss_value.place(relx = 0.5 , rely = 0.5  , anchor="center")




    def clean_slate(self):
        self.current_balance_frame.destroy()
        self.total_bets_frame.destroy()
        self.profit_loss_frame.destroy()
        self.graph_frame.destroy()



class child_form():
    def __init__(self , width  = 100 ,  height  = 60) -> None:
        self.child_form  = tk.Tk()
        self.width  = width
        self.height  = height
        self.child_form.geometry(f'{width}x{height}')
        ## 





        ## Into the main loop  
        self.child_form.mainloop()


if __name__ == '__main__':
    # root   = tk.Tk()
    # root.geometry("1000x700")
    # main = Dashboard_controls(root , 1000 , 700)
    # main.configuring()
    # main.packing()
    # root.mainloop()

    main_c = child_form()
