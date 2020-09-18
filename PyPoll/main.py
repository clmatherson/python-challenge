# Import os module and read/write CSV files
import os
import csv

# Set path to open/write csv file 
csvpath = os.path.join('..','PyPoll','Resources','election_data.csv')
output_file = os.path.join('..','PyPoll','Analysis','election_results.csv')

# Create new lists for Voter ID and candidates
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)

    Vid = []
    Candi=[]
    for row in csvreader:
        Vid.append(str(row[0]))
        Candi.append(str(row[2]))

Tot_Votes = len(Vid)

# Make candidate list and 'set' to get a list of unique records
Candis=list(set(Candi))

# Make a list of the total number of votes each candidate received
Cand_Vote = []
count = 0
for nam in Candis:
    xvotes = Candi.count(str(Candis[count]))
    Cand_Vote.append(xvotes)
    count = count + 1

# Make a list with the percentage of the vote each candidate received
Cand_PerC = []
count = 0
for nam in Candis:
    xPerct = Candi.count(str(Candis[count])) / Tot_Votes * 100
    Cand_PerC.append(xPerct)
    count = count + 1

# Get the index for the candidate with the most votes
Most_V = max(Cand_Vote)
Winner_000 = Cand_Vote.index(Most_V)
Winner = Candis[Winner_000]

# Set variant and integer for data separator 
P_Break = "-"
PB_Repeat = 35

# Print Results to User Terminal
print('\n\nElection Results')
print(f'{str(P_Break)*PB_Repeat}')
print(f'Total Votes : {Tot_Votes}')
print(f'{str(P_Break)*PB_Repeat}')

count2 = 0
for nam in Candis:
    print(f'{Candis[count2]}: {Cand_PerC[count2]:.3f}%  ({Cand_Vote[count2]})')
    count2 = count2 + 1

print(f'{str(P_Break)*PB_Repeat}')
print(f'Winner: {Candis[Winner_000]}')
print(f'{str(P_Break)*PB_Repeat}\n\n')

# Print Results to "election_results.csv" File in the Analysis Folder
with open(output_file, 'w') as csvfile2:
    csvfile2.write('Election Results\n')
    csvfile2.write(f'{str(P_Break)*PB_Repeat}\n')
    csvfile2.write(f'Total Votes : {Tot_Votes}\n')
    csvfile2.write(f'{str(P_Break)*PB_Repeat}\n')

count3 = 0
for nam in Candis:
    with open(output_file, 'a') as csvfile2:
        csvfile2.write(f'{Candis[count3]}: {Cand_PerC[count3]:.3f}%  ({Cand_Vote[count3]})\n')
        count3 = count3 + 1

with open(output_file, 'a') as csvfile2:
    csvfile2.write(f'{str(P_Break)*PB_Repeat}\n')
    csvfile2.write(f'Winner: {Candis[Winner_000]}\n')
    csvfile2.write(f'{str(P_Break)*PB_Repeat}')