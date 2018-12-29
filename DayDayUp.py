def dayup(df):
    dayup=1
    for i in range(365):
        if i%7 in [6,0]:
            dayup=dayup*(1-0.01)
        else :
            dayup=dayup*(1+df)
    return dayup
dayfactor=0.01
dayupA=pow((1+0.01),365)
while dayup(dayfactor)<dayupA:
    dayfactor=dayfactor+0.001
print("B君工作日的努力参数是：{:.3f}\nA君一年后到达的程度：{:.2f}".format(dayfactor,dayupA))
