n = int(input())

def getdigits(n):
    l = []
    
    while n > 0:
        d = n%10
        l.append(d)
        n //= 10
    
    return l

l = getdigits(n)
print(abs(sum(l[::2]) - sum(l[1::2])))