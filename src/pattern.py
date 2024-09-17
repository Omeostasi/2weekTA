for i in range(5):
    for j in range(0, i): #i 0 j 0 doesnt i 1 j0 does print
        if j!=i:
            print('*', end=' ')
    print('*')    
for i in range(4, 0,-1):
    for j in range(i, 0,-1): #i 0 j 0 doesnt i 1 j0 does print
        if j!=i:
            print('*', end=' ')
    print('*')    
        
# Print the pattern
