# def user_info(name,age,gender):
#     print(f'名字：{name}，年龄：{age}，性别：{gender}')
# user_info('Tom',age=16,gender='女')


# def user_info(name,age,gender='男'):
#     print(f'名字：{name}，年龄：{age}，性别：{gender}')
# user_info('Tom',20)
# user_info('Rose',18,'女')

# def user_info(*args):
#     print(args)
# user_info('Tom')
# user_info('Tom',18,'男')
# list1 = [1,2,3]
# user_info(*list1)
# user_info()

def user_info(**kwargs):
    print(kwargs)
user_info(name='Tom',age=18,id=110)
dict1 = {'name':'Rose','age':20,'id':111}
user_info(**dict1)