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
def print_info():
    """系统功能"""
    print('-'*20)
    print('欢迎登录学生管理系统')
    print('增加学生信息')
    print('查询学生信息')
    print('删除学生信息')
    print('-'*20)
# print_info()

info = []
def add_info():
    """增加学生信息"""
    new_name = input('请输入姓名：')
    new_age = input('请输入年龄：')
    #声明全局变量
    global info
    # 检测⽤户输⼊的姓名是否存在，存在则报错提示
    for i in info:
        if new_name == i['name']:
            print('该用户已存在。')
            return
    # 如果⽤户输⼊的姓名不存在，则添加该学员信息
    info_dict = {}
    # 将⽤户输⼊的数据追加到字典
    info_dict['name'] = new_name
    info_dict['age'] = new_age
    # 将这个学员的字典数据追加到列表
    info.append(info_dict)
    print(info)

def search_info():
    """查询学生信息"""
    search_name = input('请输入要查找的学生姓名：')
    global info
    # 判断学员是否存在：如果输⼊的姓名存在则显示这位学员信息，否则报错提示
    for i in info:
        if search_name == i['name']:
            print(f'查询到的信息是\n{i["name"]}:{i["age"]}')
            break
        else:
            print('该学生不存在')

def del_info():
    """删除学生信息"""
    del_name = input('请输入要删除的学生姓名：')
    global info
    #判断学员是否存在:如果输⼊的姓名存在则删除，否则报错提示
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
        else:
            print('该学生不存在')
        print(info)

while True:
    print_info()
    user_num = int(input('请选择您需要的功能序号：'))
    if user_num == 1:
        add_info()
    elif user_num == 2:
        search_info()
    else:
        del_info()
