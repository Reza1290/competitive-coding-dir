terpanjang = 0

def combi(numbers, jumlah, data=[]):
    global terpanjang
    
    s = sum(data)
    if s <= jumlah:
        if(len(data) > terpanjang):
            terpanjang = len(data)
            
        
        
    if s >= jumlah:
        return  
    
    
    for i in range(len(numbers)):
        n = numbers[i]
        sisa = numbers[i + 1:]
        combi(sisa, jumlah, data + [n])
    
    
    

if __name__=="__main__": 
    
   
    A, B = [int (x) for x in input().split()]
    
    comb = []
    
    for i in range(0,A):
        x = int(input())
        comb.append(x)
    
    combi(comb,B)
    print(terpanjang)


