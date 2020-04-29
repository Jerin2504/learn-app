from tkinter import *
#from universal import *
from New_Customer_bus import *

class New_Customer_Gui:

      def registratn(frame,):

          l_heading           = Label(frame, text = "Customer Registration", font = "Times 16 bold")
          l_cust_name         = Label(frame, text = "Name")
          l_address           = Label(frame, text = "Address")
          l_pincode           = Label(frame, text = "Pincode")
          l_gst               = Label(frame, text = "GST Number")
          l_credit            = Label(frame, text = "Credit Period")
          l_cntct_name        = Label(frame, text = "Contact Name")
          l_cntct_desg        = Label(frame, text = "Designation")
          l_cntct_number      = Label(frame, text = "Contact Number")
          
          btn_submit          = Button(frame, text = "Register", command = lambda : process_input())



 #         e=StringVar()
 #         e_cust_name = Entry(frame,width=5,textvariable=e).grid()

          e_cust_name         = Entry(frame, width = 20, )
          e_address           = Text (frame, width = 20, height = 5 )
          e_pincode           = Entry(frame, width = 20, )
          e_gst               = Entry(frame, width = 20, )
          e_credit            = Entry(frame, width = 20, )
          e_cntct_name        = Entry(frame, width = 20, )
          e_cntct_desg        = Entry(frame, width = 20, )
          e_cntct_number      = Entry(frame, width = 20, )
 
          l_heading.grid(row = 1, column = 1, padx = 20, pady = 50, columnspan = 3)
          btn_submit.grid(row = 10, column = 1, padx = 20, pady = 30, columnspan = 3)

          row_count = 2
          for labels in (l_cust_name, l_address, l_pincode, l_gst, l_credit, 
                         l_cntct_name, l_cntct_desg, l_cntct_number):
               labels.grid(row = (row_count), column = 1, padx = 10, pady = 5, sticky = "W") 
               row_count += 1

          row_count = 2
          for entries in (e_cust_name, e_address, e_pincode, e_gst, e_credit, 
                         e_cntct_name, e_cntct_desg, e_cntct_number):
               entries.grid(row = (row_count), column = 3, padx = 10, pady = 5, sticky = "W") 
               row_count += 1
               

#          l_cust_name.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = "w")
#          l_address.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = "W")
#          l_pincode.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = "W")
#          l_gst.grid(row = 5, column = 1, padx = 10, pady = 5, sticky = "W")
#          l_credit.grid(row = 6, column = 1, padx = 10, pady = 5, sticky = "W")
#          l_cntct_name.grid(row = 7, column = 1, padx = 10, pady = 5, sticky = "W")
#          l_cntct_desg.grid(row = 8, column = 1, padx = 10, pady = 5, sticky = "W")
#          l_cntct_number.grid(row = 9, column = 1, padx = 10, pady = 5, sticky = "W")
          
#          e_cust_name.grid(row = 2, column = 3, padx = 10, pady = 5, sticky = "W")
#          e_address.grid(row = 3, column = 3, padx = 10, pady = 5, sticky = "W")
#          e_pincode.grid(row = 4, column = 3, padx = 10, pady = 5, sticky = "W")
#          e_gst.grid(row = 5, column = 3, padx = 10, pady = 5, sticky = "W")
#          e_credit.grid(row = 6, column = 3, padx = 10, pady = 5, sticky = "W")
#          e_cntct_name.grid(row = 7, column = 3, padx = 10, pady = 5, sticky = "W")
#          e_cntct_desg.grid(row = 8, column = 3, padx = 10, pady = 5, sticky = "W")
#          e_cntct_number.grid(row = 9, column = 3, padx = 10, pady = 5, sticky = "W")

     
          def process_input():
               print("process started")






          

          
          
          
 