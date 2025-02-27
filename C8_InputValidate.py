import pyinputplus as tinput
# response=tinput.inputNum("输入一个数字：")
# response=tinput.inputNum("输入一个数字：",min=100,max=150)
# response=tinput.inputNum("输入一个数字：",min=100,max=150,limit=5,timeout=10)
# 不允许输入cat字符串
response=tinput.inputStr("输入一个字符串：",allowRegexes=[r'cater','category'],blockRegexes=[r'cat','ca','c'])