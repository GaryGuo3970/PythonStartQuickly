spam="\"That is Demo's cat\" \nNext Line \n age is 3"
print(spam)
print(spam.isalnum()) #是否只包含数字
print(spam.isalpha())


#1
#2
#3
#rjust 往右移多少位置
spam = spam+"RIGHT".rjust(10)
print(spam)
#rjust 往左移多少位置
spam = spam+"LEFT".ljust(10)
print(spam)
print("Hello".center(20,"="))
