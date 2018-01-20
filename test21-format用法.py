# coding:utf-8
# 1.通过索引填充
# print "I {0} AN {1} ED" .format("hh","xx")  #参数按照顺序0,1..
# print "I {} AN {} END" .format("hh","xx")  #不写的话 按默认顺序0,1...
# print "I {0} AN {1} END{1} no {0}" .format("hh","xx")  #同一参数可以填充多次

# =================================
# 2.通过key来填充
# print "hhh {n} sdasd i am {m}" .format(m="sssss",n="dasdsadsd")
# =====================================

# 3.通过下标
# name = ["a","b","c"]
# print "ni {n[0]} hao {n[1]} zhen {n[2]}" .format(n=name)  #重命名
# print "ni {0[0]} hao {0[1]} zhen {0[2]}" .format(name)  #默认参数
# =====================================
# 4.通过字典填充
# name = {"a":"zzz","b":"lll"}
# print "hello {n[a]} I AM {n[b]}" .format(n=name)  #重命名
# print "hello {0[a]} I AM {0[b]}" .format(name)     #默认
# ======================================
# 5.通过类填充
# class Name:
#     name1 = "zzz"
#     name2 = "lll"
# print "hello {name.name1} i am {name.name2}" .format(name = Name)
# =======================================
# 6.定义成函数
# f = "hello {0} i am {1}".format
# print f("aaa","sdd")
# ========================================
# 7.使用魔法参数 *代表元组或列表 **代表字典
a = ["ssdasd","ioiiooioio"]
b = {"name1":"zidian1","name2":"zidian2"}
print "hello {name1} {1} i {0} am {name2}".format(*a,**b)