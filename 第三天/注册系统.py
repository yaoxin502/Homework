'''
5.开发一个注册系统，
页面：
[{name:xxx,age:xxx},xxx]
----------------
*   1-新增用户
*   2-查询用户
*   3-删除用户
----------------
功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
功能2：查询学生信息
功能3：删除学生信息
'''


def print_menu():
    """打印提示功能"""

    print('1.新增学生信息')
    print('2.查询学生信息')
    print('3.删除学生信息')

# 定义一个列表，用来存储所有的学生信息
stu_info = []
def add_info():
    """新增学生信息"""
    add_name = input('请输入学生姓名：')
    add_age = input('请输入学生年龄：')
    #判断是否可以添加
    for info in stu_info:
        if info['name'] == add_name:
            print('学生姓名已存在，请重新输入。')
    #定义一个字典，用来存储添加的学生信息
    info = {}
    info['name'] = add_name
    info['age'] = add_age
    # 向列表中添加这个字典
    stu_info.append(info)
    print('增加成功。')

def query_info():
    """查询学生信息"""
    query_name = input('请输入要查询的学生姓名：')
    for info in stu_info:
        if info['name'] == query_name:
            print(f'查询到的信息是:\n{info["name"]}:{info["age"]}')
        else:
            print('没有找到该学生。')

def del_info():
    """删除学生信息"""
    del_name = input('请输入要删除的学生姓名：')
    for info in stu_info:
        if info['name'] == del_name:
            del info['name']
            print('已删除改学生。')
        else:
            print('您输入的姓名有误，请重新输入。')


def main():
    while True:
        print_menu()
        key = int(input('请输入功能对应的数字：'))
        if key == 1:
            add_info()
        elif key == 2:
            query_info()
        else:
            del_info()

main()

# def function():
#     print_menu()
#     key = int(input('请输入功能对应的数字：'))
#     if key == 1:
#         add_info()
#     elif key == 2:
#         query_info()
#     else:
#         del_info()
#
# function()
