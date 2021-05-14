#add dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Resources", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes=0

#Candidate options and candidate votes
candidate_options=[]
#declare the empty dictionary
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes +=1

        #Print the candidate name from each row.
        candidate_name=row[2]

        # if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

            #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1



       
#Print the candidate list
print(candidate_options)

#print the candidate vote dictionary
print(candidate_votes)

#Print the total votes
print(total_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes and format to 1 decimal palce
    vote_percentage = format((float(votes) / float(total_votes) * 100),'.1f')

    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")

# Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (float(votes) > float(winning_count)) and (float(vote_percentage) > float(winning_percentage)):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
   
# print the winning candidate, vote count and percentage to
print(f"The winning candidate is {winning_candidate} who received {winning_count} votes. This is {winning_percentage}% of all votes")

  