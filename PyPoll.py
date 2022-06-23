# Import the datetime class from the datetime module
## import datetime as dt
# ^ added "as dt" so datetime can be abbreviated
# Use the now() attribute on the datetime class to get the present time
# now = datetime.datetime.now()
## now = dt.datetime.now()
# Print the present time
## print("The time right now is ", now)

# import election results csv file via direct path:
# assign a variable for the file to load and the path
### file_to_load = 'Resources/election_results.csv'
# open the election results and read the file
## election_data = open(file_to_load, "r")
# to do: perform analysis
# close the file
## election_data.close()

# import election results csv file without open() and close()
# use 'with' statement instead to avoid losing/corrupting data
# with open(filename) as file_variable
### with open(file_to_load) as election_data:
    # to do: perform analysis
    ### print(election_data)

# import election results csv file via indirect path
### import csv
### import os
# assign a variable for the file to load and the path
## file_to_load = os.path.join("Resources", "election_results.csv")
# open the election results and read the file
## with open(file_to_load) as election_data:
    #print the file object
    ## print(election_data)

# create a filename variable to a direct or indirect path to the file
### file_to_save = os.path.join("analysis", "election_analysis.txt")
# using the open() function with the "w" mode, we will write data to the file
## open(file_to_save, "w")
# use the open statement to open the file as a text file
### outfile = open(file_to_save, "w")
# write some data to the file
### outfile.write("Hello World")
#close the file
### outfile.close()

# ^ creating a cleaner version of the above code
# create a filename variable to a direct or indirect path to the file
### file_to_save = os.path.join("analysis", "election_analysis.txt")
# using the with statement, open the file as a text file
### with open(file_to_save, "w") as txt_file:
    # write some data to the file
    #txt_file.write("Hello World")

    # write the 3 counties to the file
    ## txt_file.write("Arapahoe, ")
    ## txt_file.write("Denver, ")
    ## txt_file.write("Jefferson")
    # cleaner version:
    ## txt_file.write("Arapahoe, Denver, Jefferson")
    # cleaner version, with each on a separate line using "\n":
    ## txt_file.write("Arapahoe\nDenver\nJefferson")
    # modified to include header
    ### txt_file.write("Counties in the Election")
    ### txt_file.write("\n------------------------")
    ### txt_file.write("\nArapahoe\nDenver\nJefferson")

# add our dependencies
import csv #allows us to read csv
import os #connects to the os so files are available for use
# assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file
with open(file_to_load) as election_data:
    # to do: read and analyze the data here
    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # print the header row
    headers = next(file_reader)
    print(headers)
    
    # print each row in the csv file
    ## for row in file_reader:
        ## print(row)


# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

















