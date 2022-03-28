def fun():
    list=[1,2,3,4,5,6,7]
    i=0
    while i<len(list):
        if i%2==0:
            print(i,"even no")
        else:
            print(i,"odd")
        i+=1
fun()