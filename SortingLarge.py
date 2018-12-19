collection = [[173346, '7 Wonders Duel', 326707, 'Dutch/English/Korean edition', ['Dutch', 'English', 'Korean'], 2016, 12.126, 12.126, 2.04724, 1.54324], [180263, 'The 7th Continent', 278264, 'English first edition', ['English'], 2017, 8.85827, 12.4016, 4.25197, 7.27525], [205637, 'Arkham Horror: The Card Game', 320688, 'English edition', ['English'], 2016, 10.0, 10.0, 2.0, 2.0503], [37111, 'Battlestar Galactica: The Board Game', 24172, 'English first edition', ['English'], 2008, 11.7, 11.7, 2.8, 3.06], [84876, 'The Castles of Burgundy', 141049, 'Ravensburger English/French edition', ['English', 'French'], 2011, 8.625, 12.2, 2.625, 2.0], [102794, 'Caverna: The Cave Farmers', 415726, 'English third edition', ['English'], 2017, 8.93701, 12.5197, 4.05512, 0.0], [124361, 'Concordia', 364284, 'English-only third edition', ['English'], 2017, 10.7, 14.6, 2.2, 0.0], [220308, 'Gaia Project', 343321, 'English edition', ['English'], 2017, 11.811, 14.3701, 3.14961, 0.0], [174430, 'Gloomhaven', 268248, 'English Kickstarter minis edition', ['English'], 2017, 11.5, 16.0, 7.5, 19.0], [193738, 'Great Western Trail', 300884, 'English-only first edition', ['English'], 2016, 0.0, 0.0, 0.0, 0.0], [161936, 'Pandemic Legacy: Season 1', 245176, 'English blue edition', ['English'], 2015, 10.625, 14.625, 3.0, 4.9], [3076, 'Puerto Rico', 343715, 'Chinese/English edition', ['Chinese', 'English'], 2011, 10.7, 14.6, 2.2, 0.0], [169786, 'Scythe', 290632, "English collector's edition", ['English'], 2016, 11.811, 14.3701, 3.85827, 0.0], [187645, 'Star Wars: Rebellion', 290665, 'English edition', ['English'], 2016, 11.5748, 11.5748, 5.35433, 6.14649], [120677, 'Terra Mystica', 189525, 'English/French first edition', ['English', 'French'], 2013, 8.8, 12.4, 3.6, 5.5], [167791, 'Terraforming Mars', 256624, 'English first edition, first printing', ['English'], 2016, 11.7, 11.7, 2.8, 0.0], [182028, 'Through the Ages: A New Story of Civilization', 281479, 'English edition', ['English'], 2015, 10.0394, 14.5669, 2.95276, 3.96832], [233078, 'Twilight Imperium (Fourth Edition)', 365218, 'English edition', ['English'], 2017, 11.811, 17.047, 5.276, 10.5161], [12333, 'Twilight Struggle', 243057, "English collector's edition", ['English'], 2016, 13.0, 10.0, 4.0, 8.0], [183394, 'Viticulture Essential Edition', 283706, 'English edition', ['English'], 2015, 8.66142, 10.6299, 4.13386, 4.27697], [115746, 'War of the Ring (Second Edition)', 142738, 'English first edition', ['English'], 2011, 11.0, 16.0, 3.5, 6.56]]
expansionCollection = [[141648, 'Battlestar Galactica: The Board Game – Daybreak Expansion', 207222, 'English edition', ['English'], 2013, 11.8, 11.8, 3.0, 2.5, 37111, 'Battlestar Galactica: The Board Game'], [85905, 'Battlestar Galactica: The Board Game – Exodus Expansion', 78371, 'English edition', ['English'], 2010, 11.7, 11.7, 2.8, 0.0, 37111, 'Battlestar Galactica: The Board Game'], [43539, 'Battlestar Galactica: The Board Game – Pegasus Expansion', 283614, 'English second edition', ['English'], 2013, 11.7, 11.7, 2.8, 0.0, 37111, 'Battlestar Galactica: The Board Game'], [218103, 'Clank!: Sunken Treasures', 339646, 'English edition', ['English'], 2017, 0.0, 0.0, 0.0, 0.0, 201808, 'Clank!: A Deck-Building Adventure'], [161317, 'Terra Mystica: Fire & Ice', 337457, 'English/French second edition', ['English', 'French'], 2016, 12.4016, 8.85827, 2.3622, 3.08647, 120677, 'Terra Mystica']]
priorityGames = []

shelfWidth = 13 + 1/8
shelfDepth = 15 + 3/8
shelfHeight = 13 + 1.5/8
numCubicles = 100
tolerance = 2/8
tolChange = 1/16


#I want to manipulate these two list, would like to have originals though
collectionCopy = collection
expansionCollectionCopy = expansionCollection

