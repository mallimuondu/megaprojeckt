a = input("greet the computer: ") # this greets you
print("answer " + a)

print("what is your name?")# this asks you your name

b = input("input your name ")
print("i like your name " + b )

print("this is what we have in our shop " "")
c = {
"milk" : 55,     
"honey" :  258,  
"egg" :  10  ,              
"Bread" :   50,        # This are the things in my shop
"spinach" : 55,   
"towel" : 256,   
"soda " : 50   
}
print(c)

k = c[input("type here what you want to buy: ")] #type what you want to buy
print(k)
l = c[input("type here your second item that you want to buy: ")] #type your second item that you want to buy

print(l)
 
m = k + l #this for adding all the things you have bought
print("amount payable " + str(m))# this prints the addition

n = input("how much do you have: ")
o = int(n)
p = o - m
print(p)

