# def gen(n):
#     i=1
#     while i<=n:
#         yield i
#         i=i+1

# n= int(input("enter a any no"))

# var = gen(n)
# print(var)
# print(next(var))
# print("hello")
# print("hii")

# basically generator banane ke bbad hamara control rahta hai usko kab print kare kha aur  iske liye yeild keyword aur next keyword use karte hai
# yeild keyword jo genertor instanace hold 
# return value hold karta hai aur yield generator instance hold karta hai 

# ==================================================================================================
def gen(n):
    i=1
    while i<=n:
        yield (i)
        i=i+1

n= int(input("enter a any no"))

var = gen(n)
print(next(var))
print(next(var))




