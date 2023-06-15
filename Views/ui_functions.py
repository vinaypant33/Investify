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

    def __init__(self , master_frame , app_current_width  ,  app_current_height) -> None:
        
        self.current_width  = app_current_width
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

        # Placing frames wrt to the current height of the Dashboard : 
        self.current_balance_frame.place(x = (self.current_width * 0.05 / 3), y = self.current_height * 0.01)
        self.total_bets_frame.place(x  = (self.current_width / 3) + self.current_width * 0.05 / 3  , y =self.current_height * 0.01)
        self.profit_loss_frame.place(x = ((self.current_width  / 3) * 2) + self.current_width * 0.05 / 3  , y =self.current_height * 0.01)

        self.graph_frame.place(x = (self.current_width * 0.05 / 3), y = self.current_height * 0.28)


        self.current_bets_label.pack(side="left" ,  anchor='nw' , padx=(5,5) , pady=(5,5))
        self.current_bets_value.pack(anchor="center" , pady=(10 , 10))

        self.total_bets_label.pack(side="left" , anchor='nw', padx=(5,5) , pady=(5,5))
        self.total_bets_value.pack(anchor="center" , pady=(10,10))

        self.profit_loss_label.pack(side="left" , anchor="nw" , padx=(5,5) , pady=(5,5))
        self.profit_loss_value.pack(anchor="center" , pady=(10))




    # def __del__(self) -> None:
    #     print("Hello I am destroyed") 
    #     self.current_bets_name.pack_forget()



if __name__ == '__main__':
    
    root   = tk.Tk()
    root.geometry("1000x700")

    main = Dashboard_controls(root , 1000 , 700)
    main.configuring()
    main.packing()
    root.mainloop()