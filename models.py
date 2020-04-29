from sqlalchemy import Column, Integer, String, Date, Sequence
from db_config import Base

class Customer(Base):

    __tablename__ = "Customers"
    t_cust_id            = Column(Integer, primary_key=True)
    t_cust_name          = Column(String)
    t_address            = Column(String)
    t_pincode            = Column(Integer)
    t_gst                = Column(String)
    t_credit             = Column(Integer)
    t_cntct_name         = Column(String)
    t_cntct_desg         = Column(String)
    t_cntct_number       = Column(Integer)

    def __init__(self, t_cust_name, t_address, t_pincode, t_gst,
                 t_credit, t_cntct_name, t_cntct_desg, t_cntct_number):
        self.t_cust_name = t_cust_name
        self.t_address   = t_address
        self.t_pincode   = t_pincode
        self.t_gst       = t_gst
        self.t_credit    = t_credit
        self.t_cntct_name    = t_cntct_name
        self.t_cntct_desg    = t_cntct_desg
        self.t_cntct_number  = t_cntct_number

    

