def revtriangle(rows):
    for i in range(0,rows):
        for j in range(rows-i,0,-1):
            print(j,end=' ')
        print("")
rows = int(input())
revtriangle(rows)