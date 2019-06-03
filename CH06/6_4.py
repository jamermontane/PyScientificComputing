#-*-coding:GBK -*-

from traits.api import HasTraits,Float,Property,cached_property

class Rectangle(HasTraits):
    widhth = Float(1.0)
    height=Float(2.0)
    
    #area��һ�����ԣ���width,height��ֵ�仯ʱ������Ӧ��_get_area������������
    area = Property(depends_on=['width','height'])
    
    # ͨ��cached_property decorator����_get_area���������
    
    @cached_property
    def _get_area(self):
        # area��get������ע��˺������Ͷ�Ӧ��Proerty���Ĺ�ϵ
        print('recaculating')
        return self.widhth * self.height
    
