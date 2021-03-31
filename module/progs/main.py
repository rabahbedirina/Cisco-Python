import module as m 

lst=[i for i in range(5)]

print(m.suml(lst))
lst3=[m.prodl(lst) for x in  range(len(lst)) ]
print(lst3)
print(m.__counter)