points = dict([tuple(map(int, input().split())) for i in range(int(input()))]) # Dict of all points where d={start: end}
p =  int(input()) # Checkpoint AKA starting and ending point of the loop
ctr = 0 # Number of times recursion function is called AKA no. of points in the loop

# Using recursion
def fn(start, ctr):
    if ctr and start == p: # Base case: return the counter if we arrive back at the checkpoint
        return ctr
    end = points.get(start) # Given a start point, returns the end point if it exists else returns None
    if end != None:
        return fn(end, ctr+1) # Re-calls the function with end point as the new start point and increments the counter
    else:
        return 0 # Loop is impossible

print(fn(p, ctr))