l = list(map(lambda x: x[::-1], [input() for i in range(int(input()))]))

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        l[i], l[i+1] = l[i+1], l[i]

for n in l:
    print(n[::-1])