# dict1 = {'name':'Tom','age':18}
# a,b = dict1
# print(a)
# print(b)
# print(dict1[a])
# print(dict1[b])

# def return_num():
#     return 100,200
# num1,num2=return_num()
# print(num1)
# print(num2)

# a,b=1,2
# a,b=b,a
# print(a)
# print(b)

def test1(a):
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))

b = 100
test1(b)

c = [11,22]
test1(c)