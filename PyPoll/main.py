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

# Make candidate list a 'set' to get a list with only unique records
Candis=list(set(Candi))

# Assign each candidate to a variant
Cand_00 = Candis[0]
Cand_01 = Candis[1]
Cand_02 = Candis[2]
Cand_03 = Candis[3]

# Count how many votes each received and assign totals to variants
Cand_Ct_00 = 0
Cand_Ct_01 = 0
Cand_Ct_02 = 0
Cand_Ct_03 = 0

for nam in Candi:
    if nam == Cand_00:
        Cand_Ct_00 = Cand_Ct_00 + 1
    if nam == Cand_01:
        Cand_Ct_01 = Cand_Ct_01 + 1
    if nam == Cand_02:
        Cand_Ct_02 = Cand_Ct_02 + 1
    if nam == Cand_03:
        Cand_Ct_03 = Cand_Ct_03 + 1

# Calculate what Percentage of the vote each candidate received
Tot_Votes = len(Vid)
Per_VCand_00 = Cand_Ct_00 / Tot_Votes * 100
Per_VCand_01 = Cand_Ct_01 / Tot_Votes * 100
Per_VCand_02 = Cand_Ct_02 / Tot_Votes * 100
Per_VCand_03 = Cand_Ct_03 / Tot_Votes * 100

# Create a list with the total votes each candidate received
Tot_VList = [Cand_Ct_00,Cand_Ct_01,Cand_Ct_02,Cand_Ct_03]

# Get the index for the candidate with the most votes
Most_V = max(Tot_VList)
Winner_000 = Tot_VList.index(Most_V)

# Set variant and integer for data separator 
P_Break = "-"
PB_Repeat = 35

# Print Results to User Terminal
print('\n\nElection Results')
print(f'{str(P_Break)*PB_Repeat}')
print(f'Total Votes : {Tot_Votes}')
print(f'{str(P_Break)*PB_Repeat}')
print(f'{Cand_00}: {Per_VCand_00:.3f}%  ({Cand_Ct_00})')
print(f'{Cand_01}: {Per_VCand_01:.3f}%  ({Cand_Ct_01})')
print(f'{Cand_02}: {Per_VCand_02:.3f}%  ({Cand_Ct_02})')
print(f'{Cand_03}: {Per_VCand_03:.3f}%  ({Cand_Ct_03})')
print(f'{str(P_Break)*PB_Repeat}')
print(f'Winner: {Candis[Winner_000]}')
print(f'{str(P_Break)*PB_Repeat}\n\n')

# Print Resutls to "election_results.csv" File in the Analysis Folder
with open(output_file, 'w') as csvfile2:
    csvfile2.write('Election Results\n')
    csvfile2.write(f'{str(P_Break)*PB_Repeat}\n')
    csvfile2.write(f'Total Votes : {Tot_Votes}\n')
    csvfile2.write(f'{str(P_Break)*PB_Repeat}\n')
    csvfile2.write(f'{Cand_00}: {Per_VCand_00:.3f}%  ({Cand_Ct_00})\n')
    csvfile2.write(f'{Cand_01}: {Per_VCand_01:.3f}%  ({Cand_Ct_01})\n')
    csvfile2.write(f'{Cand_02}: {Per_VCand_02:.3f}%  ({Cand_Ct_02})\n')
    csvfile2.write(f'{Cand_03}: {Per_VCand_03:.3f}%  ({Cand_Ct_03})\n')
    csvfile2.write(f'{str(P_Break)*PB_Repeat}\n')
    csvfile2.write(f'Winner: {Candis[Winner_000]}\n')
    csvfile2.write(f'{str(P_Break)*PB_Repeat}')