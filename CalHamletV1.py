def getText():
    txt=open('Hamlet.txt','r').read()
    txt=txt.lower()
    for ch in '!""#$%^&*()_-+=[]{}\|;:,<.>/?''':
        txt=txt.replace(ch,'')
    return txt

hamletTxt=getText()
words=hamletTxt.split()
counts={}
for word in words:#建立（词：词频）字典
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[-1],reverse=True)#对统计出来的词频进行排序
for i in range(10):#只取前十
    word,count=items[i]
    print('{0:<10}{1:>5}'.format(word,count))
