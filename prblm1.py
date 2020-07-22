n=int(input("Enter the value of n:"))
n=n*2
a=n*2-2
for i in range(0,n):
    if(i%2==0):
        for j in range(a):
            print(end='  ')
        a=a-1
        for j in range(0,i+1):
            print("* ",end='')
        print('\n')

