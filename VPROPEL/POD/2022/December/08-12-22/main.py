n = int(input())
l = list(range(2, n+1, 2))
ans = 1
i = 2

while True:
    if l == [1]*(n//2):
        break
    
    if [n%i for n in l].count(0)>0:
        for x in range(len(l)):
            if l[x]%i == 0:
                l[x] //= i
        ans *= i        
        i = 2
    else:
        i+= 1

if ans > 10**7:
    print("No such number in range")
else:
    print(ans)