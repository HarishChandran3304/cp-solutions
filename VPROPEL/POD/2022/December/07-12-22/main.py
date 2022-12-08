m, n = map(int, input().split())
grid = [list(map(int, list(input()))) for i in range(m)]
queries = {int(input()): 0 for i in range(int(input()))} # Dict with counters for each query

points = tuple() # Extracting the 1s from the grid
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            points += ((i, j),)

def man_dist(p1, p2): # Function to calculate manhattan distance btw given 2 points p1 and p2
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

seen = set() # Set of all seen points
for p1 in points:
    for p2 in points:
        if p1 != p2 and p2 not in seen: # Finding a combination of 2 unique points
            queries[man_dist(p1, p2)] += 1 # Adding the distance to the respective query in the queries dict
    seen.add(p1) # Adding p1 to the set of seen points

for count in queries.values():
    print(count)