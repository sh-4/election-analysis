# add our dependencies
import csv
# ^ allows us to read csv
import os
from xml.dom.expatbuilder import FilterVisibilityController
# ^ connects to the os so files are available for use

# assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# (1a) initialize a total vote counter before opening the file
total_votes = 0
# (2a) declare a new, empty list for candidate names before opening the file
candidate_options = []
# (3a) declare an empty dictionary before the loop
candidate_votes = {}
# (4a) declare a variable that holds an empty string value for the winning candidate,
winning_candidate = ""
# (4a) declare a variable for the "winning count" equal to 0
winning_count = 0
# (4a) declare a variable for the "winning percentage" equal to 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
    # to do: read and analyze the data here
    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)

    # print each row in the csv file
    for row in file_reader:
        # (1b) add to the total vote count
        total_votes += 1
        # ^ shorter version of total_votes = total_votes + 1

        # (2b) print the candidate name from each row
        candidate_name = row[2]
        # (2c) add the candidate name to the candidate list
        ## candidate_options.append(candidate_name)
        # replacing 2c with 2d for efficiency and avoiding repetition
        
        # (2d) add if statement to avoid repeating candidate names
        # must be nested in the for loop iterating through each row
        # if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        # add it to the list of candidates
            candidate_options.append(candidate_name)
            # (3b) begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # (3c) add a vote to that candidate's count
        # un-indent to take out of the if statement
        # allows it to loop through all of the rows, adding 1 with each
        candidate_votes[candidate_name] += 1

# save the results to the text file
with open(file_to_save, "w") as txt_file:

    # print the final vote count to the terminal
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # save the final vote count to the text file
    txt_file.write(election_results)

    # determine the percentage of votes for each candidate by looping through the counts
    # 1. iterate through the candidate list
    for candidate_name in candidate_votes:
        # 2. retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
            
        # print out each candidate's name, vote count, and percentage of votes to the terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 
        print(candidate_results)
        # save the candidate reults to text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # inside the candidate_options for loop (the outer loop)
        # but also after determining votes/vote percentage
        # 1. determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. if true, then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    # print out the winning candidate, vote count, and percentage to terminal
    # in line with original for loop
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

















