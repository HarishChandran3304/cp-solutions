# https://www.codechef.com/problems/KITCHENSPICE

for i in range(int(input())):
    l = int(input())
    if l < 4:
        print("MILD")
    elif l < 7:
        print("MEDIUM")
    else:
        print("HOT")