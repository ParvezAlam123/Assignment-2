iteration=int(input('Enter number of iteration: '))
for i in range(iteration):
    n=int(input('Enter total number of orange: '))
    P_X1=(n-3)/n
    P_X2_X1=(n-4)/(n-1)
    P_X3_X1X2=(n-5)/(n-2)
    P_E=P_X1*P_X2_X1*P_X3_X1X2
    print("probability of approving box for sale is:",P_E)


