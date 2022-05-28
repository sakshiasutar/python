if __name__ == '__main__':
    n = int(input())
    s = 0
    for i in range(1,n+1):
        if i >= 10:
            print(i)
            s= s*10
        
        s = i + (s*10)    
    print(s)
