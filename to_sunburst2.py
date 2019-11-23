import json
import pandas as pd
import csv

data = pd.read_csv('vehicles.csv',low_memory = False)#,encoding = 'latin-1')

number_of_vehicles = []

for i in range(100):
    number_of_vehicles.append(0)
header=["AccidentNumber","Category1","Category2"]

with open('vehicletypes.csv', 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(header)
	for index,row in data.iterrows():	
		vehicle = int(row["catv"])
		if(vehicle > 0 and vehicle < 14):
			newRow=[]
			newRow.append(row["Num_Acc"])
			if(vehicle == 3):
				newRow.append("Three-Wheeler")
			elif(vehicle > 3 and vehicle < 6):
				newRow.append("Two-Wheeler")
			elif(vehicle < 13):
				newRow.append("Four-Wheeler")
			else:
				newRow.append("Heavy Vehicle")
			
			if(vehicle == 1):
				newRow.append("Bicycle")
			if(vehicle == 2):
				newRow.append("Moped")
			if(vehicle == 3):
				newRow.append("Motor tricycle")
			if(vehicle == 4):
				newRow.append("scooter")
			if(vehicle == 5):
				newRow.append("Motorcycle")
			if(vehicle == 6):
				newRow.append("Side-Car")
			if(vehicle == 7):
				newRow.append("VL")
			if(vehicle == 8):
				newRow.append("VL + caravan")
			if(vehicle == 9):
				newRow.append("VL + trailer")
			if(vehicle == 10):
				newRow.append("VU")
			if(vehicle == 11):
				newRow.append("VL + caravan")
			if(vehicle == 12):
				newRow.append("VU + trailer")
			if(vehicle == 13):
				newRow.append("PL")
			writer.writerow(newRow)
csvFile.close()
