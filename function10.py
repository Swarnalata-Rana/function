def speed():
    i=70
    c=0
    while i<85:
        if i==70:
            print("okk")
        elif i%1==0:
            c+=1
        i+=1
    print(c)
    if c>12:
        print("licence suspend")
speed()