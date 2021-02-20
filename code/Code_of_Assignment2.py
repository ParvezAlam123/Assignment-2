iteration=int(input('Enter number of iteration: '))
for i in range(iteration):
    n=int(input('Enter total number of orange: '))
    A=(n-3)/n
    B_A=(n-4)/(n-1)
    C_AB=(n-5)/(n-2)
    E=A*B_A*C_AB
    print("probability of approving box for sale is:",E)


