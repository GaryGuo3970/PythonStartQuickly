import pprint

myInfo={"Name":"Gary","Age":10,"Address":"Shanghai","Salary":12345.6}
print(myInfo["Age"])
print(myInfo["Address"])

#keys
for k in myInfo.keys():
    print(k+":"+str(myInfo[k]))

#local update1
#local update1
#update1 by otheruser
#update2 by otheruser
#Values
for v in myInfo.values():
    print(str(v))

#items
for k,v in myInfo.items():
    print(str(k)+"-"+str(v))

#get 获取字典的值，如果不存在，就返回一个默认值
print(myInfo.get("Age",0))  
print(myInfo.get("Age2",0))

#嵌套
spam={"item1":{"Name":"Gary","Age":10,"Address":"Shanghai","Salary":12345.6},"item2":{"Name":"Peter","Age":22,"Address":"Bejing","Salary":65432}}
for k,v in spam.items():
    print("------------")
    print("|"+str(k)+"|")
    print("------------")
    for subk,subv in v.items():
        print(str(subk)+"|"+str(subv))
