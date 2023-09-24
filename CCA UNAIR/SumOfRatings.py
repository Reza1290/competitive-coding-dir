 lst = [int(x) for x in input().split()]

max = 0
sum = 0
for i in range(0,lst[0]):
    x = [int(y) for y in input().split()]
    
    for j in range(1,5):
        sum = sum + x[j-1] * lst[j]
        
    if(sum > max):
        
        max = sum
        p = i+1
    
    sum = 0

print(p)