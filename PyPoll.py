import csv
import os

# We will load the file
Load_file = os.path.join("Python_HW_Data","election_data.csv")
Write_to_file = os.path.join("Python_HW_Data","election_analysis.txt")

#Parameters

# Used to count the total votes
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# We are using this to read from the file and open it
with open(Load_file) as finance_data:
    reader = csv.reader(finance_data)
    
    # We use this to skip the header
    skip_Header = next(reader)
    
    for row in reader:
        
        # This will count the total votes
        total_votes += 1
        
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
            
        # This will count the total votes for each candidate    
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
            
        # We use this to print results to the console, and to the text file
        Final_list = {
            "Election Results ": "",
            "----------------------------" : "",
            "Total Votes: " : total_votes , 
            candidate : vote_percentage,
            "candidate votes: " : votes,
            "Winner: ": winning_candidate
            }
        
        # we use this to print our results
        for pair in Final_list.items():
            print (pair)
        with open(Write_to_file, "w") as txt_file:
            txt_file.write(str(Final_list))
            