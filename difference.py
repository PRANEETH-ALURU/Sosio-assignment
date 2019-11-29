def diff(n):
    sum1=0
    sum2=0
    for i in range(1,n+1):
#performing sum of squares of individual numbers
        sum1=sum1+i*i
#performing square of sum of the numbers
        sum2=sum2+i
    sum2=sum2**2
#calculating difference
    dif=sum2-sum1
    print(dif)


if __name__ == '__main__':
    N=int(input("Enter N"))
    diff(N)