import copy

#In this one load all the probabilities
#You can do it in your file
#Not doing it here
orig_dict_bow={}


#To get the not out probability
for i in orig_dict_bow.keys():
    orig_dict_bow[i]=orig_dict_bow[i]-1

changing_dict=copy.deepcopy(orig_dict_bow)


#This is just an example dont copy ditto
#This is a function that you can call to check if the guy is out or not
def out_or_not(bowler,batsman):
    if(changing_dict[(bowler,batsman)]['give the index']<0.5):
        return True
    else:
        changing_dict[(bowler,batsman)]*=orig_dict_bow[(bowler,batsman)]
    return False