import csv
import logging

logging.basicConfig(level=logging.DEBUG,format= '%(asctime)s %(levelname)s %(message)s')

csvFile = open('csv/example.csv')
csvReader = csv.reader(csvFile)
csvData = list(csvReader)
print(csvData)
logging.debug(f'{csvData[0]}')
logging.debug(f'{csvData[0][0]}')
logging.debug(f'{csvData[0][1]}')
logging.debug(f'{csvData[0][2]}')
logging.debug(f'{csvData[1][0]}')
logging.debug(f'{csvData[1][1]}')
logging.debug(f'{csvData[2][0]}')
print('----')
csvFile2 = open('csv/example.csv')
csvReader2 = csv.reader(csvFile2)
for row in csvReader2:
    print(f'{row}')
    for column in row:
        print(column)
 
