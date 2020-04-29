from tkinter import *
from New_Customer_Gui import *
from New_Order_Gui import *
#from universal import *

class Menu_Header_Gui:
 
    def create_menu(self, ):
        print("yes")
        menubar = Menu(self.root)

        counter_list = [0,0]
        
        FNC = Frame(self.root)
    #    FNC.grid(row=0,column=0,sticky="news")
        FNO = Frame(self.root)
    #    FNO.grid(row=0,column=0,sticky="news")

        for grds in (FNC, FNO):
             grds.grid(row = 0, column = 0, sticky = "NEWS")    
  
        FNC.rowconfigure(0, weight = 1) 
        FNC.rowconfigure(100, weight = 5)   
        FNO.rowconfigure(0, weight = 1)
        FNC.columnconfigure(0, weight = 1)
        FNC.columnconfigure(100, weight = 1)
        FNO.columnconfigure(0, weight = 1)

# Menu for customer details       
        cust = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Customer",menu=cust)
        print("fnc1")
        cust.add_checkbutton(label = "New Customer",command = lambda : raise_frame("FNC"))
        

 # Menu for order details       
        order = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Order",menu=order)
        
        order.add_checkbutton(label = "New Order",command = lambda : raise_frame("FNO"))
    #    New_Order_Gui.new_order(FNO))
    #    FNO.tkraise()
    
               
        
        def raise_frame(frames, ):
            print(frames)
            if   frames == "FNC":
                  print("fnc")
                  FNC.tkraise()
                  if counter_list[0] == 0: 
                      New_Customer_Gui.registratn(FNC)
                      counter_list[0] += 1
                    
                  
            
            elif frames == "FNO":
                  print("fno")
                  FNO.tkraise()
                  if counter_list[1] == 0:
                      New_Order_Gui.new_order(FNO)
                      counter_list[1] += 1
                      
                  
            
        

        self.root.config(menu=menubar) 
        
        