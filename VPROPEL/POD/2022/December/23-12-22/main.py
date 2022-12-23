N = int(input())

def getpairs(n):
    pairs = []
    for i in range(2, n//2+1):
        if n%i == 0 and i<n//i:
            pairs.append((i, n//i))
    
    return pairs

def divcount(n):
    ctr = 0
    for i in range(2, n//2+1):
        if n%i == 0:
            ctr += 1
    
    return ctr

def d(n):
    ctr = 0
    pairs = getpairs(n)

    if pairs:
        for x, y in pairs:
            if divcount(x) == divcount(y):
                ctr += 1
        
        return ctr

    else:
        return -1

print(d(N))