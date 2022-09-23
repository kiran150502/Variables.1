a=1
b=2
c=4
print(a,b,c)
print(a) ; print(b) ; print(c)
print(a)
print(b)
print(c)
print(b,b,c)
print(v) # NameError: name 'v' is not defined


a=1 ; b=2 ; c=4
print(b)

a,n,y=5,7,9,3 # ValueError: too many values to unpack (expected 3)

a,b,c=3,4 # ValueError: not enough values to unpack (expected 3, got 2)


a,b,c,d=1,2,1,3
print(a,b,c,d)

a=c=1 ; b=2 ; d=3
print(a,b,c,d)

print('5th'.isidentifier())
print('tv_h'.isidentifier())
print('_'.isidentifier())



a=2 ; b=3
a,b=b,a
print(a)
print(b)