print("Napíš celé číslo:")
n=int(input())		
        
for i in range(n):
    if i == 0 or i == n-1:
        for j in range(2*n+1):
            if j%2 == 0:
                print('X', end='')
            else:
                print(' ', end='')
                
    else:
        print('X', end='')
        for j in range(2*n-1):
            print(' ', end='')
        print('X', end='')
    print()