import itertools
numbers = [1, 2, 3, 4, 5, 6, 7]

def findSum(numbers, target, tolerance):
    for i in range(1, len(numbers)+1):
        for comb in itertools.combinations(numbers, i): 
           if abs(sum(comb) - target) < tolerance:
               return comb


def calcSum(games, target, tolerance):
    for i in range(1, len(games)+1):
        for comb in itertools.combinations(enumerate(games), i): 
           if abs(sum(comb) - target) < tolerance:
               return comb
#findSum(numbers, 13, 0.5)

#Used to fill in a cubicle that is partially filled with priority games            
def PCalcSum(heightSum, games, target, tolerance):
    target -= heightSum
    for i in range(1, len(games)+1):
        for comb in itertools.combinations(enumerate(games), i):
            #have to add 1 to each value in combIndex because we splice the list when calling this function
            combIndex = [x[0] + 1 for x in comb]
            combVal = [x[1] for x in comb]            
            if target - sum(combVal) < tolerance and target - sum(combVal) > 0:
                return combIndex
    return []

#MixedCalcSum(PCollectionHeight[0], PCollectionHeight[1:], collectionHeight, shelfWidth, tolerance)

#Used to fill in a cubicle that is partially filled with priority games, but will pull from both priority lists and regular collection
def MixedCalcSum(PHeightSum, PGames, CGames, target, tolerance):
    target -= PHeightSum
    #While we normally prioritize larger size over # of games, we make an exception here. This is because we want more games from the priority group added to the shelf
    for i in reversed(range(0, len(PGames)+1)):
        for PComb in itertools.combinations(enumerate(PGames), i):
            PCombIndex = [x[0] + 1 for x in PComb]
            PCombVal = [x[1] for x in PComb] 
            #We compare every permutation of the priority games with every permutation of regular games
            for i in range(1, len(CGames)+1):
                for CComb in itertools.combinations(enumerate(CGames), i):
                    CCombIndex = [x[0] for x in CComb]
                    CCombVal = [x[1] for x in CComb] 
                    if target - (sum(PCombVal) + sum(CCombVal)) < tolerance and target - (sum(PCombVal) + sum(CCombVal)) > 0:
                        combIndex = []
                        combIndex.append(PCombIndex)
                        combIndex.append(CCombIndex)
                        return combIndex
    return []
            

def insertByWeight(finalShelf, finalShelfWeight, grouping):
    #Weight of the games in this grouping
    groupWeight = 0
    for game in grouping:
        groupWeight += game[9]
    if finalShelf:
        inserted = False
        #iterate through each shelf cubicle to organize from highest weight to lowest weight
        for counter, sortedGroupWeight in enumerate(finalShelfWeight):
            if groupWeight > sortedGroupWeight:
                finalShelf.insert(counter, grouping)
                finalShelfWeight.insert(counter, groupWeight)
                inserted = True
                break
        #Checks if values were inserted. If they weren't, it means that this is the smallest weighted value in the listing.
        if inserted == False:
            finalShelf.append(grouping)
            finalShelfWeight.append(groupWeight)
    else:
        finalShelf.append(grouping)
        finalShelfWeight.append(groupWeight)
        
def removeGames(collectionCopy, index):
    #Index is sorted from smallest to largest, so this allows us to remove games without affecting the index position of them
    for number in reversed (index):
        del collectionCopy[number]
    


#Group expansion games with base games and then place them in priority array
counter = 0
while counter < len(expansionCollectionCopy):
    priorityGroup = []
    #Get base game ID
    baseGame = expansionCollectionCopy[counter][len(expansionCollectionCopy[counter])-2]
    baseGameExist = False
    #Add corresponding base game to the list
    for y in range(len(collectionCopy)-1):
        if collectionCopy[y][0] == baseGame:
            priorityGroup.append(collectionCopy[y])
            del collectionCopy[y]
            baseGameExist = True
            break
    if baseGameExist == True:
        #Add current expansion to the list
        priorityGroup.append(expansionCollectionCopy[counter])
        del expansionCollectionCopy[counter]
        #Get all other games with the same base expansion
        z = 0
        while z < len(expansionCollectionCopy):
            #If the same base game, add it to the current array and then remove the game from the list
            if baseGame == expansionCollectionCopy[z][len(expansionCollectionCopy[z])-2]:
                priorityGroup.append(expansionCollectionCopy[z])
                del expansionCollectionCopy[z]
                z -= 1
            z += 1
        priorityGames.append(priorityGroup)
    else:
        counter += 1
    
#We need to do this in case we own expansions WITHOUT the base game
collectionCopy.extend(expansionCollectionCopy)
#print(collectionCopy)

