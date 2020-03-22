def numbers():
    operations = input('''
    
    1 for even
    2 for odd
    3 for prime
    ''')
    num1 = int(input("enter your first number"))
    num2 = int(input("enter your second number"))
    
    if operations == '1':
        for a in range(num1,num2):
            if a % 2 == 0:
                print(a)
                
    elif operations == '2':
        for b in range(num1,num2):
            if b % 2 != 0:
                print(b)
                
    elif operations == '3':               
        for a in range(num1,num2):
            if a > 1: 
                for b in range(2,a):
                    if a % b ==0:
                        break
                else:
                    print(a)

                
numbers()               

                



