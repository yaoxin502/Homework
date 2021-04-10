# mystr = "hello world and superctest and chaoge and Python"
# print(mystr.find('and', 15, 30))
# print(mystr.index('ands'))

# print(mystr.count('and'))
# print(mystr.count('ands'))
# print(mystr.count('and',0,30))

# print(mystr.replace('and','he'))
# print(mystr.replace('and','he',1))

# print(mystr.split('and'))
# print(mystr.split('and',2))
# print(mystr.split(' '))
# print(mystr.split(' ',2))

# list1 = ['chao','ge','test','promotion']
# t1 = ('aa','b','cc','ddd')
# print('and'.join(list1))
# print(''.join(list1))
# print(' '.join(list1))
# print('...'.join(t1))

# mystr = "  hello world and supertest and chaoge and Python  "
# print(mystr.capitalize())
# print(mystr.title())
# print(mystr.lower())
# print(mystr.upper())
# print(mystr.lstrip())
# print(mystr.rstrip())
# print(mystr.strip())

# str1 = 'hello'
# print(str1.ljust(10,'.'))
# print(str1.rjust(10,'.'))
# print(str1.center(10,'.'))

# mystr = "hello world and supertest and chaoge and Python"
# print(mystr.startswith('hello'))
# print(mystr.startswith('hello',5,20))
# print(mystr.endswith('Python'))
# print(mystr.endswith('Python',2,20))

# mystr = 'hello'
# mystr1 = '123'
# print(mystr.isalpha())
# print(mystr1.isdigit())
# print(mystr.isalnum())
# print(mystr.isspace())


mystr = 'zhangsan lisi xiaoming xiaohong lisi'
name = input('输入姓名：')
if mystr.find(name) != -1:
    if mystr.count(name) > 1:
        print(f'有重名，重名个数为{mystr.count(name)-1}')
    else:
        print('无重名')
else:
    print('不在该班级')
