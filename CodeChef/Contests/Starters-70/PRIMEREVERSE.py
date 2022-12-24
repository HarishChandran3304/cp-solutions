# https://www.codechef.com/problems/PRIMEREVERSE

for i in range(int(input())):
    n = int(input())
    x = input()
    y = input()
    
    if x.count("1") == y.count("1"):
        print("YES")
    else:
        print("NO")