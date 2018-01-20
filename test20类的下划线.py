# coding:utf-8
# __a__ : 定义的是特殊方法.类似__init__()之类的
# _a :  以单划线开头的表示得失 protec类型的变量,即保护型只能允许其本身子类进行访问,不能用于 from module import *
# __a : 双下换线的 表示的是私有类型(private)的变量,,只能允许这个类本身进行访问
class stu:
    name = "ceshi"
    _age = 19
    __shenGao = 180
    def __init__(self,z):
        self.wan = z
    def baoGao(self):
        print self.__shenGao
class stu1(stu):
    def __init__(self,z):
        self.wan = z

s = stu1("daima")
print s.name
print s._age
# print s.__shenGao  #会报错
s.baoGao()
# ============================