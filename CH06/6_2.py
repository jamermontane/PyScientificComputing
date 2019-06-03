#-*-coding:GBK -*-

from traits.api import Delegate, HasTraits, Instance, Int, Str 

class Parent( HasTraits):
    # ��ʼ��: last_name����ʼ��Ϊ'Zhang'
    last_name=Str('Zhang')
    
class Child(HasTraits):
    age = Int
    
    # ��֤: father���Ե�ֵ������Parent���ʵ��
    father = Instance(Parent)
    
    # ί��: Child��ʵ����last_name����ί�и���father���Ե�last_name
    last_name = Delegate('father')
    
    # ����: ��age���Ե�ֵ���޸�ʱ������ĺ�����������
    def _age_changed(self, old, new):
        print("Age changed from %s to %s" %(old,new))
    
    
p = Parent()
c = Child()

c.father = p
print(c.last_name)

c.age = 4

c.configure_traits()
print(c.print_traits())
print(c.get())
c.set(age = 6)