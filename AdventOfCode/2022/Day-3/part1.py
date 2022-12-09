with open("input.txt") as f:
    rapsacks = f.read().split("\n")

lower = {chr(96+i): i for i in range(1, 27)}
upper = {chr(64+i): 26+i for i in range(1, 27)}
priorities = lower | upper

prio_sum = 0
for rapsack in rapsacks:
    n = len(rapsack)
    compartment1 = rapsack[:n//2]
    compartment2 = rapsack[n//2:]

    for item in compartment1:
        if item in compartment2:
            misplaced = item
            break

    prio_sum += priorities[misplaced]

print(prio_sum)