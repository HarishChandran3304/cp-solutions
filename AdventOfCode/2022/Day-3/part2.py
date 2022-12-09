with open("input.txt") as f:
    rapsacks = f.read().split("\n")

lower = {chr(96+i): i for i in range(1, 27)}
upper = {chr(64+i): 26+i for i in range(1, 27)}
priorities = lower | upper

prio_sum = 0

for i in range(0, len(rapsacks), 3):
    group = rapsacks[i: i+3]

    for char in group[0]:
        if char in group[1] and char in group[2]:
            prio_sum += priorities[char]
            break

print(prio_sum)