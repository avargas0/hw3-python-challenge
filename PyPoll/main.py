import os
import csv

election_csv = os.path.join("Resources","election_data.csv")
election_output = os.path.join("output","election_analysis.txt")

print(election_csv)
print("**********************")

#Open csv
with open(election_csv, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    voter_info = []
    candidate_votes = {}

    candidate_votes["Khan"] = 0
    candidate_votes["Correy"] = 0
    candidate_votes["Li"] = 0
    candidate_votes["O'Tooley"] = 0
    count = 0

    for row in reader:
        count += 1

        if row[2] == "Khan":
            candidate_votes["Khan"] = candidate_votes["Khan"] + 1
            # this syntax is the same as candidate_votes["Khan"] += 1
        elif row[2] == "Correy":
            candidate_votes["Correy"] += 1
        elif row[2] == "Li":
            candidate_votes["Li"] += 1
        else:
            candidate_votes["O'Tooley"] +=1 
                
    #Calculate total sum of votes cast
    print("Election Results")
    print("___________________________")
    print(("Total Votes: ")+ str(count))
    print("___________________________")
    
    #Percentage of votes won by each candidate
    percent_Khan = candidate_votes["Khan"] / count
    percent_Correy = candidate_votes["Correy"] / count
    percent_Li = candidate_votes["Li"] / count
    percent_OTooley = candidate_votes["O'Tooley"] / count
    
    #print(percent_Khan)
    print("Khan: " + str(round((percent_Khan * 100), 2)) + "% " + "(" + str(candidate_votes["Khan"]) + ")")
    print("Correy: " + str(round((percent_Correy * 100), 2)) + "% " + "(" + str(candidate_votes["Correy"]) + ")")
    print("Li: " + str(round((percent_Li * 100), 2)) + "% " + "(" + str(candidate_votes["Li"]) + ")")
    print("O'Tooley: " + str(round((percent_OTooley * 100), 2)) + "% " + "(" + str(candidate_votes["O'Tooley"]) + ")") 
    print("___________________________")

    #Election winner
    total_cand_votes = [2218231, 704200, 492940, 105631]
    total_cand_names = ["Khan", "Correy", "Li", "O'Tooley"]
    max_winner = max(total_cand_votes)
    index = total_cand_votes.index(max_winner)
    winning_candidate = total_cand_names[index]
    print(winning_candidate)

with open(election_output,'w') as txtfile:
    print("Election Results",file=txtfile,end='\n')
    print("___________________________",file=txtfile,end='\n')
    print(("Total Votes: ")+ str(count),file=txtfile,end='\n')
    print("___________________________",file=txtfile,end='\n')

    print("Khan: " + str(round((percent_Khan * 100), 2)) + "% " + "(" + str(candidate_votes["Khan"]) + ")",file=txtfile,end='\n')
    print("Correy: " + str(round((percent_Correy * 100), 2)) + "% " + "(" + str(candidate_votes["Correy"]) + ")",file=txtfile,end='\n')
    print("Li: " + str(round((percent_Li * 100), 2)) + "% " + "(" + str(candidate_votes["Li"]) + ")",file=txtfile,end='\n')
    print("O'Tooley: " + str(round((percent_OTooley * 100), 2)) + "% " + "(" + str(candidate_votes["O'Tooley"]) + ")",file=txtfile,end='\n') 
    print("___________________________",file=txtfile,end='\n')

    print(winning_candidate,file=txtfile,end='\n')


