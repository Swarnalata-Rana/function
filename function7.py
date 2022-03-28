def fun():
    i=0
    num2=int(input("enter 2nd number: "))
    while i<=num2:
        j=1
        while j<=12:
            print(i,"×",j,"=",i*j)
            j+=1
        i+=1
    print(" ")
fun()
