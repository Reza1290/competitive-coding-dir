def cek_panjang(terdepan):
    return str(terdepan)*3

if __name__=="__main__": 
    i = int(input())
    data = [int (x) for x in input().split()]
    
    sorted_data = sorted(data,key=cek_panjang, reverse=True)
    
    hasil = [str(x) for x in sorted_data]
    
    for i in hasil:
        print(i,end='')
    
