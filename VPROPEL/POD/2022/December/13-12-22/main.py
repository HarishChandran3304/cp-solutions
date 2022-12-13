r1 = int(input())
c1 = int(input())
m1 = [list(map(int, input().split())) for i in range(r1)]

r2 = int(input())
c2 = int(input())
m2 = [list(map(int, input().split())) for i in range(r2)]

s = int(input())

def rcpairing(r, c):
    ctr = 0
    
    rowofm1 = m1[r]
    colofm2 = [row[c] for row in m2]
    for i in range(len(rowofm1)):
        if rowofm1[i] + colofm2[i] <= s:
            ctr += 1
        
    return ctr

for i in range(r1):
    for j in range(c1):
        print((rcpairing(i, j)), end="\t")
    print()