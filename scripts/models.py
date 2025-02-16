from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DOUBLE_PRECISION, String, Date

Base = declarative_base()

class OnhandRecord(Base):
    
    __tablename__= 'table_onhand'

    id = Column(Integer, primary_key=True, index=True)
    file_date = Column(name="file_date", type_=Date)
    org = Column(name='org', type_=String)
    item = Column(name='item', type_=String)
    uit = Column(name='uit', type_=String)
    uom = Column(name='uom', type_=String)
    desc = Column(name='desc', type_=String)
    spec = Column(name='spec', type_=String)
    subinv = Column(name='subinv', type_=String)
    locator = Column(name='locator', type_=String)
    onhand_qty = Column(name='onhand_qty', type_=String)
    reserve_qty = Column(name='reserve_qty', type_=String)
    available = Column(name='available', type_=String)
    item_cost = Column(name='item_cost', type_=String)
    amount = Column(name='amount', type_=String)
    small_packing = Column(name='small_packing', type_=String)
    w_keeper = Column(name='w_keeper', type_=String)
    planner = Column(name='planner', type_=String)
    purchaser = Column(name='purchaser', type_=String)
    location = Column(name='location', type_=String)
    delivery_type = Column(name='delivery_type', type_=String)
    sub_mat = Column(name='sub_mat', type_=String)
    wms_flag = Column(name='wms_flag', type_=String)