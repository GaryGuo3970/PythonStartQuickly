# webbrowser 是Python自带的，可以打开浏览器获取指定页面
# requests 因特网上下载文件和网页
# ba4 解析HTML
# selenium 启动并控制一个Web浏览器，能够填写表单，模拟鼠标在浏览器中单击


# 打开网页
import webbrowser,sys,pyperclip,logging
import requests

logging.basicConfig(level=logging.DEBUG,format= '%(asctime)s %(levelname)s %(message)s')

if len(sys.argv)>1:
    address= ' '.join(sys.argv)
else:
    address=pyperclip.paste()
    
logging.debug('123')
logging.debug(address)
logging.debug('456')

#webbrowser.open("https://www.baidu.com")

# request下载文件
resouce = requests.get("http://www.sjwx.la/files/article/image/84/84288/84288s.jpg")
#resouce2=requests.get("https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%9B%BE%E7%89%87%E4%B8%8B%E8%BD%BD&step_word=&hs=0&pn=4&spn=0&di=7466852183703552001&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=&st=-1&cs=2006583362%2C1420351640&os=2601955683%2C1354959760&simid=3519087961%2C331440929&adpicid=0&lpn=0&ln=937&fr=&fmq=1740747242279_R&fm=index&ic=0&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=https%3A%2F%2Fpic.rmb.bdstatic.com%2Fbjh%2F240518%2Ff7bf526f1a4946c72edbfba1336d9eef2572.jpeg%40h_1280&fromurl=ipprf_z2C%24qAzdH3FAzdH3F4k1_z%26e3Bkwt17_z%26e3Bv54AzdH3Fgjofrw2jAzdH3F1wpwAzdH3F1pswg1tg2otfj%3Fgt1%3D1p_90mll0llnnllallmnl0%26f576vjF654%3Di54jrw2j&gsm=1e&rpstart=0&rpnum=0&islist=&querylist=&nojc=undefined&lid=8048636046190921571")
#resouce3=requests.get("https://www.noexist1234.com/1.txt")
try:
    resouce.raise_for_status()
except Exception as e:
    print(f"{e}")
#resouce3.status_code == requests.codes.ok
playfile = open('wwwroot/2.jpg','wb')
for chunk in resouce.iter_content(100000):
    playfile.write(chunk)


    