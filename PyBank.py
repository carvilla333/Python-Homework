import csv
import os

#we will load the file
Load_file = os.path.join("Python_HW_Data","budget_data.csv")
Write_to_file = os.path.join("Python_HW_Data","budget_analysis.txt")

#parameters
total_months = 0
net_total = 0
net_change = 0
store_changes = []
biggest_increment = ["", 0]
biggest_decrease = ["", 10000000]


#we are using this to read from the file and open it
with open(Load_file) as finance_data:
    reader = csv.reader(finance_data)
    skip_Header = next(reader)
    
    # We are skipping one more row in order to get the difference between two rows
    first_row = next(reader)

    # we add one more count to the total months that we took away when we skipped another row (otherwirse this would give us one less month)
    total_months += 1

    #this is a value ahead
    net_total += int(first_row[1])

    #this is the original value
    prev_net = int(first_row[1])

    



    for row in reader:



#this will calculate the months
        total_months += 1

        #this will calculate the net total
        net_total += int(row[1])


        #this will calculate the change average
        net = int(row[1]) - prev_net
        prev_net = int(row[1])
        store_changes += [net]

        #we calculate average change
        Average_change = sum(store_changes) / len(store_changes)

        #we calculate the greatest increase in profits
        if net > biggest_increment[1]:
            biggest_increment[0] = row[0]
            biggest_increment[1] = net

        #we calculate the lowest increase in profits
        if net < biggest_decrease[1]:
            biggest_decrease[0] = row[0]
            biggest_decrease[1] = net












# this is the dictionary we will use to print out the restults, and print out the contents to the text file
Final_list = {
    "Financial Analysis ": "",
    "----------------------------" : "",
    "Total Months: " : total_months , 
    "Total: $ " : net_total,  
    "Average  Change: $": Average_change, 
    "Greatest Increase in Profits:": biggest_increment, 
    "Greatest Decrease in Profits:": biggest_decrease
    }


# we use this to print our results
for pair in Final_list.items():
    print (pair)

# we use this to output our results into a txt file
with open(Write_to_file, "w") as txt_file:
    txt_file.write(str(Final_list))
