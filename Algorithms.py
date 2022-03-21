import operator
# Алгоритмы!

# сортировка
dict_a = {2:5, 4:7,6:8, 2:5}
dict_b={6:8, 2:5}

# выводим сортировку
results={}
for i in (dict_a,dict_b):
    results.update(i)
    print(results)

# сортировка с алгоритмом
results=dict(sorted(results.items(),key=operator.itemgetter(1)))
print(results)

# сортировка reverse
results=dict(sorted(results.items(),key=operator.itemgetter(1),reverse=True))
print(results)
# The Endd COde

# самыми высокими значениями

a={'a':500,'b':5700,'c':400,'d':5300}
result4=sorted(a,key=a.get,reverse=True)[:2]
print(result4)
# end
# New
print(int('ABC',23))
# End

# New

n=7
p=[]

for i in range(n):
    row=[1]*(i+1)
    for j in range(i+1):
        if j!=0 and j !=i:
            row[j]=p[i-1][j-1]+p[i-1][j]
    p.append(row)

for r in p:
    print(r)
