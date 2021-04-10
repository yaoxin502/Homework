#conding:utf-8
# f = open('data.txt','w')
# f.write('hello world\n123\n哈喽')
# f.close()

f = open('data.txt')
content = f.readlines()
print(content)
f.close()

# f = open('data.txt')
# content = f.readline()
# print(content)
# content = f.readline()
# print(content)
# f.close()

# f = open('data.txt')
# f.seek(5)
# content = f.read()
# print(content)
# f.close()