import requests,os,bs4,logging

logging.basicConfig(level=logging.DEBUG,format= '%(asctime)s %(levelname)s %(message)s')

url = 'https://www.hippopx.com/zh'
os.makedirs('xkcd',exist_ok=True)           
logging.debug("创建目录xkcd")
#while not url.endswith('#'):
success=True
if success:
    success=False
    logging.debug("开始下载页面")
    # Download page
    response = requests.get(url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text,'html.parser')

    logging.debug("查找图片地址的URL")
    # Find the URL of the comi image
    imags=soup.find_all('img')
    logging.debug(f'共找到 {len(imags)} 张照片')

    logging.debug("下载图片到文件夹xkcd下")
    # Save the image to ./xkcd
    for i,img in enumerate(imags):
        img_url = img['src']
        logging.debug(f"正在下载 {img_url} ....")
        img_data = requests.get(img_url).content
        img_filename = os.path.join('xkcd',f'image_{i+1}.jpg')
        with open(img_filename,'wb') as img_file:
            img_file.write(img_data)        
        logging.debug(f"成功下载 {img_url}")    

    logging.debug("获取下一个按钮的URL")
    # Get the prev button's url


logging.debug("全部完成")
