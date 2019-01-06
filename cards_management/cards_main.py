#名片管理系统的主程序
from cards_tools import *
#显示主菜单
while True:
    print('*'*50)
    print('欢迎使用【名片管理系统】V1.0\n\n\
1.新建名片\n2.查看全部\n3.查询名片\n\n0.退出系统')
    print('*'*50)
#根据用户输入，决定后续操作
    action=input('请选择操作功能：')
    if action in ['1','2','3','4']:
        if action=='1':
            new_cards()
        elif action=='2':
            show_cards()
        elif action=='3':
            search_cards()
    elif action=='0':
        print('欢迎再次使用【名片管理系统】')
        break
    else:
        print('输入错误，请重新输入')
