# Import os module and read/write CSV files
import os
import csv

# Set path to open/write csv file 
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')
output_file = os.path.join('..','PyBank','Analysis','budget_analysis.csv')

# Create new lists for Dates and Amounts
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)

    Date = []
    Amts = []
    for row in csvreader:
        Date.append(str(row[0]))
        Amts.append(int(row[1]))

# Calculat the 'change in periods' and assign amounts to new list
Diff_List=[]
count=0
for num in Amts:
    if count == 0:
        pass
    else:
        Diffs = num - Amts[count - 1]
        Diff_List.append(Diffs)
    count = count + 1

# Calculate the average
average1 = sum(Diff_List)/len(Diff_List)

# Count the number of periods
lnegth_Mths = len(Date)

# Calculate period total
Net_Amt = sum(Amts)

# Calculate 'change in periods' total
Total_Diff = sum(Diff_List)

# Get the Min and Max and their corresponding index numbers from the 'change in periods'
GIPmax = max(Diff_List)
GIPmaxID = Diff_List.index(GIPmax) + 1

GIPmin = min(Diff_List)
GIPminID = Diff_List.index(GIPmin) + 1

# Create a variant for the report header
FAna = ('Financial Analysis')

# Set variant and integer for data separator 
P_Break = "-"
PB_Repeat = 50

# Set variants for each results line
R1_Line = (f"Total Months: {lnegth_Mths}")
R2_Line = (f"Total: ${Net_Amt}")
R3_Line = (f"Average Change: ${average1:.2f}")
R4_Line = (f"Greatest Increase in Profits: {Date[GIPmaxID]} (${GIPmax})")
R5_Line = (f"Greatest Decrease in Profits: {Date[GIPminID]} (${GIPmin})")

# Assign results to a list
Rpt_Summary = [R1_Line,R2_Line,R3_Line,R4_Line,R5_Line]

# Print Resutls to "Budget_Analysis" File in the Analysis Folder
with open(output_file, 'w') as csvfile2:
    csvwriter = csv.writer(csvfile2, delimiter='\n')
    csvfile2.write(f'{FAna}\n\n')
    csvfile2.write(f'{str(P_Break)*PB_Repeat}\n\n')
    csvwriter.writerow(Rpt_Summary)
    csvfile2.write(f'{str(P_Break)*PB_Repeat}')

# Print Results Summary to Terminal
print(f'\n\n{str(FAna)}\n')
print(str(P_Break)*PB_Repeat)
for row in Rpt_Summary:
    print(row)
print(f'{str(P_Break)*PB_Repeat}\n\n')