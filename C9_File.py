from pathlib import Path
import os
path='F:\Python\Study\StartQuickly\Chapter9'
try:
    os.makedirs(path)
except:
    print('已存在')
p=Path(path)
print(p.anchor)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)

#读写文件
newFile='F:\\Python\\Study\\Temp.txt'
f=Path(newFile)
f.write_text("Hello World!")
f.read_text()