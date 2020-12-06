import os
name_of_file = 'C:\\Users\\daria\\OneDrive\\Documents\\1\\data.txt'


def Sequence(filename):
    m = l = z = k = 0
    a = []
    c = []
    
    try:
        f = open(filename, 'r')
        for s in [s5 for s1 in f for s2 in s1.split(' ') for s3 in s2.split('\n') for s4 in s3.split(',') for s5 in s4.split('\t') if s5!='']:
            try:
                int(s)
            except:
                print('word ',s,' ignored',sep='')
            c.append(int(s))
            m=m+1
        m = int(m/2)
        for i in range(m):
            b = []
            for j in range(2):
                b.append(c[k])
                k = k + 1
            a.append(b)
        for i in range(m):
            for j in range(2):
                print(a[i][j],end=' ')
            print()
        for h in range(m):
            for g in range (m):
                if (a[h][0]<a[g][0]) and (a[h][1]<a[g][1]) and (a[h][1]>=a[g][0]) and (a[h][0]<a[g][1]):
                    a[h][1]=a[g][1]
                if (a[h][0]>a[g][0]) and (a[h][1]>a[g][1]) and (a[h][0]<=a[g][1]) and (a[h][1]>a[g][0]):
                    a[h][0]=a[g][0]
        print ('Введите первую координату отрезка')
        x = int(input())
        print ('Введите вторую координату отрезка')
        y = int(input())
        for v in range(m):
            if (x>=a[v][0]) and (y<=a[v][1]):
                z=1
        if z == 1:
            print ('Отрезак принадлежит объединению')
        else:
            print ('Отрезак не принадлежит объединению')
        return 0    
    except FileNotError:
        return None
        

average = Sequence(name_of_file)

if (average == None):
    print("Can't open file")
elif (average == ArithmeticError):
    print("Empty file")
