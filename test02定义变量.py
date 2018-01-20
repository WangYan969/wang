# coding:utf-8
# a = 1
# b = '2'
# c = type(b)
# print a,b,c
# e , f , g = 5 , '喝' , 3.14
# h = type(g)
# print e,f,g,h
# i = j = 10
# print i,j
#
# a = 1
# b = 2
# print a,b
# #把a指向b所指向的值,即2
# a = b
# print a,b
# #把b指向3
# b = 3
# print a,b

a = [1,2]
b = [3,4]
print a,b
#把a指向b所指向的值,即[3,4]
a = b
print a,b
#把b指向的值调整,即[3,3]
b[1] = b[0]
print a,b