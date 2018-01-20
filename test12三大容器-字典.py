# coding:utf-8
# =============
#字典的两种取值方法
a = {"v":7,"x":4,"m":3}
# print a.get("z")
# print a["c"]
# =================
#字典的修改
# a["z"] = 22,333,222,333
# print a.get("z")
# =================
#字典的删除
# del a["z"]  #此种只删除一个 （后边如果用a.get()会报错）
# print a
#
# a.clear()  #将a里面全部清除 并且此时如果输出a 会报错
# peint a
# ===================
# 把字典的key和value表示出来

# for key,value in a.items():
#     print key,value
# ============================
# 单独打印 字典的key 和 value
# print a.values()
# print a.keys()
# ============================
# updata()是在其最后添加
# b = {"a":1,"aaa":2412434}
# a.update(b)
# print a
# =============================
# g="name@abc$age@18"
# m = {}
# for x in g.split("$"):
#     z= x.split("@")
#     m[z[0]] = z[1]
# print m
# ===============================
#正确的JSON是这样的：属性名必须用双引号包裹
