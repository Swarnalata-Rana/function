def fibo(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibo(number-1) + fibo(number-2)  
i=1
while i<11:
    print(fibo(i))
    i=i+1
