# https://www.codechef.com/problems/MINDIST

def fn(s):
    indices = []
    for i, n in enumerate(s):
        if n == "1":
            indices.append(i)
    
    for i in range(len(indices)-1):
        nofzeroes = indices[i+1]-indices[i]-1
        if nofzeroes%2 == 0:
            return 1
    
    return 2

for i in range(int(input())):
    n = int(input())
    s = input()
    
    print(fn(s))