collectionHeight = []
#need to isolate height info in collection array (itertools.combinations won't function in current form)
for grouping in collectionCopy:
    collectionHeight.append(grouping[8])


PCollectionHeight = []
#need to isolate height info in priority collection array (itertools.combinations won't function in current form)
for grouping in priorityGames:
    heightSum = 0
    for game in grouping:
        heightSum += game[8]
    PCollectionHeight.append(heightSum)
        
    
#This is for any priority games that don't have a combination of other games that fill up to the threshold.
PUnfilledShelf = []
#Weight of each incomplete shelf
PUnfilledShelfWeight = []
#These will be filled later at the very end with a larger threshold value, after other games are filled with the current threshold
UnfilledShelf = []
#Weight of each incomplete shelf
UnfilledShelfWeight = []
#These are the games that will be guaranteed to be on the shelf (Priority games + whichever games fill up the shelf)
PFinalShelf = []
#The weight of each shelf cubicle. Will be used to determine where they are placed on the shelf
PFinalShelfWeight = []
#The non-priority games that will be on the shelf
finalShelf = []
#The weight of each shelf cubicle. Will be used to determine where they are placed on the shelf
finalShelfWeight = []

#Check to see if each grouping is smaller than the size of a shelf. Break-up the grouping if it is
for counter, grouping in enumerate(priorityGames):
    #Check if the grouping of priority games is larger than the shelf width
    if PCollectionHeight[counter] > shelfWidth:
        #Find the amount of width we need to remove for the game to fit
        extraWidth = PCollectionHeight[counter] - shelfWidth
        #These three variables make it easier to delete the listing without needing to iterate through the list again
        smallestExtra = [grouping[0]]
        smallestExtraIndex = 0
        for i in range(1, len(grouping)+1):
                for games in itertools.combinations(enumerate(grouping), i):
                    height = [el[1][8] for el in games]
                    #check to see if this game(s) is the smallest batch of games that is also larger than the threshold we need to remove
                    if height < smallestExtra[8] and height > shelfWidth:
                        smallestExtra = [el[1] for el in games]
                        smallestExtraIndex = [el[0] for el in games]
                        for index in smallestExtraIndex:
                            del priorityGames[counter][index]
                        for index in smallestExtra:
                            PCollectionHeight[counter] -= index[8]
                        priorityGames.insert(counter + 1, smallestExtra)
                        PCollectionHeight.insert(counter + 1, sum(el[8] for el in smallestExtra))
                        



#Sort the games in the following manner:
#1. Sort priority games 
#2. Reduce tolerance on priority games and continue sorting
#3. Repeat Step 2 until all games are sorted
#4. Sort regular games
#5. Reduce tolerance on regular games and continue sorting
#6. Repeat Step 5 until all games are sorted                        

def prioritySort():
    return 1

#Will change over time
tempTolerance = tolerance

while priorityGames:
    counter = 0
    while counter < len(priorityGames):
        #If the grouping of games (base + expansion) happens to be a perfect fit for the shelves, we can allocate one entire cubicle for this shelf
        if shelfWidth - PCollectionHeight[counter] < tempTolerance and shelfWidth - PCollectionHeight[counter] > 0:
            #print ("shelfWidth = ", shelfWidth, ", Priority Collection Height = ", PCollectionHeight[0], "tolerance = ", tolerance) 
            insertByWeight(PFinalShelf, PFinalShelfWeight, priorityGames[counter])
            del PCollectionHeight[counter]
            del priorityGames[counter]
        else:
            #If it's not a perfect fit, try grouping with other priority shelves first
            combination = []
            #There needs to be more than one grouping to try this
            if len(priorityGames) > 1:
                combination = PCalcSum(PCollectionHeight[counter], PCollectionHeight[counter+1:], shelfWidth, tempTolerance)
            #If we find a combination of games that fits the shelf
            if combination:
                for gameNum in combination:
                    priorityGames[counter].extend(priorityGames[gameNum])
                #removes the priority games from the list so that we don't use them in other shelf combinations
                removeGames(priorityGames, combination)
                removeGames(PCollectionHeight, combination)
                insertByWeight(PFinalShelf, PFinalShelfWeight, priorityGames[counter])
                del PCollectionHeight[counter]
                del priorityGames[counter]    
            else:
                #Find a combination through both priority + regular games, with an emphasis on priority games first
                combination = MixedCalcSum(PCollectionHeight[counter], PCollectionHeight[counter + 1:], collectionHeight, shelfWidth, tempTolerance)
                #we're ordering the conditionals in this manner because in the majority of cases it will be a length of size 2. 
                if (len(combination) == 2):
                    for gameNum in combination[0]:
                        priorityGames[counter].extend(priorityGames[gameNum])
                    for gameNum in combination[1]:
                        priorityGames[counter].append(collectionCopy[gameNum])
                    insertByWeight(PFinalShelf, PFinalShelfWeight, priorityGames[counter])
                    removeGames(priorityGames, combination[0])
                    removeGames(collectionCopy, combination[1])
                    removeGames(PCollectionHeight, combination[0])
                    removeGames(collectionHeight, combination[1])
                    del priorityGames[counter]
                    del PCollectionHeight[counter]
                    print("A combination of both priority games and regular games were added to the current priority games to fill the shelf")
                #if there is only one list, it means that there were 0 games in the priority game list that fills in the gap
                elif (len(combination) == 1):
                    for gameNum in combination[0]:
                        priorityGames.extend(collectionCopy[gameNum])
                    insertByWeight(PFinalShelf, PFinalShelfWeight, priorityGames[0])
                    removeGames(collectionCopy, combination[1])
                    removeGames(collectionHeight, combination[1])
                    print("Only regular games were added to the current priority games to fill the shelf")
                    del priorityGames[counter]
                    del PCollectionHeight[counter]
                elif not combination:
                    #print ("No additional games will fit on this shelf with current tolerance threshold")
                    counter += 1
                    #insertByWeight(PUnfilledShelf, PUnfilledShelfWeight, priorityGames[0])
    #Increase the tolerance value for any remaining priority games
    tempTolerance += tolChange
    


