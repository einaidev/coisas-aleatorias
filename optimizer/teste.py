dir = "C:\\Users\\Fernando Schmidt\\Documents\\pyPrograms\\optimizer\\regedits".replace('\\','/')
list = dir.split('/')
strg2 = ''
for i in dir.split('/'):
    if ' ' in i:
        position = list.index(i)
        strg = i.replace(i[0],"'"+i[0]).replace(i[-1],i[-1]+"'")
        list.insert(position,strg)
        list.remove(i)
for i in list:
    strg2 = strg2+i+"/"           