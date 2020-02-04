unsortedlist =[['name1', 10], ['name2', 5], ['name3', 20], ['name4', 15]]

def Sort(unsortedList):
    return(sorted(unsortedList, key = lambda x: x[1]))

print(Sort(unsortedList))
