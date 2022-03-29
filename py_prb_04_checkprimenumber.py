def  check_prime(n):
    temp=False
    for i in range(2,n):
        if n%i==0:
            temp=True
    if temp==False:
        return 1
    else:
        return 0
def prime_composite_list(l):
    l1=[]
    l2=[]
    l3=[]
    for j in l:
        if  check_prime(j)==1:
            l1.append(j)
        else:
            l2.append(j)
    l3.append(l1)
    l3.append(l2)
    return l3
if __name__=="__main__":
    l=[]
    count=int(input(""))
    for i in range(count):
        l.append(int(input("")))
    print( check_prime(l[1]))
    result=prime_composite_list(l)
    print(result)