import math
def main():
    T = int(input())
    for i in range(T):
        L,R=input().split(" ")
        L=int(L)
        R=int(R)
        x =[]
        for num in range(L,R+1):
            if num>1:
                for i in range(2,int(math.sqrt(num))+1):
                    if (num % i) == 0:
                        break
                else:
                    x.append(num)
        print( -1 if len(x)==0 else max(x)-min(x))
       

main()