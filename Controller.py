from tkinter import *
from Menu_Header_Gui import *
from db_config import engine, Session
#from New_Customer_Gui import *
#from New_Order_Gui import *


class main_gui:
    def __init__(self):
     
        self.root = Tk()
        self.root.title("Travancore Cartons")   
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(),self.root.winfo_screenheight()))
        self.root.rowconfigure(0, weight = 1)
        self.root.columnconfigure(0, weight = 1)
        self.root.option_readfile('optionDb')


        
    

    
def main():
    app = main_gui()
    Menu_Header_Gui.create_menu(app)
#    New_Customer_Gui.registratn(app)
#    New_Order_Gui.new_order(app)
    
    
    app.root.mainloop()
    

if __name__ == "__main__":
    main()

    
