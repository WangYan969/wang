# coding:utf-8
#
#@ xrange是在使用的时候才会生成我们的数字 而 range只要运行就会生成
# a = range(0,8)
# a1 = range(8)
# a2 = xrange(8)
#
#==================================
# 先导入random 用random的choice 进行生成随机数
# a = range(8)
# import  random
# b = random.choice(a)
# print b
#==============================
# random.random 是生成一个0~1的数 randrange是生成一个()内范围的数
# import random
#
# a = random.random()
# b = random.randrange(50,100)
#=================================
# random.shuffle是打乱顺序,不能对xrange使用
# import random
# a = range(10)
# random.shuffle(a)
# print a
#================================

