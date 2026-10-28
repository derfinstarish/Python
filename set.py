# x={2,3,4,9,'py',23}
# x.add('osc')
# x.remove('py')
# x.clear()
# print(x)

x={2,3,4,9,'py',23}
y={78,3}
# z=x.union(y)
# z=x.intersection(y)
# z=x.difference(y)
z=x.symmetric_difference(y)
print(z)
