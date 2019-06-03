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
    Item(name = 'department',label="����",tooltip="���ĸ����ָɻ�"),
    Item(name = 'last_name',label="��"),
    Item(name = 'first_name',label="��"),
    )    

sam  = SimpleEmployee()
sam.configure_traits(view = view1)

