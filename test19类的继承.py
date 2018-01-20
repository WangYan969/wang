# coding:utf-8
# ===============================
# 类的继承
# class Parent:
#
#     def __int__(self):
#         parentAttr = 1
#     def myMethod(self):
#         print "父类方法"
#     def setAttrZ(self,setattr):
#         self.parentAttr = setattr
#     def getAttr(self):
#         print self.parentAttr
#
# class Child(Parent):
#     def __int__(self):
#         print "子类构造函数"
#     def myMethod(self):
#         print "子类方法"

# c = Child()
# c.childMethod()      #调用子类方法
# c.parentMethod()     #调用父类方法
# c.myMethod()     # 父类 子类 方法名 一致  调用子类(方法重写)
# c.setAttrZ(222333)      #调用父类方法
# c.getAttr()          #调用父类方法
# ===================================
# 运算符重载
# class Vector:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return "Vector (%d,%d)" % (self.a, self.b)
#     def __add__(self, other):
#         return Vector(self.a + other.a , self.b + other.b)
#     def __sub__(self, other):
#         return Vector(self.a - other.a , self.b - other.b)
#
#
#
# v1 = Vector(1,2)
# v2 = Vector(3,4)
# print v1 + v2

# =================================
