import os
import csv 

#Set the variable
vote_count = 0
candidate_dd = []
candidate_votes = {}
most_votes = 0
winner = ""

#import csv file
election = os.path.join("Resources","election_data.csv")
#export txt file
output = os.path.join("analysis","output.txt")

#Open csv file
with open(election) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')

    #Start with header
    next(csv_reader)
    
    #This is going to loop through the file
    for row in csv_reader:

        #to find the total vote count
        vote_count = vote_count + 1   
        #to idendify the candidate name column
        candidate_name = row[2]
        
        #if statment to grab unique candidate and add to dictonary 
        if candidate_name not in candidate_dd:
            candidate_dd.append(candidate_name)

            #Set candidates vodes with name to count indiviual votes
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

#To print header and votes
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(vote_count))
print("----------------------------")

# To open the file and write the header and votes
with open(output, 'w') as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write("Total Votes: {}\n".format(vote_count))
    file.write("----------------------------\n")

    #set loop to loop throught each candidates votes
    for candidate in candidate_votes:
                
        #Get the vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(vote_count) * 100
        
        #print candidate information to terminal
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})") 
        
        #write candidate information to the file
        file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")       
        
        #find the candidate with the most votes to find winner
        if (votes > most_votes):
            most_votes = votes
            winner = candidate  
    
    #print winner to terminal
    print("----------------------------")
    print("Winner: " + str(winner))

    #write the winner to the file
    file.write("----------------------------\n")
    file.write("Winner: " + str(winner))