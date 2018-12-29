def getNum():#依次输入数据
    nums=[]
    iNumStr=input('请输入数字（回车退出）：')
    while iNumStr!='':
        nums.append(eval(iNumStr))
        iNumStr=input('请输入数字（回车退出）：')
    return nums

def mean(numbers):#求平均数
    s=0.0
    for num in numbers:
        s=s+num
    return s/len(numbers)

def dev(numbers,mean):#求方差
    sdev=0.0
    for num in numbers:
        sdev=sdev+(num-mean)**2
    return sdev/len(numbers)

def median(numbers):#求中位数
    Num=sorted(numbers)#或者numbers.sort()整理numbers
    size=len(Num)
    if len(Num)%2==0:
        med=(Num[size//2-1]+Num[size//2])/2
    else:
        med=Num[size//2]
    return med

n=getNum()
m=mean(n)
print('平均值：{}，方差：{}，中位数：{}。'.format(m,dev(n,m),median(n)))
#print(m)
