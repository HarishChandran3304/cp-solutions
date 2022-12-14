c1 = [int(input()) for i in range(int(input()))]
m = int(input())

for n in sorted(c1):
    if n%m == 0:
        print(n)
        break
else:
    print("No multiple found")