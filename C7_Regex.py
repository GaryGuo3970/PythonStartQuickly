import re

# 手机号码
def is_valid_mobile_phone(phone):
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, phone))

phone_numbers = ['13800138000', '12345678901', 'abcdefghijk','15821189999','1582118999']
for phone in phone_numbers:
    if is_valid_mobile_phone(phone):
        print(f"{phone} 是有效的手机号码。")
    else:
        print(f"{phone} 不是有效的手机号码。")

        import re

# E-mail
def is_valid_email_simple(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

test_emails = [
    "example@example.com",
    "user.name+tag+sorting@example.com",
    "invalid_email",
    "example@.com"
]

for email in test_emails:
    if is_valid_email_simple(email):
        print(f"{email} 是有效的邮箱地址。")
    else:
        print(f"{email} 不是有效的邮箱地址。")

        import re

def is_text_present(text, pattern):
    # 使用 re.search 函数搜索匹配项
    result = re.search(pattern, text)
    # 如果 result 不为 None，则表示找到了匹配项
    return result is not None

# 测试文本
main_text = "Hello, world! This is a test."
search_pattern = r"is a"

if is_text_present(main_text, search_pattern):
    print(f"模式 '{search_pattern}' 存在于文本中。")
else:
    print(f"模式 '{search_pattern}' 不存在于文本中。")


# 提取文本
def extractText(text):
    phonePattern=r'1[3-9]\d{9}'
    emailPattern=r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    phoneNumbers=re.findall(phonePattern,text)
    emails=re.findall(emailPattern,text)

    return phone_numbers,emails
    
text = """
这是一段包含电话号码和电子邮件的文本。
电话号码：13800138000，13912345678
电子邮件：example@example.com，user.name+tag@example.co.uk
"""

print()
print("-----提取文本------")
phones,emials=extractText(text)
for p in phones:
    print(p)

for e in emials:
    print(e)
