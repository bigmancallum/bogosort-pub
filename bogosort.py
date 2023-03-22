from random import randint, shuffle #For choosing random number and shuffling lists

timesRandomised = 0 #Sets amount of time randomised to zero
list = [] #Starts list off blank

#Ask user for length of list and creates a list with that many random numbers in it
listLen = int(input("How many numbers do you want in the list? "))
rangeNum1 = int(input("What do you want the numbers in the list to be between? (first number) "))
rangeNum2 = int(input("What do you want the numbers in the list to be between? (second number) "))
for i in range(listLen):
  ranNum = randint(rangeNum1, rangeNum2)
  list.append(ranNum)

print(f"List: {list}\n") #Prints the random list

#Makes a copy of the random list and orders it it
sortedList = list[:]
sortedList.sort()

#While the list doesn't match the sorted copy, say it's not sorted, randomise it, and print it
while list != sortedList:
  print("\nThe list is not sorted.")
  shuffle(list)
  timesRandomised += 1
  print (list)

#When the list matches the sorted copy, say it's sorted, say how many times it was sorted, and print the sorted list
print(f"\n\nThe list is sorted.\n\nSorted list: {list}\n\nIt took {timesRandomised} sorts to put the list in order.")
