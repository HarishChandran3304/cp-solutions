a, b = map(int, input().split())
q = int(input())
queries = tuple(map(int, input().split()))
l = []

for i in range(1, max(queries)+2):
    if i == 1:
        l.append(a)
    
    elif i == 2:
        l.append(b)
    
    else:
        l.append(3*b+4*a)
        a, b = b, 3*b+4*a

print(" ".join([str(l[query-1]%(10**9+7)) for query in queries]))