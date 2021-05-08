# Adding dependencies
import os
import csv

# assign a variable to load input file from a path
file_to_load = os.path.join("Resources","election_results.csv")
# assign a variable to save output file to a given path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0

#list to store individual candidate votes
candidate_options =[]
# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the input text file to read it
with open(file_to_load, "r") as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes+= 1
        # Get the candidate name from each row.
        candidate_name = row[2]
         # get unique candidate names
        if candidate_name not in candidate_options:
           candidate_options.append(candidate_name)
           # 2. Begin tracking that candidate's vote count.
           candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    # save results to the output text file
with open(file_to_save, "w") as txt_file:
    election_results = (f"Election Result\n----------------------\n"
    f"Total Votes: {total_votes} \n"
    f"----------------------\n")
    print(election_results)
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = round((float(votes)/float(total_votes))*100,1)
        candidate_results = (f"{candidate_name}:{vote_percentage}% ({votes}).\n")
        if votes > winning_count and vote_percentage > winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
        txt_file.write(candidate_results)
        print(candidate_results)
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)

'''print(f'total number of votes: {total_votes}\n')
print (f'candidate names: {candidate_options}\n')
print(f'votes per candidate: {candidate_votes}\n')
    
with open(file_to_save,"w") as election_analysis :
    election_analysis.write("Counties in the Election \n---------------------------------\n Arapahoe\nDenver\nJefferson")
'''

# open & close the file
# election_data = open(Path,"r")
#election_data.close()

# take sum of all ballots to get to the total number of votes
# group by each candidate and then get the sum of votes received for each candidate
# calculate percentage of votes received per candidate
# idnetify the candidate receiving highest number of votes