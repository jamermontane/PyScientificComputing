#-*-coding:GBK -*-

from traits.api import *

a = HasTraits()
a.add_trait("x",Float(3.0))
print(a.x)

b = HasTraits()
b.add_trait("a",Instance(HasTraits))
b.a = a
b.add_trait("y",Delegate("a","x",modify=True))
print("b.y",b.y)
b.y = 10
print("a.x",a.x)