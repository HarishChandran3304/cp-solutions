m, n, p, q = int(input()), int(input()), int(input()), int(input())
seating = [list(map(int, input().split())) for i in range(m)]
l = int(input())
a = [] # Answer list
t = q if l==p else p # Number to check for transition (Opposite of lucky number)

# A kid will be luck after transition if the t doesnt exist in his row and column before transition
for i in range(m):
    for j in range(n):
        row = seating[i]
        if t in seating[i]: # Checking if t exists in the row
            break # Break out of inner for if it does

        col = [row[j] for row in seating] 
        if t not in col: # Checking if t exists in the column
            break # Break out of inner for if it does
    else:
        a.append((i+1, j+1)) # Add coordinates of seat to answer list if t doesnt exist in row and column

if a: 
    for x, y in a:
        print(x, y)
else:
    print("No winner")