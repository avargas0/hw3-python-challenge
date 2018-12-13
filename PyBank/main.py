import os
import csv

#Load file and create output file
financial_csv = os.path.join("Resources","budget_data.csv")
financial_output = os.path.join("output","budget_output.txt")

#print(financial_csv)

#Set parameters
totalMonths = 0
monthsChange = []
totalNet = 0
netChange = 0
total_netChange = 0
greatestInc = [1 , 0]
greatestDec = ["", 99999999999999999999999]
count = 0 

#print(os.getcwd())

#Open CSV file and convert into list of dictionaries
with open(financial_csv,"r",newline="") as csvfile: 
    reader = csv.reader(csvfile, delimiter=",")

    #Read the header row first
    header = next(reader)
    #print(header)
    #print(header[0])
    #print(header[1])

    #Remove first row
    first_row = next(reader)
    #print(first_row)
    #print(first_row[0])
    #print(first_row[1])

    #Calculate outputs
    totalMonths = totalMonths + 1
    totalNet = totalNet + int(first_row[1])
    previous = int(first_row[1])
    #print("totalNet " + str(totalNet))

    for row in reader: 
        #print(row)
        #print(len(row))
        totalMonths = totalMonths + 1
        totalNet = totalNet + int(row[1])
        #print("totalNet " + str(totalNet))

        count = count + 1
        #print("count " + str(count))

        netChange = int(row[1]) - previous
        previous = int(row[1])
        total_netChange = total_netChange + netChange 
        monthsChange = monthsChange + [row[0]] 
        #print("net change " + str(netChange))
        #print("total net change " + str(total_netChange))


        #print("before " + str(greatestInc[1]))
        if netChange >= greatestInc[1]:
            greatestInc[0] = row[0]
            greatestInc[1] = netChange
        #print("greatest increase " + str(greatestInc))

        #print("before " + str(greatestDec[1]))
        if netChange < greatestDec[1]:
            greatestDec[0] = row[0]
            greatestDec[1] = netChange 
        #print("greatest decrease " + str(greatestDec))
        #print("----------------------------")
    
#Caluclate average net change
net_monthly_avg = total_netChange / count
#print("net monthly average " + str(net_monthly_avg))

print("Total Months " + str(totalMonths))
print("Net Total " + str(totalNet))
print("Net Monthly Average " + str(net_monthly_avg))
print("Greatest Increase " + greatestInc[0] + " " + str(greatestInc[1]))
print("Greatest Decrease " + greatestDec[0] + " " + str(greatestDec[1]))

with open(financial_output,'w') as txtfile:
    print("Financial Output",file=txtfile,end='\n')
    print("Total Months " + str(totalMonths),file=txtfile,end='\n')
    print("Net Total " + str(totalNet),file=txtfile,end='\n')
    print("Net Monthly Average " + str(net_monthly_avg),file=txtfile,end='\n')
    print("Greatest Increase " + greatestInc[0] + " " + str(greatestInc[1]),file=txtfile,end='\n')
    print("Greatest Decrease " + greatestDec[0] + " " + str(greatestDec[1]),file=txtfile,end='\n')
