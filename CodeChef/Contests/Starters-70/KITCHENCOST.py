# https://www.codechef.com/problems/KITCHENCOST

for i in range(int(input())):
    s = 0
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    for j in range(n):
        if a[j] >= x:
            s += b[j]
    
    print(s)