#函数化编程（功能函数化）
cards_list=[]
def new_cards():
    '''新建名片
    '''
    print('*'*50)
    print('新建名片')
    
    #提示用户输入名片信息
    name=input('请输入名字：')
    phone=input('请输入电话：')
    qq=input('请输入QQ：')
    email=input('请输入邮箱：')
    
    #将用户信息保存到一个字典
    card_dict={'name':name,
               'phone':phone,
               'qq':qq,
               'email':email
               }
    
    #将用户字典添加到列表
    cards_list.append(card_dict)
    
    #提示用户添加成功
    print('成功添加{}的名片'.format(name))

    #返回主菜单
    input('回车返回主菜单：')


    
def show_cards():
    '''显示全部
    '''
    print('*'*50)
    print('显示全部')
    #判断是否有名片记录
    if len(cards_list)==0:
        print('提示：没有任何名片记录')
        return
    #打印表头
    for name in ['姓名','电话','QQ','邮箱']:
        print(name,end='\t\t')
    print('')

    #打印分割线
    print('='*50)
    for card_dict in cards_list:
        print('{0}\t\t{1}\t\t{2}\t\t{3}'.format(card_dict['name'],
                                                card_dict['phone'],
                                                card_dict['qq'],
                                                card_dict['email'],
                                                ))
    
    
def search_cards():
    '''查询名片
    '''
    print('*'*50)
    print('查询名片')
    #提示要搜索的姓名
    find_name=input('请输入要搜索的姓名：')

    #遍历查找
    for card_dict in cards_list:
        if card_dict['name'] == find_name:
            find_card=card_dict
            for name in ['姓名','电话','QQ','邮箱']:
                    print(name,end='\t\t')
            print('')
            print('-'*50)
            print('{0}\t\t{1}\t\t{2}\t\t{3}'.format(card_dict['name'],
                                                card_dict['phone'],
                                                card_dict['qq'],
                                                card_dict['email'],
                                                ))
            print('-'*50)
            #针对找到的字典进行后续操作：修改，删除,返回上一级
            deal_card(find_card)
            break
        else:
            print('没有找到{}'.format(find_name))

def deal_card(find_card):
    ''' 针对找到的字典进行后续操作：修改，删除,返回上一级
    '''
    action_str=input('请输入要执行的操作[1] 修改 [2] 删除 [0] 返回上一级：')
    if action_str=='1':
        find_card['name']=input_card_info(find_card['name'],'请输入名字（回车不修改）：')
        find_card['phone']=input_card_info(find_card['phone'],'请输入电话（回车不修改）：')
        find_card['qq']=input_card_info(find_card['qq'],'请输入QQ（回车不修改）：')
        find_card['email']=input_card_info(find_card['email'],'请输入邮箱（回车不修改）：')
        print('%s的名片修改成功'%find_card['name'])
    elif action_str=='2':
        card_list.remove(find_card)
        print('删除成功')
    elif action_str=='0':
        return
    else:
        print('输入错误')


def input_card_info(dict_value,tip_massage):
    '''输入名片信息

    dict_value:字典原有值
    tip_massage:输入提示信息
    return: 如果有输入，返回输入内容，否则返回字典原有值
    '''
    #提示用户输入内容
    result_str=input(tip_massage)

    #针对用户输入进行判断，如果有输入，返回输入内容
    if len(result_str)>0:
        return result_str

    #如果没有输入，返回’字典中原有值‘
    else:
        return dict_value
