# Import os module and read/write CSV files
import os
import csv

csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')
output_file = os.path.join('..','PyBank','Analysis','budget_analysis.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)

    Date = []
    Data = []
    for row in csvreader:
        # Data.append(row[0])
        Date.append(str(row[0]))
        Data.append(int(row[1]))

Diff_List=[]
count=0
for num in Data:
    if count == 0:
        pass
    else:
        Diffs = num - Data[count - 1]
        Diff_List.append(Diffs)
    count = count + 1

def average(numbers):
    length = len(Diff_List)
    total = 0.0
    for number in numbers:
        total +=number
    return total / length

def sum(numbers):
    total = 0
    for num in numbers:
        total += num    
    return total

lnegth_Mths = len(Date)

Net_Amt = sum(Data)

Total_Diff = sum(Diff_List)

GIPmax = max(Diff_List)
GIPmaxID = Diff_List.index(GIPmax) + 1

GIPmin = min(Diff_List)
GIPminID = Diff_List.index(GIPmin) + 1

FAna = ('Financial Analysis')

P_Break = "-"
PB_Repeat = 50

R1_Line = (f"Total Months: {lnegth_Mths}")
R2_Line = (f"Total: ${Net_Amt}")
R3_Line = (f"Average Change: ${average(Diff_List):.2f}")
R4_Line = (f"Greatest Increase in Profits: {Date[GIPmaxID]} (${GIPmax})")
R5_Line = (f"Greatest Decrease in Profits: {Date[GIPminID]} (${GIPmin})")

Rpt_Summary = [R1_Line,R2_Line,R3_Line,R4_Line,R5_Line]

# Print Resutls to "Budget_Analysis" File in the Analysis Folder
with open(output_file, 'w') as csvfile2:
    csvwriter = csv.writer(csvfile2, delimiter='\n')
    csvwriter.writerow([FAna])
    csvwriter.writerow(Rpt_Summary)

# Print Results Summary to Terminal
print("")
print(str(FAna))
print(str(P_Break)*PB_Repeat)
for row in Rpt_Summary:
    print(row)
print(str(P_Break)*PB_Repeat)
print("")