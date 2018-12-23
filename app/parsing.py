#This file has been temporarily created as I haven't decided how to send the
#information back to the webpage. We don't need ALL of the information gathered,
#but at the same time I don't want to use app.py to modify the information.
#This way we can have a few custom parsers

def basicParse(shelf):
    parsedShelf = []
    for grouping in shelf:
        tempGroup = []
        for game in grouping:
            tempGame = []
            #game name
            tempGame.append(game[1])
            #game thumbnail
            tempGame.append(game[10])
            tempGroup.append(tempGame)
        parsedShelf.append(tempGroup)
    return parsedShelf

            
        
