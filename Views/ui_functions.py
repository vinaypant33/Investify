import tkinter as tk 

# root   = tk.Tk()



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

    def __init__(self , master_frame , current_width  ,  app_current_height) -> None:

        self.current_width  = current_width
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
        self.current_balance_frame.configure(height=self.current_height*0.30 , width=self.current_width / 3.50 , background='red')
        self.total_bets_frame.configure(height=self.current_height * 0.30 , width=self.current_width / 3.50 , background='green')
        self.profit_loss_frame.configure(height=self.current_height * 0.30 , width=self.current_width / 3.50 , background='yellow')
        self.graph_frame.configure(height = self.current_height * 0.70 , width=self.current_width * 0.90 , background='pink')


        self.current_balance_frame.pack_propagate(0)
        self.total_bets_frame.pack_propagate(0)
        self.profit_loss_frame.pack_propagate(0)
        self.graph_frame.pack_propagate(0)

    def packing(self):
        ## Packing all in sequence : 
        self.current_balance_frame.pack(side="left")
        self.total_bets_frame.pack(side="left")
        self.profit_loss_frame.pack(side="left")
        self.graph_frame.pack(side="bottom")

        self.current_bets_label.pack(side="left" ,  anchor='nw' , padx=(5,5) , pady=(5,5))
        self.current_bets_value.pack(anchor="center" , pady=(10))

        self.total_bets_label.pack(side="left" , anchor='nw', padx=(5,5) , pady=(5,5))
        self.total_bets_value.pack(anchor="center" , pady=(10,10))

        self.profit_loss_label.pack(side="left" , anchor="nw" , padx=(5,5) , pady=(5,5))
        self.profit_loss_value.pack(anchor="center" , pady=(10))


        self.graph_frame.pack(side="top" , padx=(2,2))


    # def __del__(self) -> None:
    #     print("Hello I am destroyed") 
    #     self.current_bets_name.pack_forget()



# main = Dashboard_controls(root , 900 , 1100)
# main.configuring()
# main.packing()




# root.mainloop()