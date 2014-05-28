## Analyzing Phase Resolved Partial Data
## Plots the Maximum Amplitude of the PD, Numbers of PD, Average Amplitude of PD
##
## Author : Bharath Kumar Pareek
## Email  : bharathpareek@gmail.com

from pylab import * 					#Import the matplotlib library

fileName = sys.argv[1]								#Raw Data File Name
fullFile = [line.strip() for line in open(fileName)]
formattedFile = [float(x) for x in fullFile]
absFormattedFile = [abs(x) for x in formattedFile]				#Formatted File containing the Data
resultArray = absFormattedFile[0:10000]						#Array/List to store the final result to be plotted on graph (Figure 0). Each Cycle contains 10000 values.

for i in range(0,50):
	start = i*10000 
	end = start + 10000
	currentArray = absFormattedFile[start : end]
	
	for j in xrange(len(resultArray)):
		resultArray[j] = max(resultArray[j],currentArray[j])		#Determining the maximum amplitude
	
for m in range(len(resultArray)):
	if resultArray[m] < 0.3:
		resultArray[m] = 0						#Discard the values less than 0.3

xAxis = arange(0,10000,1)							#Set the X Axis 

figure(0)
plot(xAxis, resultArray)
title('Maximum Amplitude')
xlabel('Phase Angle (Degrees)')
ylabel('Max Value of PD')
xticks([0,2500,5000,7500,10000],[0,90,180,270,360])

resultArray2 = [0]*10000							#Array/List to store the final result to be plotted on graph (Figure 1)	
countArray = [0]*10000								#Count Array to store the numbers. Numbers explains how many cycles from the given 50 Cycles has PD at a given phase degree
count = 0

for i in range(0,50):
	start = i*10000 
	end = start + 10000
	currentArray1 = absFormattedFile[start : end]
	
	for j in range(len(resultArray)):
		if currentArray1[j] > 0.3 :
			resultArray2[j] = resultArray2[j] + currentArray1[j]
			countArray[j] = countArray[j] + 1


for j in range(len(resultArray2)):
	if countArray[j] !=0 :
		resultArray2[j] = resultArray2[j]/countArray[j]			#Determine the Average amplitude value

figure(1)
plot(xAxis, resultArray2)
title('Average Amplitude')
xlabel('Phase Angle (Degrees)')
ylabel('Average Value of PD')
xticks([0,2500,5000,7500,10000], [0,90,180,270,360])

figure(2)
print max(countArray)
plot(xAxis,countArray)
title('Numbers')
xlabel('Phase Angle (Degrees)')
ylabel('Number of PD')
xticks([0,2500,5000,7500,10000],[0,90,180,270,360])
show()
		
		