#Reset temp tolerance value
tempTolerance = tolerance

print(collectionCopy)
while collectionCopy:
    counter = 0
    while counter < len(collectionCopy):
        #If the single game happens to be a perfect fit for the shelves, we can allocate one entire cubicle for this one game
        if shelfWidth - collectionHeight[counter] < tempTolerance and shelfWidth - collectionHeight[counter] > 0:
            insertByWeight(finalShelf, finalShelfWeight, collectionCopy[counter])
            print("Regular Game Add: perfect for shelf (tolerance accounted for). Tolerance = ", tempTolerance)
            print(collectionCopy[counter])
            del collectionHeight[counter]
            del collectionCopy[counter]
        #While all the remaining games can't fit on one cubicle
        elif sum(collectionHeight) > shelfWidth:
            #Find a combination through remaining games
            #def PCalcSum(heightSum, games, target, tolerance):
            combination = PCalcSum(collectionHeight[counter], collectionHeight[counter+1:], shelfWidth, tempTolerance)
            #adds square brackets to make it become a list of lists
            if combination:
                if counter == 0:
                    collectionCopy[counter] = [collectionCopy[counter]]
                #print (collectionCopy)
                #print ("combination = ", combination)
                for gameNum in combination:
                    collectionCopy[counter].append(collectionCopy[gameNum])
                    print("index value = ", gameNum)
                #removes the regular games from the list so that we don't use them in other shelf combinations
                insertByWeight(finalShelf, finalShelfWeight, collectionCopy[counter])
                print("Regular Game Add: Added some additional games to current game (tolerance accounted for). Tolerance = ", tempTolerance)
                print(collectionCopy[counter])
                removeGames(collectionCopy, combination)
                removeGames(collectionHeight, combination)
                del collectionHeight[counter]
                del collectionCopy[counter]
            else:
                #print ("No additional games will fit on this shelf")
                counter += 1
                #insertByWeight(UnfilledShelf, UnfilledShelfWeight, collectionCopy[counter])
        #All remaining games fit on shelf
        else:
            insertByWeight(finalShelf, finalShelfWeight, collectionCopy)
            print("Regular Game Add: Added all remaining games to current game (tolerance accounted for). Tolerance = ", tempTolerance)
            print(collectionCopy)
            collectionHeight = []
            collectionCopy = []
    #Increase the tolerance value for any remaining priority games
    tempTolerance += tolChange   
print("----------------------------Complete----------------------------")
print("Priority Unfilled Shelf = ", PUnfilledShelf)
print("----------------------------")
print("Regular Unfilled Shelf = ", UnfilledShelf)
print("----------------------------")
print("Priority Final Shelf = ", PFinalShelf)
print("----------------------------")
print("Regular Final Shelf = ", finalShelf)
print("----------------------------")

shelf = PFinalShelf
shelf.extend(finalShelf)

print (shelf)

#Now we need to do the entire thing again, with the items in the Unfilled Shelves. It may be beneficial to rework entire set of while loops into a larger loop instead





        ########This set of code is reserved for extreme cases where no games will allow this set of games to reach the threshold. In this case, the games are just added to a shelf as is.
        ########The intent is to fill it using a greater tolerance value later
        
        


#for grouping in collectionCopy:
    

#nested itertools.combinations needed when combining priority games + regular games

        
    #Fill in gaps in priority listing where there wasn't a combination that met the threshold


        


