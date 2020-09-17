# Import os module and read/write CSV files
import os
import csv

csvpath = os.path.join('..','PyPoll','Resources','election_data.csv')
output_file = os.path.join('..','PyPoll','Analysis','election_results.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    headers = next(csvreader)

    Vid = []
    Candi=[]
    for row in csvreader:
        Vid.append(str(row[0]))
        Candi.append(str(row[2]))

Candis=list(set(Candi))

Cand_00 = Candis[0]
Cand_01 = Candis[1]
Cand_02 = Candis[2]
Cand_03 = Candis[3]

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

Tot_Votes = len(Vid)

Tot_VCand_00 = Cand_Ct_00
Tot_VCand_01 = Cand_Ct_01
Tot_VCand_02 = Cand_Ct_02
Tot_VCand_03 = Cand_Ct_03

Per_VCand_00 = Tot_VCand_00 / Tot_Votes * 100
Per_VCand_01 = Tot_VCand_01 / Tot_Votes * 100
Per_VCand_02 = Tot_VCand_02 / Tot_Votes * 100
Per_VCand_03 = Tot_VCand_03 / Tot_Votes * 100

Tot_VList = [Tot_VCand_00,Tot_VCand_01,Tot_VCand_02,Tot_VCand_03]

Most_V = max(Tot_VList)
Winner_000 = Tot_VList.index(Most_V)

P_Break = "-"
PB_Repeat = 35

print('')
print('Election Results')
print(str(P_Break)*PB_Repeat)
print(f'Total Votes : {Tot_Votes}')
print(str(P_Break)*PB_Repeat)
print(f'{Cand_00}: {Per_VCand_00:.3f}%  ({Tot_VCand_00})')
print(f'{Cand_01}: {Per_VCand_01:.3f}%  ({Tot_VCand_01})')
print(f'{Cand_02}: {Per_VCand_02:.3f}%  ({Tot_VCand_02})')
print(f'{Cand_03}: {Per_VCand_03:.3f}%  ({Tot_VCand_03})')
print(str(P_Break)*PB_Repeat)
print(f'Winner: {Candis[Winner_000]}')
print(str(P_Break)*PB_Repeat)
print('')

# Print Resutls to "election_results.csv" File in the Analysis Folder
with open(output_file, 'w') as csvfile2:
    csvwriter = csv.writer(csvfile2, delimiter=',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['--------------------------'])
    csvwriter.writerow([f'Total Votes : {Tot_Votes}'])
    csvwriter.writerow(['--------------------------'])
    csvwriter.writerow([f'{Cand_00}: {Per_VCand_00:.3f}%  ({Tot_VCand_00})'])
    csvwriter.writerow([f'{Cand_01}: {Per_VCand_01:.3f}%  ({Tot_VCand_01})'])
    csvwriter.writerow([f'{Cand_02}: {Per_VCand_02:.3f}%  ({Tot_VCand_02})'])
    csvwriter.writerow([f'{Cand_03}: {Per_VCand_03:.3f}%  ({Tot_VCand_03})'])
    csvwriter.writerow(['--------------------------'])
    csvwriter.writerow([f'Winner: {Candis[Winner_000]}'])
    csvwriter.writerow(['--------------------------'])