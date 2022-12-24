n = int(input()) 
s1 = [int(input()) for _ in range(n)]
s2 = [int(input()) for _ in range(n)]
xor = [int(input()) for _ in range(n)]

error = 0
real = []

for i in zip(s1,xor,s2):
    value = i[0]^i[1]
    real.append(value)
    error += abs(value-i[2])

print(*real, sep="\n")
print(error)