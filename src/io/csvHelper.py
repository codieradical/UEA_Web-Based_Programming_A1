import csv

def readCsv(csvFilePath):
#read a file and return a list
    with open(csvFilePath, 'r') as csvFile: 
        reader = csv.reader(csvFile)
        csvDataList = [row for row in reader]
    return csvDataList

def writeCsv(csvDataList, csvFilePath):
#write a list to file
    with open(csvFilePath, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        if(debug):
            print(csvDataList)
        writer.writerows(csvDataList)      
    return