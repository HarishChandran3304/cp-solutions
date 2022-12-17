input()
l = tuple(map(int, input().split()))

for i in range(2, min(l)+1):
    if not any(tuple(n%i for n in l)):
        print("YES")
        break
else:
    print("NO")