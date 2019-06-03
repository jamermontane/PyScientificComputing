#-*-coding:GBK -*-

from traits.api import HasTraits,Str,Int
from traitsui.api import View,Item,Group
from altair.vegalite.v2.schema.channels import Tooltip

class SimpleEmployee(HasTraits):
    first_name = Str
    last_name = Str
    department = Str
    employee_number = Str
    salary = Int
    
view1 = View(
    Item(name = 'department',label="部门",tooltip="在哪个部分干活"),
    Item(name = 'last_name',label="姓"),
    Item(name = 'first_name',label="名"),
    )    

sam  = SimpleEmployee()
sam.configure_traits(view = view1)

