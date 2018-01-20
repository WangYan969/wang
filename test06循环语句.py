# coding:utf-8

# a , b , c = 1 , 2 , 3
#
# if a is b:
#     print '相等'
# else :
#     print '不相等'


# elseif' 写作 elif'
# a = raw_input()
# b = raw_input()
#
# if a > b :
#     print '大于'
# elif a < b :
#     print '小于'
# else :
#     print '等于'

#
# for x in "abcd" :
#     print x
# print x

# A 报错
# B abcdd               √
# C abcd (有一个空格)
# =========================
#
# for a in range(1,10) :
#     print a
# print a

# A 1~10
# B 1~9   √
# C 1~99
#========================
#
# for x in 'abcd':
#     if x == 'a':
#         print x
#     print x
#
# A 报错
# B a a b c d   √
#=======================
# range后的第三个 表示间隔
# for x in range(1,10,2):
#     print x,
# =============================
# 9 9乘法表
# for x in range(1,10):
#     for y in range(1,x+1):
#         print "%d*%d=%d" % (x,y,x*y),#最后加一个 ',' 实现 三角效果
#     print "      "
#=======================
#可以让控制输出的格式 (中间 两边 以及填充的字符 以及个数)
# a = 'xxxx'
# print a.center(10,'*')
# print a.ljust(10,'&')
# print a.rjust(15,'*')
#=====================
#
#  python的while循环
# count = 0
# while count < 10 :
#     print count
#     count+=1
#=========================
#      break的解释
# for x in 'asdfgh':
#     if x == 'd':
#         print "结束"
#         break # 直接终止整个循环(跳出)
#     print x
# print x

# A 报错
# B a s 结束 d          √
#===============================
#       continue的解释
# for x in 'asdfgh':
#     if x == 'd':
#         print "结束"
#         continue # 终止此次循环,进入下一次循环
#     print x
# print x
#==============================
#
# count = 0
# while count < 10 :
#     print count ,
#     count+=1
#     if count == 5:
#         break
# print count

# A 报错
# B 012345      √
# C 0123455
#==========================
