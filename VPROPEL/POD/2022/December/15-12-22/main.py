s = input()
n = int(input())

for i in range(0, len(s)-n+1):
    sub = s[i: i+n]
    for char in sub:
        if char in "aeiou":
            break
    else:
        print(sub)