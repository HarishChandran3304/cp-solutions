input()
l = tuple(map(int, input().split()))
m = min(l)

if m == 1:
    print("NO")
else:
    for i in range(2, m+1):
        if not any(tuple(n%i for n in l)):
            print("YES")
            break
    else:
        print("NO")