# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)
   
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1 
        
        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.    
with open(file_to_save,"w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
    f"\nElection Results\n"
    f"--------------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"--------------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

 
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes)*100

    # To do: pirnt out each candidate's name, vote count, and percentage of votes to the terminal.
    # print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's election results to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage ot the terminal.
        print (candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # Determine winning vote count and candidate
    # If the vote count > winning_count and % > winning_percentage, 
        if (votes > winning_count) and (vote_percentage > winning_percentage):

        # set the winning_count equal to the votes and 
        # set the winning_percentage equal to the vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
        # Set the winning_count = candidate
            winning_candidate = candidate
    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


       


