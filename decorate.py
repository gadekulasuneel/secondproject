def divdecor(func):
    def inner(a,b):
        if b==0:
            print("Unable To Execute Please Enter Valid Number")
        else:
            return func(a,b)
    return inner
@divdecor

def division(a,b):
    return a/b

print(division(10,2))
print(division(10,1))
print(division(10,0))