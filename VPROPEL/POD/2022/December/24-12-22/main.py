w = input()
n = len(w)
l = [None]*n

for i in range(n):
    l[int(input())-1] = w[i]

print("".join(l))

for c in l:
    print(w.index(c)+1)