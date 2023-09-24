
x = str(input())
lst = []
flag = 0
after = 0
numerics= "0123456789"
bef = '0'

for i in x:
    
    if(i in numerics):
        if(flag == 0):
            if(bef < i):
                if(int(i)-1 == int(bef) or bef == '0'):
                    lst.append(i)
                    after = 1
                    bef = i
            else:
                break;
            
    elif(after == 1):
        break;
    # print(i)
# for(i in lst)
if(after == 1):
    print(*lst, sep="")
else: 
    print('0')