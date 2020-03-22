a = {
"milk" : 50,
"honey" : 120,
"bread" : 50
}

print(a)
b = a[input("type here what you want to buy: ")]
print(b)
c = a[input("type here your second item what you want to buy: ")]
print(c)

d = b + c
newD = str(d)
print(d)

e = input("whow much do you have: ")
f = int(e)

g = f - d
print(g)