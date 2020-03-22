def function():
    a = input("which number do you want to start from")
    b = input("which number do you want to end at")
    for b in range(a,b):
        if(b % 2 != 0):
            print(b)
function()