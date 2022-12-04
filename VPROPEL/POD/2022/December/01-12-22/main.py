n = int(input())
m = [[int(input()) for i in range(n)] for j in range(n)]

edges = [] #List to store all edges in clockwise order
edges += [m[0][i] for i in range(n)] #Getting Top edges
edges += [m[i][n-1] for i in range(1, n)] #Getting Right edges
edges += [m[n-1][i] for i in range(n-2, -1, -1)] #Getting Bottom edges
edges += [m[i][0] for i in range(n-2, 0, -1)] #Getting Left edges

edgesToBeRotated = edges[::2] #Getting the edges that need to be rotated (Alternate edges)
edgesInPosition = edges[1::2] #Getting the edges that are already in position
edgesAfterRotation = edgesToBeRotated[1::] + [edgesToBeRotated[0]] #Rotating the edges that need to be rotated
finalEdges = [None]*2*len(edgesToBeRotated) #Creating a list for rotated edges with None's as place holders
finalEdges[::2], finalEdges[1::2] = edgesAfterRotation, edgesInPosition #Intertwining both the lists

#Replacing all the edges with finalEdges in clockwise order
for i in range(n): m[0][i] = finalEdges.pop(0) #Replacing top edges
for i in range(1, n): m[i][n-1] = finalEdges.pop(0) #Replacing right edges
for i in range(n-2, -1, -1): m[n-1][i] = finalEdges.pop(0) #Replacing bottom edges
for i in range(n-2, 0, -1): m[i][0] = finalEdges.pop(0) #Replacing left edges

for row in m:
    print("\t".join(map(str, row)), end="\t\n")