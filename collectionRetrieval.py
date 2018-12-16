import xml.etree.ElementTree as ET
from urllib.request import urlopen

collectionXml = urlopen('https://www.boardgamegeek.com/xmlapi2/collection?username=shelfspace&brief=1&own=1&version=1')
collectionTree = ET.parse(collectionXml)
collectionRoot = collectionTree.getroot()

collection = []
expansionCollection = []

for child in collectionRoot:
    currentGame = []
    
    #add game ID
    if child.tag=='item':
        currentGame.append(int(child.attrib['objectid']))
    else:
        currentGame.append(None)
    #add game name
    currentGame.append(child.find('name').text)

    #get info of board game (needed later on to check if game is base or expansion)
    gameXml = urlopen('https://www.boardgamegeek.com/xmlapi2/thing?id=%s&versions=1' % currentGame[0])
    gameTree = ET.parse(gameXml)
    gameRoot = gameTree.getroot()
        
    if child.find('version'):
        version = child.find('version').find('item')
        #add version ID
        currentGame.append(int(version.attrib['id']))
        #add version
        currentGame.append(version.find('name').attrib['value'])
        #add language(s)
        language = []
        for link in version.findall('link'):
            if link.get('type') == 'language':
                language.append(link.get('value'))
        currentGame.append(language)
            
        #add year published
        if version.find('yearpublished').attrib['value']:
            currentGame.append(int(version.find('yearpublished').attrib['value']))
        #add width
        if version.find('width').attrib['value']:
            currentGame.append(float(version.find('width').attrib['value']))
        #add length
        if version.find('length').attrib['value']:
            currentGame.append(float(version.find('length').attrib['value']))
        #add depth
        if version.find('depth').attrib['value']:
            currentGame.append(float(version.find('depth').attrib['value']))
        #add weight
        if version.find('weight').attrib['value']:
            currentGame.append(float(version.find('weight').attrib['value']))
    else:
        #get latest english version
        

        gameVersion = gameRoot.find('item').find('versions')

        #newest version entry (just in case no english version exists
        missingInfo = []
        #add version ID
        missingInfo.append(int(gameVersion.find('item').attrib['id']))
        #add version
        missingInfo.append(gameVersion.find('item').find('name').attrib['value'])
        #add language(s)
        language = []
        for link in gameVersion.find('item').findall('link'):
            if link.get('type') == 'language':
                language.append(link.get('value'))
        missingInfo.append(language)
        #add year published
        if gameVersion.find('item').find('yearpublished').attrib['value']:
            missingInfo.append(int(gameVersion.find('item').find('yearpublished').attrib['value']))
        #add width
        if gameVersion.find('item').find('width').attrib['value']:
            missingInfo.append(float(gameVersion.find('item').find('width').attrib['value']))
        #add length
        if gameVersion.find('item').find('length').attrib['value']:
            missingInfo.append(float(gameVersion.find('item').find('length').attrib['value']))
        #add depth
        if gameVersion.find('item').find('depth').attrib['value']:
            missingInfo.append(float(gameVersion.find('item').find('depth').attrib['value']))
        #add weight
        if gameVersion.find('item').find('weight').attrib['value']:
            missingInfo.append(float(gameVersion.find('item').find('weight').attrib['value']))
            
        if 'English' in missingInfo[2] == True:
            currentGame.extend(missingInfo)
        else:
            #setup english info
            englishMissingInfo = []
            #check if an english version is found, needed to break out of nested for loop
            found = False
            for x in gameVersion:
                if found == True:
                    break
                #check if at least one of the supported versions in this game is english
                for y in x.findall('link'):
                    if y.get('type') == 'language':
                        if y.get('value') == 'English':
                            #add version ID
                            englishMissingInfo.append(int(x.attrib['id']))
                            #add version
                            englishMissingInfo.append(x.find('name').attrib['value'])
                            #add language(s)
                            language = []
                            for z in x.findall('link'):
                                if z.get('type') == 'language':
                                    language.append(z.get('value'))
                            englishMissingInfo.append(language)
                            #add year published
                            if x.find('yearpublished').attrib['value']:
                                englishMissingInfo.append(int(x.find('yearpublished').attrib['value']))
                            #add width
                            if x.find('width').attrib['value']:
                                englishMissingInfo.append(float(x.find('width').attrib['value']))
                            #add length
                            if x.find('length').attrib['value']:
                                englishMissingInfo.append(float(x.find('length').attrib['value']))
                            #add depth
                            if x.find('depth').attrib['value']:
                                englishMissingInfo.append(float(x.find('depth').attrib['value']))
                            #add weight
                            if x.find('weight').attrib['value']:
                                englishMissingInfo.append(float(x.find('weight').attrib['value']))
                            found = True
                            break
            if found == True:
                currentGame.extend(englishMissingInfo)
            else:
                currentGame.extend(missingInfo)
    if gameRoot.find('item').attrib['type'] == 'boardgame':
        #add game to collection            
        collection.append(currentGame)
    elif gameRoot.find('item').attrib['type'] == 'boardgameexpansion':
        for x in gameRoot.find('item').findall('link'):
            if x.get('type') == 'boardgameexpansion':
                currentGame.append(int(x.get('id')))
                currentGame.append(x.get('value'))
                #add game to collection            
                expansionCollection.append(currentGame)
        
            
print(collection)
print(expansionCollection)



        
