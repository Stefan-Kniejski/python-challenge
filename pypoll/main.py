import csv
import os

# Path to collect data from the Resources folder
election_data = os.path.join('.','Resources', 'election_data.csv')

# Read in the CSV file
with open(election_data, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Creates lists for both candidates and candidate list
    # Also creates a dictionary for votes to be added to
    Candidate = []
    candidateList = []
    totalVoters = 0
    votes = {}

    # Loop through the data
    for row in csvreader:
        Candidate = row[2]
        if Candidate not in candidateList:
            candidateList.append(Candidate)
            votes[Candidate] = 0
        votes[Candidate] += 1
        totalVoters += 1

    # Print the Results
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str('{:,.0f}'.format(totalVoters)))
    print("-------------------------")
    for i in votes:
        PctVotes = '{:,.3f}'.format((votes[i]/totalVoters)*100)
        print(i + ": " + str(PctVotes) +
              "% (" + str('{:,.0f}'.format(votes[i])) + ")")
    print("-------------------------")
    keyMax = max(votes, key=votes.get)
    print("Winner:  " + keyMax)
    print("-------------------------")
  