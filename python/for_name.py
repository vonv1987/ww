#!/usr/bin/python
# -*- coding: UTF-8 -*-
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
# for i in range(len(names)):
# print names[i], 'is', ages[i], 'years old'
# print zip(names,  ages)
for x, y in zip(names, ages):
    print "%d号运动员,名字叫%s" % (y, x)
