#Program begins
#Player vs Player Batting Data
#This program will give "Batsman, Bowler, Score, Balls"

import csv
import yaml
from time import time
from math import sqrt

#Code Snippets

#Snippet to Load a file
def yaml_loader(filepath):
    with open(filepath,"r") as file_descriptor:
        data=yaml.load(file_descriptor)
    return data

# Snippet to reverse a list using reversed() 
def Reverse(lst): 
	return [ele for ele in reversed(lst)] 


#Main Code Starts from here

#Some matches may not have equal innings
innings1=0
innings2=0

filepath="/home/srikar/Desktop/Big_Data_Project/Phase_1/data/"
extension=".yaml"

#For batsman dict will be 
#Name , runs, balls, out_times
batsman_dict=dict()

#For bowler dict will be
#Name , wickets, balls, runs_given
bowler_dict=dict()


#Function that does the main job
def magic_function(i):
    k=list(i.keys())
    req_dict=i[k[0]]
    bowler=req_dict['bowler']
    if('wicket' in req_dict.keys()):
        batsman=req_dict['wicket']['player_out']
        if(bowler in bowler_dict.keys()):
            temp=bowler_dict[bowler]
            temp[0]=temp[0]+1;temp[1]=temp[1]+1
            bowler_dict[bowler]=temp
        else:
            temp=[1,1,0]
            bowler_dict[bowler]=temp
        if(batsman in batsman_dict.keys()):
            temp=batsman_dict[batsman]
            temp[1]=temp[1]+1;temp[2]=temp[2]+1
            batsman_dict[batsman]=temp
        else:
            temp=[0,1,1]
            batsman_dict[batsman]=temp
    else:
        runs=req_dict['runs']['total']
        batsman=req_dict['batsman']
        if(bowler in bowler_dict.keys()):
            temp=bowler_dict[bowler]
            temp[1]=temp[1]+1;temp[2]=temp[2]+int(runs)
            bowler_dict[bowler]=temp
        else:
            temp=[0,1,int(runs)]
            bowler_dict[bowler]=temp
        if(batsman in batsman_dict.keys()):
            temp=batsman_dict[batsman]
            temp[0]=temp[0]+int(runs);temp[1]=temp[1]+1
            batsman_dict[batsman]=temp
        else:
            temp=[int(runs),1,0]
            batsman_dict[batsman]=temp
                

for num in range(335983,1082651):
    #If the file is there, the loaded other wile exception and goes to next loop
    try:
        d=yaml_loader(filepath+str(num)+extension)
    except FileNotFoundError:
        continue
    #print(num)

    total_innings=d["innings"]
    first=total_innings[0]
    first_innings_deliveries=first['1st innings']['deliveries']
    second_innings_deliveries=dict()
    innings1+=1

            #For each ball I must compute and store it in both files
            #Very slow
            
    for i in first_innings_deliveries:
        magic_function(i)

    if(len(total_innings)==2):
        second=total_innings[1]
        second_innings_deliveries=second['2nd innings']['deliveries']
        innings2+=1
    else:
        continue
    
    for i in second_innings_deliveries:
        magic_function(i)

#What heuristics to use
#For bowler goodness is directly proportional to the number of wickets he takes
#and inversely proportional to the square root of runs he gives

#For batsman goodness is directly proprotional to the number of runs he scores
#and 

counter=0

for i in bowler_dict.keys():
    l=bowler_dict[i]
    if(l[2]==0):
        l[2]=1
    value=l[0]/sqrt(l[2])
    #print(counter,value,i)
    print(counter,"1:"+value)
    counter=counter+1
    #This if for the clustering

print("\n\n\n\n\n")

counter=0
for i in batsman_dict.keys():
    l=batsman_dict[i]
    if(l[2]==0):
        l[2]=1
    value=l[0]/l[2]
    #print(counter,value,i)
    print(counter,"1:"+value)
    counter=counter+1
    #This if for the clustering
    
#Program ends