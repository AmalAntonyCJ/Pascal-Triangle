def pascal_triangle (n):
    for i in range (1,n+1):
        for j in range (n-i,0,-1):
            print (end=' ')
        c=1
        for k in range (1,1+i):
            print (c,end=' ')
            c = int (c*(i-k)/k)
        print (' ')

pascal_triangle (6)