# coding=utf-8
i = range(1, 11)
for n in i:
    print '*' * n
    # print n
print '-' * 100

k = 10

i = range(1, k + 1)

for n in i:
    print '*' * k
    k -= 1

print '-' * 100

# coding:utf-8
rows = int(raw_input('please enter a rows! '))
i = j = k = 1
for i in range(0, rows):
    for k in range(0, rows - i):
        print "*",
        k += 1
    i += 1
    print "\n"

print '*' * 100

for i in range(0, rows + 1):  # 变量i控制行数
    for j in range(0, rows - i):  # (1,rows-i)
        print " ",
        j += 1
    for k in range(0, 2 * i - 1):  # (1,2*i)
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
                if k % 2 == 0:
                    print "*",
                else:
                    print " ",
            else:
                print "*",
        else:
            print " ",
        k += 1
    print "\n"
i += 1
