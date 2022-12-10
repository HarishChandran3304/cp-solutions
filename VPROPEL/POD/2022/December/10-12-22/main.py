l = [int(input()) for i in range(int(input()))] # Getting input as list of numbers l = [1, 2, 3, ...]

def highest_pfs(n: int): # Takes and int n and finds its highest proper factor
    for i in range(n//2, 0, -1): # Iterate from n/2 to 1
        if n%i==0: # If n is divisible i
            return i # i is the highest proper factor so return it

highest_pfs_list = [highest_pfs(n) for n in l] # Makes a list of hpf of all elements in the orignal list

for i in range(len(l)-1): # Iterating 
    if max(highest_pfs_list[i+1:]) <= highest_pfs_list[i]: # Check for given condition
        print(l[i]) # Print i if above condition is satisfied
print(l[-1]) # Last number is always included so print it