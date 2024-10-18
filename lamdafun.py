m=eval(input(" list::"))
print(list(map(lambda x:x**2,m)))
print(list(map(lambda x:"even" if x%2==0 else "odd",m)))