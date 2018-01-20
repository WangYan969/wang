# coding:utf-8
# ============================
# l = [ 1 , 2 , 3 , "aa" ]
# 取值
# print l[-2:]
# print l[:7]
#修改
# l[0] = 111
# l[-2:] = [2333,2222222222,3333333333]
# l[-2:] = [3]
# print l
#删除
# del l[-2:]
# print l
# del l
#print l # 因为l已经没有东西 所以 print 会报错
# 添加
# l = [ 1 , 2 , 3 , "aa" ]
# l.append(5)
# print l
# l.insert(10,1223)
# print l
# ==============================================
# l = [ 1 , 2 , 3 , "aa" ]
# print l.count(3)  #统计()内输入值的个数
# print l.index('aa',0,3) #输出()内的值第一次出现的 索引值,0是起始索引值,3是终止索引值
# =============================================


# ===============================
# a = [1,3,2,4]
# b = [2,2]
# print a + b
# print a * 2
# print max(a)
# print min(a)
# print len(a),a.__len__()
# a.sort()
# print a
# a.reverse()
# print a
# ===================================
# 打印列表里的 汉字
# a = ["哈哈","呵呵"]
# print str(a).decode("string_escape")
# =====================================
# 先找出列表里某个元素的全部索引 在这个元素出现的位置前 加个"a"
list = [0,1,2,3,2,4,4,4,4]
b = 0
num = 0
getnumber = 4
for i in range(list.count(getnumber)):
    if list.index(getnumber,b) :
         print '%d的索引有%d' % (getnumber,list.index(getnumber,b)-num)
         list.insert(list.index(getnumber, b), "a")
         num += 1
         b = list.index(getnumber, b) + 1
print list
print num
#
#

# ===================================

# "i am a coder"  将所有的a 都替换成大写
# a = "i am a coder"
# for x in range(0,len(a)-1):
#         if a[x] == 'a' :
#                 a = a[:x] + 'A'+ a[x+1:]
# print a


# =================================
#"i am a coder"   做到  首尾变大写  "I  AM A CodeR"
# a = "i am a coder"
# for x in a.split():
#         for y in range(len(x)):
#                 # print len(x)
#                 if  y == (len(x)-1) :
#                         x = x[:y] + x[y].upper() +x[y+1:]
#                 elif y == 0 :
#                         x = x[:y] + x[y].upper() + x[y + 1:]
#         print x,
# ====================================


