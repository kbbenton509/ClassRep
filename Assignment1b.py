import csv
import unittest
import glob, os
path = os.getcwd()
os.chdir(path)
os.remove("Test.xml")


#xmlFile = 'Test.xml'
#xData = open(xmlFile, 'w')
#xData.write('<?xml version="1.0"?>' + "\n")
#xData.write('<csv_data>' + "\n")

def csvRead():
	filename = raw_input('Enter the file you want to convert: ')
	cData = csv.reader(filename)
	convert(cData)
def convert(Data):
	xmlFile = 'Test.xml'
	xData = open(xmlFile, 'w')
	xData.write('<?xml version="1.0"?>' + "\n")
	xData.write('<csv_data>' + "\n")
	rowNum = 0;
	for row in Data:
		if rowNum == 0:
			tags = row
			for i in range(len(tags)):
				tags[i] = tags[i].replace(' ', '_')
                else:
                        xData.write('<row>' + "\n")
                        for i in range(len(tags)): 
                                xData.write('    ' + '<' + tags[i] + '>' + row[i] + '</' + tags[i] + '>' + "\n")
                        xData.write('</row>' + "\n") 
                rowNum +=1
	xData.write('</csv_data>' + "\n")
	xData.close()
def output():
	for file in glob.glob("*.xml"):
    		print('The conversion worked')

#xData.write('</csv_data>' + "\n")
#xData.close()

if __name__ == "__main__":
	csvRead();
	output();
