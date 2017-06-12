print '\n9x9 Table\n'

for i in range(1, 10) :
    for j in range(1, i+1) :
        print j, 'x', i, '=', j*i, '\t',
        # print '%d x %d = %d\t' %(j, i, j*i),
    print '\n'

print '\nDone!'

print '-'*100


for i in range(1,10):
    for j in range(1,i+1):
        print "%d*%d=%2d\t " % (j,i,j*i),
    print '\n'

print '-'*100

from prettytable import PrettyTable
pt = PrettyTable()

pt.field_names=[i for i in range(1,10)]

mulp=[["{b}x{a}={c}".format(a=a,b=b,c=a*b) if a>=b else "" for b in range(1,10)] for a in range(1,10)]
map(pt.add_row,mulp)

print(pt)