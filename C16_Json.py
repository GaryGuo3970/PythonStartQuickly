import json

#json文件读取转换成json对象
with open('json/demo.json','r',encoding='utf-8') as file:
    data = json.load(file)
    print(f' type :{type(data)} data:{data}')

#json字符串转换成json对象
jsonString = '{"安徽":{"亳州":{"pop":3000,"tracts":3},"合肥":{"pop":2000,"tracts":1},"安庆":{"pop":1100,"tracts":1}},"江苏":{"南京":{"pop":2300,"tracts":1},"苏州":{"pop":3000,"tracts":1}},"河北":{"唐山":{"pop":1600,"tracts":1},"廊坊":{"pop":1500,"tracts":1}}}'
jsonData = json.loads(jsonString)
print(f' type :{type(jsonData)} data:{jsonData}')

#json对象转换成字符串
jsonobj={'name':'gary','age':18,'handsome':True}
convertStr = json.dumps(jsonobj)
print(convertStr)