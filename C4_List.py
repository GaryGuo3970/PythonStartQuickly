#1
spam=[1,2,3,5,8,13]
for i in spam:
    print(i)

#2
spam =[["Cat","Dog"],["A","B","C","D"]]
for i in spam:
    for j in i:
        print(j)

#3 负索引：从结尾倒序
spam = [1,2,3,4,5]
print(spam[-1])
print(spam[4])
print(spam[4]==spam[-1])

#4 切片 从哪个到哪个
print(spam[2:4])  #输出 [3,4]

#5 删除 
del spam[3]
print(spam)  #输出[1, 2, 3, 5]

#6 in / not in
print(10 in spam)
print(10 not in spam)

#7 enumerate 获取索引值和值
for index,item in enumerate(spam):
    print("Index:"+str(index)+ '--- Value:'+str(item))

#8 常用方法
spam.append(6)
spam.append(7)
spam.insert(1,10)  #第一个参数是插入位置，第二个参数是要插入的值
spam.insert(1,10)
spam.remove(10)  #删除列表中的值，只会删除第一个符合条件的。如果有多个相同的值也只会删第一个，如果要删的值不存在，会报异常
print(spam)

#9 元组：元组不可变，且用（）定义
spam =(1,10.1,"Hello",[10,11])
for i in spam:
    print(i)

try:
    spam[1]=10.2
except:
    print("不能修改元组值")

#10 id = 变量的内存地址
print(id(spam))
for i in spam:
    print(i) 
    print(id(i))
print(id(spam))