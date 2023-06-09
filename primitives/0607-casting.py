x = 7.0
y = 7

# Casting
print(type(x))
print(type(y))

print(x, int(x))
print(y,float(y))


x = int(1)   
y = int(2.8)
z = int("3")
print(x, type(x)) # 1
print(y, type(x)) # 2?
print(z, type(x)) # string 3

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x, type(x)) # 1.0, float
print(y, type(y)) # 2.8 , float
print(z, type(z)) # 3.0, float
print(w, type(w)) # 4.2 float


x = str("s1")
y = str(2)
z = str(3.8)
print(x, type(x)) # "s1", string 
print(y, type(y)) # "2", string
print(z, type(z)) # "3.8", string