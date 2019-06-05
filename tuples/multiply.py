
data=(1,2,3)
strin=("aaa","bbb")

##       
##def multiply(*args):
##    product=[]
##    multiply = 2
##    for arg in (args[0]):
##        product.append(arg * multiply)
##    print(product)
##    return product
##
##
##multiply(data)
##multiply(strin)



def multiply(*args):
    total = 2
    for value in args:
        total = total * value
    print(total)
    return total

multiply(data)
multiply(strin)
