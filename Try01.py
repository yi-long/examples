#获取数字，建立列表并排序
'''def getNum():
    nums=[]
    iNumStr=input('请输入数字（回车退出）：')
    while iNumStr!='':
        nums.append(eval(iNumStr))
        iNumStr=input('请输入数字（回车退出）：')
    return nums
nums=getNum()
nums=sorted(nums)
print(nums)
print('请输入网址;')
url=input()
print('请输入文件名')
name=input()
print(url,name+'.pdf')'''
def is_palindrome(n):
    if n>0 and n<10:
        return True
    else:
        s=str(n)
        return s==s[::-1]
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
