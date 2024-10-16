#  decotor is that we have to change the behaviour of  function code without  change the main code 
# def decor(fun):
#     def inner(x,y):
#         x=x+5
#         y=y+5
    
#         return fun(x,y)
#     return inner

# def addition(x,y):
#     return x+y

# p = int (input("enter a no 1"))
# q=int(input("enter no 2"))

# var = decor(addition)
# x=var(p,q)
# print(x)



# =================================================================
# def decor(fun):
#     def inner(x,y):
#         x=x+5
#         y=y+5
    
#         return fun(x,y)
#     return inner
# @decor                               # this is called decorator 
# def addition(x,y):
#     return x+y

# p = int (input("enter a no 1"))
# q=int(input("enter no 2"))

# x=addition(p,q)
# print(x)
# =============================================================
def decor(fun):
    def inner(x,y):
        x=x*y
        y=0
    
        return fun(x,y)
    return inner
@decor                               # this is called decorator 
def addition(x,y):
    return x+y

p = int (input("enter a no 1"))
q=int(input("enter no 2"))

x=addition(p,q)
print(x)




