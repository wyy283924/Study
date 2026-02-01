from flask import Flask, render_template, request, redirect

# 创建一个Flask实例
app = Flask(__name__)

# 添加一个路由
@app.route('/')
def hello_world():
    if request.method == 'GET':
        return redirect('login')

# 添加登录界面的路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print('666')
        return render_template('login2.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return "Please provide both username and password", 400
        print(username)
        print(password)
        # 如果用户名是admin，密码是123456，则登录成功，进入后台页面
        if username == 'admin' and password == '123456':
            return redirect('admin')
        else:
            return render_template('login2.html')

#定义一个员工字典列表，里面key字段分别是：名字、年龄、职位、编号
employee_dict = [
        {'name': '张三', 'age': 18, 'position': 'Python开发工程师', 'id': 1},
        {'name': '李四', 'age': 20, 'position': 'Java开发工程师', 'id': 2},
        {'name': '王五', 'age': 22, 'position': '测试工程师', 'id': 3},
        {'name': '赵六', 'age': 24, 'position': '运维工程师', 'id': 4},
    ]


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    #让employee_dict按照id进行排序
    employee_dict.sort(key=lambda x:int(x['id']))
    return render_template('admin.html', employee_dict=employee_dict)

# 添加一个路由，关于新增员工
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        # 获取表单数据
        name = request.form.get('name')
        age = request.form.get('age')
        position = request.form.get('position')
        id = request.form.get('id')
        # 定义一个新的员工字典
        new_employee = {'name': name, 'age': age, 'position': position, 'id': id}
        # 将新员工字典添加到员工字典列表中
        employee_dict.append(new_employee)
        return render_template('admin.html', employee_dict=employee_dict)


# 添加一个路由，关于删除员工。在admin.html点击删除后，跳转到delete.html页面，然后输入想要删除的员工编号
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'GET':
        return render_template('delete.html')
    elif request.method == 'POST':
        # 获取表单数据
        id = request.form.get('id')
        # 遍历员工字典列表
        for employee in employee_dict:
            # 如果员工字典中的id和传入的id一致
            if employee['id'] == int(id):
                # 删除员工字典
                employee_dict.remove(employee)
                return redirect('admin')
        return render_template('admin.html', employee_dict=employee_dict)

# # 添加一个路由，关于修改员工信息
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     # 定义一个员工字典列表，里面key字段分别是：名字、年龄、职位、编号
#     employee_dict = [
#         {'name': '张三', 'age': 18, 'position': 'Python开发工程师', 'id': 1},
#         {'name': '李四', 'age': 20, 'position': 'Java开发工程师', 'id': 2},
#         {'name': '王五', 'age': 22, 'position': '测试工程师', 'id': 3},
#         {'name': '赵六', 'age': 24, 'position': '运维工程师', 'id': 4},
#     ]
#     if request.method == 'GET':
#         # 遍历员工字典列表
#         for employee in employee_dict:
#             # 如果员工字典中的id和传入的id一致
#             if employee['id'] == id:
#                 # 将该员工字典返回给前端页面
#                 return render_template('update.html', employee=employee)
#     elif request.method == 'POST':
#         # 获取表单数据
#         name = request.form.get('name')
#         age = request.form.get('age')
#         position = request.form.get('position')
#         # 遍历员工字典列表
#         for employee in employee_dict:
#             # 如果员工字典中的id和传入的id一致
#             if employee['id'] == id:
#                 # 更新员工字典中的数据
#                 employee['name'] = name
#                 employee['age'] = age
#                 employee['position'] = position
#                 # 跳出循环
#                 break
#         return render_template('admin.html', employee_dict=employee_dict)

# 启动Flask应用
if __name__ == '__main__':
    app.run()