#SevenDigitsDrawV1.py
import turtle as t
def drawLine(draw):#绘制单段数码管
    t.pendown() if draw else t.penup()
    t.fd(40)
    t.right(90)
def drawDigit(digit):#根据数字绘制一个七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,8,9] else drawLine(False)
    t.left(180)
    t.penup()#移到下一个起点处
    t.fd(20)
def drawDate(date):#获得要输出的数字
    for i in date:
        drawDigit(eval(i))#通过eval()函数将数字变为整数
def main():
    Date=input('')
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
#    drawDate('20181209')
    drawDate(Date)
    t.hideturtle()
    t.done()
main()
