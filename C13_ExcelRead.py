import logging
import pprint
import openpyxl

logging.basicConfig(level=logging.DEBUG,format= '%(asctime)s %(levelname)s %(message)s')

logging.debug(f'读取excel')
wb=openpyxl.load_workbook('excel/人口数量.xlsx')

logging.debug(f'读取sheet')
sheet=wb['Sheet1']

countyData={}

logging.debug(f'读取单元格')
for row in range(2,sheet.max_row+1):
    province = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop2020 = sheet['D'+str(row)].value
    pop2021 = sheet['E'+str(row)].value

    countyData.setdefault(province,{})  #设置第一级
    countyData[province].setdefault(county,{'tracts':0,'pop':0})
    countyData[province][county]['tracts']+=1
    countyData[province][county]['pop']+=int(pop2020)    


    print(province+ ' '+county + ' '+ str(pop2020) + ' '+ str(pop2021))

print(countyData)

resultFile = open('excel/census2020.py','w',encoding='utf-8')
resultFile.write(pprint.pformat(countyData))
resultFile.close()

