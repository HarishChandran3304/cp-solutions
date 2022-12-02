d, k = input(), int(input()) 
n = len(d)
l = []

for i in range(2**(n)): 
    b = bin(i)[2:].zfill(n)
    if b.count("1") == k:
        l.append(("".join(([d[i]*int(b[i]) for i in range(n)]))))

for dna in sorted(l): print(dna)