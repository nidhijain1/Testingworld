num=int(input())
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print("number is not prime"+ str(num))
            break
    else:
        print("number prime"+str(num))