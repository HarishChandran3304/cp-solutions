p = int(input())
m, n = map(int, input().split())
moves = {
    "l": (lambda m, n: (m, n-1) if n>0 else (m, n)),
    "r": (lambda m, n: (m, n+1) if n<p-1 else (m, n)),
    "u": (lambda m, n: (m+1, n) if m<p-1 else (m, n)),
    "d": (lambda m, n: (m-1, n) if m>0 else (m, n))
}

for i in range(int(input())):
    m, n = moves[input()](m, n)

if (m, n) == tuple(map(int, input().split())):
    print("Win")
else:
    print("Lose")