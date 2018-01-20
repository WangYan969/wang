# coding:utf-8
# 文件 的读取
# data =open('./util/ceshi.txt',"r")   # r表示读取文件
# data.close()                             #关闭读的文件
# print data.read()
# print data.readline()   # 不写参数表示读一行
# print data.readline(4)  # 写数字表示读取几个字符
# print data.readlines()   # 输出所有的
# print data.readlines()[0][-1] # 删除每一行的结尾

# for line in data :  #使用遍历读取文件
#     print line.strip(),  # 用于删除开头和结尾的内容,不写参数会删除 :包括'/n','/r','/t'," "
# ========================
#
# print data.read(3)
# print data.tell()
# print data.read(4)
# print data.tell()  # tell 返回光标所在位置
# data.seek(3,1)     #使光标偏移,正数代表向右,负数代表向左;后边的0:从文件开始,1:当前位置,2:文件结尾
# print data.tell()
# =========================
# import os
# os.rename('./util/ceshi.txt','./util/ceshi')  #同级目录修改文件名
# os.rename('./ceshi',"./util/ceshi.txt")
# os.remove('./util/ceshi.txt')            # 删除文件
# os.rmdir('./util')               # 删除目录
# os.mkdir("./util")                  # 创建目录
# ======================
# print __file__                      # __file__是当前文件的路径,精确到名字
# print os.path.dirname(__file__)     # os.path.dirname()是当前文件的目录
# print os.path.abspath(__file__)     # 是绝对路径的目录
# print os.path.join(os.path.dirname(__file__),"util/ceshi")
# =============================
# 文件的写入
f = open("ceshi2","w")   # 文件句柄,使用w时,事实上是创建了一个新文件,如果源文件存在,会覆盖
f.write("12334")
f.write('\nsdasd')

f = open("ceshi2","a")   # a表示追加
f.write("\n")   # 换行
f.write("the end")
f.close()