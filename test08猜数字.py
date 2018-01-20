# coding:utf-8
import random
b = random.randrange(1,100)
count =0
while 1 :

    c = int(raw_input())
    if b == c :
        count += 1
        print "对了"
        break

    if b > c :
        count += 1
        print '小了'
        continue
    if b < c :
        count += 1
        print '大了'
    continue
print count