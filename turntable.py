import tkinter
#导入线程模块
import threading
import time #导入sleep,代码休眠

root=tkinter.Tk()#创建图形窗口
root.title('大转盘')
root.minsize(300,300)


#摆放按钮
btn1=tkinter.Button(root,text='樱桃',bg='red')
btn1.place(x=20,y=20,width=50,height=50)

btn2=tkinter.Button(root,text='香蕉',bg='white')
btn2.place(x=90,y=20,width=50,height=50)

btn3=tkinter.Button(root,text='苹果',bg='white')
btn3.place(x=160,y=20,width=50,height=50)

btn4=tkinter.Button(root,text='鸭梨',bg='white')
btn4.place(x=230,y=20,width=50,height=50)

btn5=tkinter.Button(root,text='榴莲',bg='white')
btn5.place(x=230,y=90,width=50,height=50)

btn6=tkinter.Button(root,text='柚子',bg='white')
btn6.place(x=230,y=160,width=50,height=50)

btn7=tkinter.Button(root,text='西瓜',bg='white')
btn7.place(x=230,y=230,width=50,height=50)

btn8=tkinter.Button(root,text='葡萄',bg='white')
btn8.place(x=160,y=230,width=50,height=50)

btn9=tkinter.Button(root,text='草莓',bg='white')
btn9.place(x=90,y=230,width=50,height=50)

btn10=tkinter.Button(root,text='芒果',bg='white')
btn10.place(x=20,y=230,width=50,height=50)

btn11=tkinter.Button(root,text='荔枝',bg='white')
btn11.place(x=20,y=160,width=50,height=50)

btn12=tkinter.Button(root,text='甘蔗',bg='white')
btn12.place(x=20,y=90,width=50,height=50)

#将所有选项组成列表
fruitlists=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12]

#是否开启循环
isloop=False
#是否停止
stopsign=False #是否收到stop信号用于进行stop信号
#存储停止id----->用于stop后的重新启动
stopid=None
def round():
    global isloop
    global stopid
    #判断是否开始循环
    if isloop==True:
        return    #条件为真，return之后的语句不再执行
    i=1
    if isinstance(stopid,int):
        i=stopid
    while True:
        #延时操作
        time.sleep(0.2)
        #将所有的组件背景色设为白色
        for i in fruitlists:
            i['bg'] = 'white'
        #将当前数值对应的组件变色
        print(type(fruitlists[i]))
        fruitlists[i]['bg']='red'#在IDLE中报错，在spyder中，显示fruitlists[i]的类型为<class 'tkinter.Button'>
        #变量+1
        i += 1
        print('当前i为',i)#用来追踪当前位置
        #如果i大于最大索引值，直接归零
        if i >= len(fruitlists):
            i=0
        if stopsign == True:
            isloop=False
            stopid=i#赋值stopid
            break

def stop1():#定义stop按钮,运行函数时，将stopsign变为True
        global stopsign
        if stopsign == True:
            return
        stopsign=True

#建立一个新线程的函数
def newtask():
    global isloop
    global stopsign
    #建立线程
    stopsign=False
    #print('stopsign={}'.format(stopsign))   #打印 点击开始时，stopsign的状态
    t=threading.Thread(target=round)
    #开启线程
    t.start()
    #设置循环开始标志
    isloop=True

#开始按钮
btn_start=tkinter.Button(root,text='start',command=newtask)
btn_start.place(x=90,y=125,width=50,height=50)

#停止按钮
btn_stop=tkinter.Button(root,text='stop',command=stop1)
btn_stop.place(x=160,y=125,width=50,height=50)

root.mainloop()
