with open("input.txt", "r") as f:
    deers = f.read().split("\n\n")

print(max([sum(map(int, deer.split("\n"))) for deer in deers]))