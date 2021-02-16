x=11
print(x)
print("data type of x",type(x))#x is object of class int and class is user define data type so data type of x is class int
print("id of x:",id(x))#gives uique id


y=12
z=12
print("id of y:",id(x))#id of y and z is same bacause reffering to same value so refference count of 12 is 2
print("id of z:",id(z))


z=z+1
print("id of z:",id(z))#id will change because now y and z not reffering to same value i.e 11 now z having value 13
