#Program begins
#Player vs Player Batting Data
#This program will give "Batsman, Bowler, Score, Balls"

import csv
import yaml
from time import time

#Code Snippets

#Snippet to Load a file
def yaml_loader(filepath):
    with open(filepath,"r") as file_descriptor:
        data=yaml.load(file_descriptor)
    return data

# Snippet to reverse a list using reversed() 
def Reverse(lst): 
	return [ele for ele in reversed(lst)] 

#Snippet to check whether entry is in the dictionary or not
def check_or_add(type,tup):
    if(type==0):
        bowler_batsman[tup]=[0,0,0]
    else:
        batsman_bowler[tup]=[0,0,0,0,0,0,0,0,0,0]


#Main Code Starts from here


#Some matches may not have equal innings
innings1=0
innings2=0

filepath="/home/srikar/Desktop/Big_Data_Project/Phase_1/data/"
extension=".yaml"

#For bowler I want to find for each batsman how many runs he's given and how many wickets he's taken
#For that purpose this dictionary
#Pattern : Bowler, Batsman, Wickets, Runs_given
bowler_batsman=dict()

#For batsman I want to find how many wickets lost to each bowler and how many runs against that bowler
#For that purpose this dictionary
#Pattern : Batsman, Bowler, Runs_scored_totally, Times_out, Singles, Doubles, Triples, 4's, 6's, Total_balls_faced_against_that_bowler
batsman_bowler=dict()

for num in range(335983,1082651):
    #If the file is there, the loaded other wile exception and goes to next loop
    try:
        d=yaml_loader(filepath+str(num)+extension)
    except FileNotFoundError:
        continue

    total_innings=d["innings"]
    first=total_innings[0]
    first_innings_deliveries=first['1st innings']['deliveries']
    second_innings_deliveries=dict()
    innings1+=1

    for i in first_innings_deliveries:
            k=list(i.keys())
            req_dict=i[k[0]]

            if('wicket' in req_dict.keys()):
                bowler=req_dict['bowler']
                batsman=req_dict['wicket']['player_out']
                if((bowler,batsman) not in bowler_batsman.keys()):
                    check_or_add(0,(bowler,batsman))
                if((batsman,bowler) not in batsman_bowler.keys()):
                    check_or_add(1,(batsman,bowler))
                row1=bowler_batsman[(bowler,batsman)]
                row2=batsman_bowler[(batsman,bowler)]
                row1[0]+=1;row1[2]+=1
                row2[1]+=1;row2[2]+=1
                bowler_batsman[(bowler,batsman)]=row1
                batsman_bowler[(batsman,bowler)]=row2
            else:
                bowler=req_dict['bowler']
                batsman=req_dict['batsman']
                if((bowler,batsman) not in bowler_batsman.keys()):
                    check_or_add(0,(bowler,batsman))
                if((batsman,bowler) not in batsman_bowler.keys()):
                    check_or_add(1,(batsman,bowler))
                runs=int(req_dict['runs']['total'])
                row1=bowler_batsman[(bowler,batsman)]
                row2=batsman_bowler[(batsman,bowler)]
                row1[1]+=runs;row1[2]+=1
                if(runs>6):
                    runs=6
                row2[0]+=runs;row2[runs+3]+=1
    
    if(len(total_innings)==2):
        second=total_innings[1]
        second_innings_deliveries=second['2nd innings']['deliveries']
        innings2+=1
    else:
        continue
    
    for i in second_innings_deliveries:
            k=list(i.keys())
            req_dict=i[k[0]]

            if('wicket' in req_dict.keys()):
                bowler=req_dict['bowler']
                batsman=req_dict['wicket']['player_out']
                if((bowler,batsman) not in bowler_batsman.keys()):
                    check_or_add(0,(bowler,batsman))
                if((batsman,bowler) not in batsman_bowler.keys()):
                    check_or_add(1,(batsman,bowler))
                row1=bowler_batsman[(bowler,batsman)]
                row2=batsman_bowler[(batsman,bowler)]
                row1[0]+=1;row1[2]+=1
                row2[1]+=1;row2[2]+=1
                bowler_batsman[(bowler,batsman)]=row1
                batsman_bowler[(batsman,bowler)]=row2
            else:
                bowler=req_dict['bowler']
                batsman=req_dict['batsman']
                if((bowler,batsman) not in bowler_batsman.keys()):
                    check_or_add(0,(bowler,batsman))
                if((batsman,bowler) not in batsman_bowler.keys()):
                    check_or_add(1,(batsman,bowler))
                runs=int(req_dict['runs']['total'])
                row1=bowler_batsman[(bowler,batsman)]
                row2=batsman_bowler[(batsman,bowler)]
                row1[1]+=runs;row1[2]+=1
                if(runs>6):
                    runs=6
                row2[0]+=runs;row2[runs+3]+=1

row=list()

print("Computation done, Printing/Writing")

for i in bowler_batsman.keys():
    try:
        print(list(i)+bowler_batsman[i])
    except:
        continue

print("\n\n")

for i in batsman_bowler.keys():
    try:
        print(list(i)+batsman_bowler[i])
    except:
        continue

#Program ends
