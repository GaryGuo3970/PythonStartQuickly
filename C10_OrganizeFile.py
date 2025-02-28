import shutil
import os
import send2trash
import zipfile
from pathlib import Path

# 移动文件夹
def move_folder(source_folder,destination_folder):
    if not os.path.exists(source_folder):
        print(f"source {source_folder} is not exist")
    try:
        shutil.move(source_folder,destination_folder)
        print(f"source {source_folder} moved to {destination_folder}")
    except Exception as e:
        print(f"move excption: {e}")

#move_folder("From","To2")
#move_folder("To/1.txt","To2/test.txt")

# 删除文件
try:
    os.unlink("TO/1.txt")  #unlink = remove
except:
    print("")

# 清空 空文件夹：必须为空
try:
    os.rmdir("To")
except Exception as e:
    print(f"{e}")

# 删除到回收站
try:
    send2trash.send2trash("To/test.txt")
except Exception as e:
    print(f"{e}")

# 遍历目录树
for foldername, subfolders,filenames in os.walk("F:\Python\Study\StartQuickly\To"):
    # print(f'current folder {foldername}')
    print(f'current subfolder {subfolders}')
    # print(f'current filename {filename}')

    # for sub in subfolders:
    #     print(f'{sub}')    
    for subfolder in subfolders:
        print(f'{subfolder}')

    for f in filenames:
        print(f'{f}')

# 读取压缩文件
myzip = zipfile.ZipFile('F:\Python\Study\StartQuickly\TestZip.zip')
myzipFileList = myzip.filelist
for f in myzipFileList:
    #print(f)
    print(f.filename+ " "+str(f.file_size)+ " "+str(f.date_time))

# 解压文件
myzip.extractall('F:\Python\Study\StartQuickly\TestZipExact')