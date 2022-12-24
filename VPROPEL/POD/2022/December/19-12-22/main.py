a = int(input())

print(len(tuple(((i, a//i) for i in range(1, int(a**0.5)+1) if a%i==0 and i!=a//i))))