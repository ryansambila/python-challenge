import os
import csv 

#Set Variables
line_count = 0
month_count = 0
total = 0
max_change = ["",0]
min_change = ["",0]
previous = 0
pnl = []

#Import budget file
budget = os.path.join("Resources","budget_data.csv")
#export txt file
output = os.path.join("analysis","output.txt")

#Open budget file
with open(budget) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    
    #This is to loop through the file
    for row in csv_reader:

        #First line is the names of the columns so we start
        if line_count >= 1:    
        
            #Add each month to total months
            month_count += 1

            #Add each months total to get total dollars
            total += int(row[1])

            #Start the if statemetn to get change, max, & min
            if line_count > 1:

                #Find the change per period and set to a list
                change = int(row[1]) - previous
                pnl.append(change)

                #find the max increase in profit per preiod
                if change > max_change[1]:
                    max_change = [row[0], change]
                
                if change < min_change[1]:
                    min_change = [row[0], change]

            #Set the previous change from the priod before
            previous = int(row[1])
            
        #Move to the next line in the loop
        line_count = line_count+1     

#Cacluate the aveage profit loss per period
average = sum(pnl)/len(pnl)

#print the analysis to the termainal
print("Financial Analysis")
print("----------------------------")
print("Total Months: "+ str(month_count))
print("Total: " +str(total))
print("Average Change: $" + "{:.2f}".format(average))
print("Greatest Increase in Profits: "+ max_change[0] + " ($" + str(max_change[1]) + ")")
print("Greatest Decrease in Profits: "+ min_change[0] + " ($" + str(min_change[1]) + ")")

with open(output, 'w') as file:
    # Write the analysis to a text file
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months: {}\n".format(month_count))
    file.write("Total: ${}\n".format(total))
    file.write("Average Change: ${:.2f}\n".format(average))
    file.write("Greatest Increase in Profits: {} (${:.2f})\n".format(max_change[0], max_change[1]))
    file.write("Greatest Decrease in Profits: {} (${:.2f})\n".format(min_change[0], min_change[1]))

