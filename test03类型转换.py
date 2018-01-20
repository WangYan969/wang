# coding:utf-8
# a = '10+1'
# print type(a)
# # 将数据转换成字符串的方法 : str是内容,给人看;repr是所有,给机器看
# b = str(a)
# c = repr(a)
# print b,c
# # 用eval函数 测试上述 (eval函数 是将它里面的内容当做可执行代码执行并输出)
# print eval(b)
# d = eval(b)
# e = eval(c)
# print d,e

# # int()可讲数据转换为整型,里面若有非数字,则报错
# a = '3'
# b = 2.111
# c = '3ss'
# print int(a),type(a)
# print int(b),type(b)
# print int(c),type(c)
#float()可讲数据转换为float型,里面若有非数字,则报错
a = '22'
print float(a),type(a),type(float(a))