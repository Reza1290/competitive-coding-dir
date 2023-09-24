a, b, c, d = [int(x) for x in input().split()]
 
if(pow(a,b) - pow(c,d) > pow(a,c) - pow(b,d)):
    print("YA!")
elif(pow(a,b) - pow(c,d) < pow(a,c) - pow(b,d)):
    print("TIDAK!")
else:
    print("SAMA!")