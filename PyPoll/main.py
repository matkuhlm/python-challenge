import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

#set empty variables for loopp
total_votes = 0
candidates = []
votecount = 0
county = []
winning_vote_count = 0


    #set reader and then loop through data 
with open(csvpath, 'r', newline='') as csvfile:
    csv.reader=csv.reader(csvfile,delimiter=',')
    csv_header= next(csvreader)

    for row in csvreader:
        total_votes +=1

        if(row[2] not in candidates) :
            candidates.append(row[2])
            votecount.append(0)

        #index the candidate list
        cindex = candidates.index(row[2])
        votecount[cindex]+=1
    
    print(f'Election Results')
    print(f'-------------------------------------------')
    print(f'Total Votes: {total_votes}')
    print(f'-------------------------------------------')

    for i in range(len(candidates)):
            pvote = round((votecount[i]/total_votes)*100,3)
            print(f'{candidates[i]}: {pvote}% ({votecount[i]})')
        
         if(winning_vote_count < votecount[i]):
            winning_vote_count = votecount[i]
            winner = candidates[i]

    print('-------------------------------------------')
    print(f'WINNER: {winner} !')
    print('-------------------------------------------')