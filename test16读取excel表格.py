# coding:utf-8
import xlrd
import os
data = xlrd.open_workbook("./util/dataBase.xls")
sh = data.sheet_by_index(0)
ncols = sh.ncols
nrows = sh.nrows
data = open("./util/ceshi","a")
for x in range(1,nrows):
    content = {}
    key1 =  str(sh.row_values(0,1,3)[0])
    value1 = sh.row_values(x,1,3)[0]
    content[key1.encode("utf-8")] = value1.encode("utf-8")
    key2 =  str(sh.row_values(0,1,3)[1])
    value2 = sh.row_values(x, 1, 3)[1]
    content[key2.encode("utf-8")] = int(value2)
    data.write(str(content))
data.close()