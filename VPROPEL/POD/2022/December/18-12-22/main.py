d = dict(zip([chr(n) for n in range(97, 123)],[n for n in range(1, 27)]))
print(d)
s1 = input()
s2 = input()

s1diff = d[s1[1]] - d[s1[0]]
s2diff = d[s2[1]] - d[s2[0]]

if len(s1) != len(s2):
    print("Length different")
for i in range(len(s1)-1):
    if s1[i].isspace():
        if s2[i].isspace():
            continue
        else:
            print("Strings differ in space")
    if d[s1[i+1]]-d[s1[i]] != s1diff or d[s2[i+1]]-d[s2[i]] != s2diff:
        print("Strings are not stepped")
else:
    print("Strings are stepped")