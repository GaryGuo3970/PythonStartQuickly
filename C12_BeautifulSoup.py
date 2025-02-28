import requests,bs4

response  = requests.get("https://www.baidu.com")
response.raise_for_status()
noStarchSoup=bs4.BeautifulSoup(response.text,'html.parser')
type(noStarchSoup)
with open('wwwroot/exampleFile.html') as exampleFile:
    exampleSoup=bs4.BeautifulSoup(exampleFile,'html.parser')
    type(exampleSoup)
    divlist= exampleSoup.select('div')
    for d in divlist:
        print(d)