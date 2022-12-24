import re

s = input()

pattern = r'([a-z])\1{1,}'
# `([a-z])` captures a [a-z] character and `\1{1,}` matches 1 or more characters from that group

while True:
    if s == "*":
        print(1)
        break
    elif " *" in s:
        s = s.replace(" *", "")
    elif "*" in s:
        s = s.replace("*", "")
    
    else:
        match = re.search(pattern, s)
        if match:
            start, end = match.span()
            s = s.replace(match.group(), "*", 1)
        else:
            print(0)
            break