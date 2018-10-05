t=int(input()) #number of test cases
for _ in range(t):
    n=int(input()) # no. of array elements
    l=[int(x) for x in input().split()]  #array elements
    for i in range(1,n-1):
        if l.count(i)==2:  # using count function to count the elements
            print(i,end=' ')
    print()
