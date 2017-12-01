import csv

#Read a csv file and return the data in a list.
def readCsv(csvFilePath):
    with open(csvFilePath, 'r') as csvFile: 
        reader = csv.reader(csvFile)
        csvDataList = [row for row in reader]
    return csvDataList

#Write a csv data list to a file.
def writeCsv(csvDataList, csvFilePath):
    with open(csvFilePath, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        #Needs testing!
        if(debug):
            print(csvDataList)
        writer.writerows(csvDataList)      
    return