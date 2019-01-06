#TextProBar.py(Exercise)
'''import time
scale=50
print('执行开始'.center(scale//2,'-'))
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='-'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print('\r{:3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur))
    time.sleep(0.1)
print('\n'+'执行结束'.center(scale//2,"-"))'''
#ThreePowerFormat.py
'''a=eval(input('请输入一个实数：'))
b=pow(a,3)
print('{:-^20}'.format(b))
try:
    if a>=1e20:
        print(b)
except:
    pass'''
#AsteriskTriangle.py
'''a=eval(input())
for i in range(1,a+1,2):
    print('{:^{}}'.format('*'*i,a))
'''
i=0
while i<3:
    name=input()
    password=input()
    if name=='Kate' and password=='666666':
        print('load')
        break
    else:
        if i<2:
            print('name or password error;try again')
            i=i+1
        else :
            print('over 3')
            break
