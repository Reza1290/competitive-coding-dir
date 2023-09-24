R, C = [int(x) for x in input().split()]

matrix = []


for i in range(R):        
    
    a = [int(b) for b in input().split()]
    
    matrix.append(a)
    

max = 0


for i in range(R):
    for j in range(C):
        if(max == 0):
            max = matrix[i][j]
        if(matrix[i][j] > max):
            max = matrix[i][j]
        
    print(max)
    max = 0
