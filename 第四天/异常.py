# try:
#     print(num)
# except NameError:
#     print('有错误')

# try:
# #     print(1/0)
# # except(NameError,ZeroDivisionError):
# #     print('有错误')

# try:
#     print(1/0)
# except(NameError,ZeroDivisionError) as msg:
#     print(msg)

# try:
#     print(1/0)
# except Exception as msg:
#     print(msg)

try:
    f = open('test.txt','r')
except Exception as msg:
    f = open('test.txt','w')
else:
    print('无异常')
finally:
    f.close()