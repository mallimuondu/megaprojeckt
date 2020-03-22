def evennumbers(): 
    num1 = input("entere the number which you want to start form :")
    num2 = input("entere the second number which you want it to end :") 
    for b in range(num1,num2):
        if(b % 2 == 0):
            print(b)
            
evennumbers()