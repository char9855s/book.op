# 用户
root = ''
dict_root = {'root': 'root'}
# -------------------
# 图书信息
list_book = ['测试']  # 图书目录
list_root = ['root']  # 借出人名字
list_number = [3]  # 图书数量


# -------------------
# 登录系统
def dl():
    n = 0
    global root
    print("请按照提示输入内容：")
    while True:
        root = input("请输入账号:")
        password = input("请输入密码：")
        if root in dict_root:
            if password == dict_root[root]:
                print("欢迎%s登录图书管理系统" % root)
                return True
        print("账号或密码错误请重新输入")
        n += 1
        if n == 3:
            print("多次错误程序退出。")
            return


# ----------------------------
# 注册系统
def zc():
    print("输入000退出注册")
    while True:
        root = input("请输入账号：")
        if root in list_root:
            print("账号重复，请重新输入。")
            continue
        if root=='000':
            return
        password = input("请输入密码：")
        if input("请重新输入密码："):
            dict_root[root] = password
            return
        else:
            print("前后两次输入密码不一样请重新输入：")


# --------------------------------
# 查询系统
def cx():
    a = input("1.输出全部图书信息\t2.搜索书名")
    if a == '1':
        for i in range(len(list_book)):
            print('图书名称', list_book[i] + '\t剩余数量',
                  list_number[i])
    elif a == '2':
        book = input("请输入书名：")
        print('图书名称', list_book[list_book.index(book)] + '\t剩余数量',
              list_number[list_book.index(book)])
    return


# ---------------------------------
# 借书系统
def js():
    book = input("请输入书籍的名称:")
    if book in list_book:
        print("当前图书剩余数量为：", list_number[list_book.index(book)])
        if list_number[list_book.index(book)] == 0:
            print("书籍剩余数量不足，无法外借。")
        else:
            while True:
                a = input("是否要借此书：是\否")
                if a == '是':
                    print("成功登记")
                    list_root[list_book.index(book)] = root
                    list_number[list_book.index(book)] -= 1
                    return
                elif a == '否':
                    print("不借此书。")
                    return
                else:
                    print("输入不合法，请重新输入")


# --------------------------
# 管理员操作界面
def gly():
    while True:
        if root == 'root':
            print("1.图书入库\t2.查看图书信息")
            print("3.图书出库\t4.退出")
            a5 = input("请输入编号：")
            if a5 == '1':
                list_book.append(input("请输入图书名字："))
                list_root.append("无")
                list_number.append(int(input("请输入图书数量：")))
            elif a5 == '2':
                for i in range(len(list_book)):
                    print("书名：", list_book[i] + '\t出借人：', list_root[i] + '\t剩余数量：', list_number[i])
            elif a5 == '3':
                book = input("请输入书名：")
                if list_root[list_book.index(book)] != '无':
                    print("当前图书有人借出，借出人为：", list_root[list_book.index(book)])
                    if input("确认要删除吗：是\否") == '是':
                        list_root.pop(list_book.index(book))
                        list_number.pop(list_book.index(book))
                        list_book.pop(list_book.index(book))
                        print("已成功删除。")
                    else:
                        print("取消操作")
            elif a5 == '4':
                return
        else:
            print("您无权访问此界面")
            return


# ------------------------------
# 主程序区域
print("欢迎来到图书管理系统，请选择进入方式")
a = input("1.登录\t 2.注册\n")
if a == '1':
    a2 = dl()
elif a == '2':
    zc()
    a2 = dl()
else:
    print("输入不合法，程序自动退出")
if a2 == True:
    while True:
        print("请选择您需要的功能：")
        print("1.查询系统\t2.借书系统\n" +
              "3.管理员操作界面. \t 4.退出")
        a1 = input("请输入编号：")
        if a1 == '1':
            zc()
        elif a1 == '2':
            js()
        elif a1 == '3':
            gly()
        elif a1 == '4':
            break
