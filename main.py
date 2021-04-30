import math

def main():
    n = int(input())
    o=0
    for i in range(2, math.floor(n/2+1)):
        f = 1
        for j in range(2, math.floor(i/2+1)):
            if (i%j==0):
                f=0
        for j in range(2, math.floor((n-i)/2+1)):
            if((n-i)%j==0):
                f=0
        if(f==1):
            o=1
            break

    if(o==1):
        print("true")
    else:
        print("false")

main()