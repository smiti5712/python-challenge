import os
import csv

#Opening the output file in append mode
with open("PyPollOutput.txt", 'a') as f:
#Creating Path for Election_data file which is in the Resources folder 2 dirctories up from where the code is running
    Election_csv = os.path.join("..","..","Resources","election_data.csv")

#printing  Header for Display
    print("Election Results")
    f.write("Election Results \n")
    print("-----------------------------------------------")
    f.write("-----------------------------------------------\n")

#creating empty lists
    VoterID = []
    County = []
    Candidate = []
    Unique_candidate = []
      

#Opening file in read mode
    with open(Election_csv, "r", encoding='utf-8') as csvfile:
 
        csvreader = csv.reader(csvfile, delimiter=",")

    #Looping through the file to count number of Votes
        for row in csvreader:
            VoterID.append(row[0])
            County.append(row[1])
            Candidate.append(row[2])
        writeTotalVotes = "Total Votes: " + str(len(VoterID)-1)
        print(writeTotalVotes)
        f.write(writeTotalVotes + "\n")
        print("-----------------------------------------------")
        f.write("-----------------------------------------------\n")

    #Looping through Candidate check the distinct candidates, while appending to the Unique Candidate list
        for i in Candidate:
            if i not in Unique_candidate:
                Unique_candidate.append(i)
        Unique_candidate.pop(0)

    #setting a counter to store the previous Vote count (this is to check if the current vote count is greater than the previous vote count to find winner)
        prev_vote_count=0
    #Looping through Unique Candidate list and check the number of votes for that caldidate using the Candidate list
        for j in Unique_candidate:
            #calculating current Candidate's count and votes won percent
            curr_vote_count = Candidate.count(j)
            Votes_won_percent = round(curr_vote_count*100/(len(VoterID)-1),3)
            write_votes_won_percent = j + ": " + str(Votes_won_percent) + "00% (" + str(curr_vote_count) + ")"
            print (write_votes_won_percent)
            #writing output to file
            f.write(write_votes_won_percent + "\n")
            #finding the winner
            if curr_vote_count>prev_vote_count:
                winner=j
            prev_vote_count=curr_vote_count
        print("-----------------------------------------------")
        f.write("-----------------------------------------------\n")
        print("Winner: "+winner)
        #writing output to file  
        f.write("Winner: "+ winner + "\n")  
        print("-----------------------------------------------")
        f.write("-----------------------------------------------\n")