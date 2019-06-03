#-*-coding:GBK -*- 

from traits.api import HasTraits, Color

class Circle(HasTraits):
    color = Color
    
c = Circle()
print(c.color)

c.color="red"
print(c.color)
c.color=0x00FF00
print(c.color)
c.color=(0,255,255)
print(c.color)
print(c.configure_traits())
print(c.color)