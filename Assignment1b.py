import csv
import glob, os #all imports needed for this program
path = os.getcwd() #gets the current path of the directory, this is used later on to find if the xml file is in the directory
os.chdir(path)
os.remove("Test.xml") #removes previous conversion xml file so the program will not give a false positive

def csvRead(): #function to read in a csv
	filename = raw_input('Enter the file you want to convert: ') #user-input file name
	cData = csv.reader(filename) #reads the file name csv to cData
	convert(cData) #calls the function convert to convert the csv to xml
def convert(Data): #function to convert a csv to xml
	xmlFile = 'Test.xml' #opens a empty xml file so that we can write in it
	xData = open(xmlFile, 'w')
	xData.write('<?xml version="1.0"?>' + "\n")
	xData.write('<csv_data>' + "\n")
	rowNum = 0;
	for row in Data: #a for loop that converts the csv to xml row by row
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
def output(): #a function that outputs if there is a xml file in the directory 
	for file in glob.glob("Test.xml"): #checks the directory for the xml file
    		print('The conversion worked') #prints out a statement if the xml file was found


if __name__ == "__main__":
	csvRead();
	output();
