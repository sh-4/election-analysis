# Election-Analysis

## Project Overview
At the request of the Colorado Board of Elections, I have completed the following tasks to perform an audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of counties with voters.
3. Calculate the total number of votes each county contributed.
4. Calculate the percentage of votes in each county.
5. Determine the county with the largest voter turnout.
3. Get a complete list of candidates who received votes.
4. Calculate the total number of votes each candidate received.
5. Calculate the percentage of votes each candidate won.
6. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- SoftwareL Python 3.6.1, Visual Studio Code, 1.38.1

## Results
![election_results](https://user-images.githubusercontent.com/105808695/175662007-6b5ddb22-ebe1-485e-8b11-e9f664911dad.png)

As seen in the above image, the analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The counties that were audited were:
    - Jefferson
    - Denver
    - Arapahoe
- The county results were:
    - Jefferson County received 10.5% of the vote and 38,855 number of votes.
    - Denver County received 82.8% of the vote and 306,055 number of votes.
    - Arapahoe County received 6.7% of the vote and 24,801 number of votes.
- The county with the largest voter turnout was:
    - Denver County, which received 82.8% of the vote and 306,055 number of votes.
- The candidates in the election were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
  
## Election Audit Summary
### How this code can be used for future projects
This code could be used as a base for any future election. One example would be that it could be modified for educational purposes. If grade schools in each state were given surveys for proposed changes to the state’s curriculum, the candidate names could be swapped with the options up for a change. The counties could be swapped out for the varying school districts. This could allow the educational staff in each district to provide valuable input for changes that would directly affect them.

It could also be modified to find the results for the presidential election, as it could easily loop through every county within each state. In doing so, it could provide an analysis on which counties have the most influence in the swing states. All it would take, would be adding an additional column in the original data for the presidential candidate. From there, we could copy and paste the below loop model and change the variables within. Below is a step-by-step example of modifying this code to account for another column of data where we’re analyzing the results of our congressional election and presidential election at the same time.

Defining the lists and dictionary to hold the information we want:

![lists_and_dictionaries](https://user-images.githubusercontent.com/105808695/175695932-8d5ba739-5a1e-4cae-86b5-327662225bfd.png)

With presidential example:

![pres_list_and_dict](https://user-images.githubusercontent.com/105808695/175695989-9e14a519-dc49-491d-84a0-d3109eade86a.png)

Setting the variables to place into the loop model:

![results_variables](https://user-images.githubusercontent.com/105808695/175696162-4da8a28b-8265-4160-b90a-88bd167a3fb9.png)

With presidential example:

![pres_results_variables](https://user-images.githubusercontent.com/105808695/175696055-430b0d7b-b726-455f-8156-39daf9fab544.png)

Accessing the row data so the information can be pulled into a new loop:

![access_row_data](https://user-images.githubusercontent.com/105808695/175695859-423cbd7c-9006-4b7e-8d9f-b95783fc4811.png)

With presidential example:

![pres_access_row_data](https://user-images.githubusercontent.com/105808695/175695965-a2398161-92f9-463c-9528-62beb95e1a03.png)

Creating the loop to gather the data’s names and vote counts:

![collecting_names_and_votes](https://user-images.githubusercontent.com/105808695/175695884-472e7eca-c833-4f85-9764-2ed6dd777f97.png)

With presidential example:

![pres_names_and_votes](https://user-images.githubusercontent.com/105808695/175696025-fc3b49f1-fa0e-4812-8c89-46b823188bf6.png)

Creating the loop to calculate the winning data:

![winning_results_candidates](https://user-images.githubusercontent.com/105808695/175696221-9adb96e6-cd09-4886-9fe6-e81639a75576.png)

Substitute out the candidate info with presidential example:

![pres_winning_results_candidates](https://user-images.githubusercontent.com/105808695/175696074-0837e483-f322-47ad-b0a0-fe8a5578cb19.png)

These simple modifications are why this code could be a great base model for any poll results needed.

