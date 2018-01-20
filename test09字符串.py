# coding:utf-8
# ========================
# print "\'"  # \为转义符
# print r"\t" # 显示原始字符串
# print '''  保洁 ''' #在输出时保持原来的格式 但是不显示\t之类的 所以进行整合
# print r'''奥术大师多撒\1\2\e'''
# ========================

# 索引值左闭右开 左边从0开始 右边从-1开始
# a = "0123456789"
#
# print a[0] #取一个值
# print a[0:2] #取一个区间的值
# print a[0:] #默认到-1结束
# print a[:-1] #默认从0开始
# print a[-2:-1] #负数索引
# print a[5:2] #没有输出
# print a[10:] #没有输出
# ==============================
# name = "王山石"
# age = 20.1235
# country = "China\\"
#
# print "我的名字是%s,我的年龄是%s" % (name,age) # %s 把后面变量当做字符串输出
# print "我的名字是%s,我的年龄是%d" % (name,age) # %d 把后面变量当做整型输出
# print "我的名字是%s,我的国家是%r" % (name,country) # %r 把后面变量当做原使字符串输出
# print "我的名字是%10s,我的年龄是%s" % (name,age) # 在%s中 加数字 表示加空格(需减去原字符串的个数)
# print "我的名字是%10s,我的年龄是%.2f" % (name,age) # 在%f中 加.2 表示小数点后保留两位(四舍五入)
# print "我的名字是%10s,我的年龄是%10.2f" % (name,age) # 在%f中 加10.2 表示上两种的混合

# ===============================
#
# for x in "python":
#     print "当前字母是%3s" % x

# ===============================
# a = "i am a coder"
# print a.capitalize()  #首字母大写
# print a.__len__()   #长度
# print len(a)    #长度
# print a.upper() #全部大写
# print a.upper().lower()  #全部小写
# print a.split(" ")  #分割
# b = a.split()
# for x in b :
#     print x.capitalize(),
# print a.count("a",0,4)  #a在0~4出现的次数
# print a.find("a",8) #a在 从8开始 出现的首个索引值 没有则输出-1
#===================================
# b = 0
# for x in a :
#     if a.find("a",b) != -1:
#         print a.find("a", b)
#         b += a.find("a", b)+1
#上边是我的  下面是老师的

# 输出字符串里 a 的索引值
# i = -1
# while 1 :
#     i = a.find("a",i+1)
#     if i==-1:
#         break
#     print i
# =============================
# join 分隔
# b = "abcd"
# print " ".join(b)
# print "1".join(b)
# =================================
# encode编码 decode 解码
# c = u"嘿嘿"
# print c.encode("gbk")
# print c.encode("gbk").decode("gbk")
# ============

