with open("input.txt", "r") as f:
    deers = f.read().split("\n\n")

print(sum(sorted([sum(map(int, deer.split("\n"))) for deer in deers], reverse=True)[:3]))