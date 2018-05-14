"""tuple """
a=(1,45,3,4,5,6,7,8,9)
print a
print hex(id(a))






a=("a",450)                      #immutable
print a
print hex(id(a))


"""list"""


b=[1,45,3,4,5,6,7,8,9]
print b
print hex(id(b))




b.append(" c")            #mutable
print b
print hex(id(b))






"""dictionary"""

b={"a":45,"b":597,"c":"prashant",7:"manish"}
print b

b["7"] = "anmol"
print b
b[7]="kumar"
print b


