countyData={}

#单层级
countyData.setdefault('name','gary')
countyData.setdefault('age',18)
print(countyData)

#多层级
countyData.setdefault('chiled',{})
countyData['chiled'].setdefault('son','kyle')
countyData['chiled'].setdefault('daughter','mandy')
print(countyData)