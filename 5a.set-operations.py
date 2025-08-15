#Looking at why sets are useful

epl = {"Liverpool", "ManU", "ManC", "Tottenham", "Arsenal","Chelsea","NewCastle", "West Ham", "Wolves"}
ecl = {"Liverpool","ManC", "Tottenham", "Arsenal","Chelsea"}

#set operations
not_ecl = epl.difference(ecl) #finds the element that is not present from the first set while comparing it to the second set
all_teams = epl.union(ecl) # combines both sets and generates a new set with all the elements
big_teams = epl.intersection(ecl) # selects the elements similar in both sets and generates a new set


print(not_ecl)
print(all_teams)
print(big_teams)





