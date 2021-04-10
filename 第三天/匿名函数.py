# def fn1():
#     return 200
# print(fn1)
# print(fn1())
#
# fn2 = lambda: 100
# print(fn2)
# print(fn2())

# add = lambda a,b: a+b
# result = add(1,2)
# print(result)

students = [
 {'name': 'TOM', 'age': 20},
 {'name': 'ROSE', 'age': 19},
 {'name': 'Jack', 'age': 22} ]
students.sort(key=lambda x:x['name'])
# students.sort(key=lambda x:x['age'],reverse=True)
print(students)
