#Modules - import os and csv
import os
import csv

#Set Path for file using relative path - make sure you have "/"instead of "\"
csvpath="PyPoll/Resources\election_data.csv"

# Total Votes = 0 -->Initialize a total vote counter 
total_votes = 0

# Candidate Options and candidate votes
candidate_list = []
candidate_votes = {} #Use Dictionary

# Find winning candidate (Start Tracker)
winning_candidate = ""
winning_count = 0



# Open the CSV using the UTF-8 encoding - Class Example
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip if there is no header) - Class Example
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


     # Print each row in the CSV file.
    for row in csvreader:
        # 2. Add to the total vote count.
        total_votes += 1

        #Print candidate name for each row
        candidate_name = row[2] #There are a total of 3 columns (start from 0-1-2) since candidate name is in column 3 then it is Row 2

        #if a candidate name is not matching any existing candiate add it to the list of candidates (use append)
        if candidate_name not in candidate_list:
            # Add it to the list of candidates.
            candidate_list.append(candidate_name)

            # Start tracking vote counter for each candidate - Candidate Names are keys and candidate votes are the values
            candidate_votes[candidate_name] = 0

        # Add a one (vote) to the candidate's vote counter
        candidate_votes[candidate_name] += 1

# Create a TEXT file to save the summarized results
with open("pypoll_outout.txt", "w") as txt_file:
    # Print vote count
    election_results = (
        f"\nElection Results\n"

        f"---------------------------------------\n"

        f"Total Votes: {total_votes:,}\n"

        f"---------------------------------------\n"
    )
    print(election_results, end="")
   
    # Add Final Vote Count
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Get vote count for each candidate and calculate the % = (candidates vote/total vote)*100
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100 #float to make it a decimal
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n" #Add Percentage Sign-https://stackoverflow.com/questions/28142688/how-to-turn-input-number-into-a-percentage-in-python
                                                                                    # Add Comma as thousand separator https://stackoverflow.com/questions/1823058/how-to-print-a-number-using-commas-as-thousands-separators
        # Print vote count for each candidate and their %
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Find winning candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate_name
         
    # Print winning candidate
    winning_candidate_summary = (
        f"-----------------------------------------\n"
        f"Winner: {winning_candidate}\n"

        f"-----------------------------------------\n"
    )
    print(winning_candidate_summary)
    # Save TEXT file
    txt_file.write(winning_candidate_summary)