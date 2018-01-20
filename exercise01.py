# coding:utf-8
#  2018-01-18
# 1.声明1个方法 叫做quyu  再声明一个方法 ceshi
#		 ceshi有3个参数  第2个参数是方法,1,3是整数  执行ceshi 传入quyu
#		 如果能整除 返回 "恭喜你整除了" 如果不能 返回 余数是6
# def quyu(a,b):
#     if a % b == 0:
#         print "恭喜你整除了"
#     else:
#         print a % b
# def ceshi(a,c,b):
#     c(a,b)
# ceshi(2,quyu,3)
# ===================================================
# 2.把从ecl读出数据变成字典
# import xlrd
# data = xlrd.open_workbook("./util/dataBase.xls")
# sh = data.sheet_by_index(0)
# ncols = sh.ncols
# nrows = sh.nrows
# data = open("./util/ceshi1","a")
# for x in range(1,nrows):
#     content = {}
#     key1 = str(sh.row_values(0,1,3)[0])
#     value1 = sh.row_values(int(x),1,3)[0]
#     content[key1.encode("utf-8")] = value1.encode("utf-8")
#     key2 = str(sh.row_values(0,1,3)[1])
#     value2 = sh.row_values(int(x),1,3)[1]
#     content[key2.encode('utf-8')] = value2
#     data.write(str(content))
# data.close()
# 3.彩票将数据读出来
# import xlrd
# data = xlrd.open_workbook("./util/x3d.xls")
# sh = data.sheet_by_index(0)
# nrows = sh.nrows
# ncols = sh.ncols
# data = open("./util/caipiao","a")
# for x in range(1,nrows):
#     string = ""
#     string = string[0:]\
#              +str(sh.row_values(x,1,4)[0]) \
#              +str(sh.row_values(x,1,4)[1])\
#              +str(sh.row_values(x,1,4)[2])\
#              +string[:-1]
#     list = [string]
#     data.write(str(list))
# data.close()
#  上面这种方法输出的数字都有 ' ' 下面进行第二种方法的研究
import xlrd
data = xlrd.open_workbook("./util/x3d.xls")
sh = data.sheet_by_index(0)
nrows = sh.nrows
ncols = sh.ncols
data = open("./util/ceshi111","a")
all = []

for x in range(1,nrows):
    l = []
    l.append((sh.row_values(x,1,4)[0]+sh.row_values(x,1,4)[1]+sh.row_values(x,1,4)[2]).encode("utf-8"))
    eval(l)
    all.append(str(l[0]))

data.write(str(all))
data.close()

# l1=[123]
# l2=[222]
# la = [l1]
# la.append(l2)
# print la
