# Lib imports
import json

# Local imports
from utils.format import Format

class TomesDB:
    # Create Tomes
    def TomeNodesData(parsedValues, nodeID, objectiveID, level):
        with open('DeadByDaylight\Content\Data\Archives\ArchiveNodeDB.json', 'r') as archiveNode:
            parsedArchiveNode = json.load(archiveNode)
        with open('DeadByDaylight\Content\Data\Archives\ArchiveQuestObjectiveDB.json', 'r') as archiveQuestObjective:
            parsedQuestObjective = json.load(archiveQuestObjective)
        with open('output\Perks.json', 'r') as perksJson:
            parsedPerks = json.load(perksJson)
        with open('components\CharactersID.json', 'r') as charactersIDJson:
            parsedCharactersID = json.load(charactersIDJson)
        with open('output\Characters.json', 'r') as charactersJson:
            parsedCharacters = json.load(charactersJson)
        with open('output\Cosmetics.json', 'r') as cosmeticsJson:
            parsedCosmetics = json.load(cosmeticsJson)

        for nodeKey in parsedArchiveNode[0]['Rows']:
            if parsedValues['level'][level]['nodes'][nodeID]['clientInfoId'] == 'reward':
                nodeName = 'Reward'
                if parsedValues['level'][level]['nodes'][nodeID]['reward'][0]['type'] == 'inventory':
                    for cosmeticID, cosmeticValue in parsedCosmetics.items():
                        if parsedValues['level'][level]['nodes'][nodeID]['reward'][0]['id'] == cosmeticID:
                            iconPath = cosmeticValue['IconFilePathList']
                else:
                    iconPath = ''
                playerRole = Format.PrettyRole(parsedArchiveNode[0]['Rows'][nodeKey]['PlayerRole'])
            if parsedValues['level'][level]['nodes'][nodeID]['clientInfoId'] == 'End':
                nodeName = 'Epilogue'
                iconPath = 'images/Archives/StartEndNode.png'
                playerRole = Format.PrettyRole(parsedArchiveNode[0]['Rows'][nodeKey]['PlayerRole'])
            if parsedValues['level'][level]['nodes'][nodeID]['clientInfoId'] == 'Start':
                nodeName = 'Prologue'
                iconPath = 'images/Archives/StartEndNode.png'
                playerRole = Format.PrettyRole(parsedArchiveNode[0]['Rows'][nodeKey]['PlayerRole'])
            if (str(nodeKey).lower() == str(parsedValues['level'][level]['nodes'][nodeID]['clientInfoId']).lower() and parsedValues['level'][level]['nodes'][nodeID]['clientInfoId'] != 'reward'):
                nodeName = parsedArchiveNode[0]['Rows'][nodeKey]['DisplayName']['SourceString']
                iconPath = parsedArchiveNode[0]['Rows'][nodeKey]['IconPath']
                playerRole = Format.PrettyRole(parsedArchiveNode[0]['Rows'][nodeKey]['PlayerRole'])

        if objectiveID != 'ignore':
            for objectiveKey in parsedQuestObjective[0]['Rows']:
                if parsedValues['level'][level]['nodes'][nodeID]['clientInfoId'] == 'reward':
                    objectiveDescription = ''
                if str(objectiveKey).lower() == str(objectiveID).lower() and parsedValues['level'][level]['nodes'][nodeID]['clientInfoId'] != 'reward':
                    description = parsedQuestObjective[0]['Rows'][objectiveKey]['Description']['SourceString']
                    try:
                        rulesDescription = parsedQuestObjective[0]['Rows'][objectiveKey]['RulesDescription']['SourceString']
                    except:
                        rulesDescription = None
                    if objectiveKey == 'RedGlyph':
                        description = str(description).replace('_GFX::CQGRIcon', '<img src="images/Archives/Glyphs/ChallengeIcon_redGlyph.png" style="vertical-align:middle;" height="25px" width="25px">')
                    elif objectiveKey == 'WhiteGlyph':
                        description = str(description).replace('_GFX::CQGIBIcon', '<img src="images/Archives/Glyphs/ChallengeIcon_whiteGlyph.png" style="vertical-align:middle;" height="25px" width="25px">')
                    elif objectiveKey == 'BlueGlyph' or objectiveKey == 'BlueGlyphEscape':
                        description = str(description).replace('_GFX::CQGBIcon', '<img src="images/Archives/Glyphs/ChallengeIcon_blueGlyph.png" style="vertical-align:middle;" height="25px" width="25px">')
                    elif objectiveKey == 'PurpleGlyph':
                        description = str(description).replace('_GFX::CQGPIcon', '<img src="images/Archives/Glyphs/ChallengeIcon_purpleGlyph.png" style="vertical-align:middle;" height="25px" width="25px">')
                    elif objectiveKey == 'YellowGlyph':
                        description = str(description).replace('_GFX::CQGYIcon', '<img src="images/Archives/Glyphs/ChallengeIcon_yellowGlyph.png" style="vertical-align:middle;" height="25px" width="25px">')
                    elif objectiveKey == 'GreenGlyph':
                        description = str(description).replace('_GFX::CQGGIcon', '<img src="images/Archives/Glyphs/ChallengeIcon_greenGlyph.png" style="vertical-align:middle;" height="25px" width="25px">')

                    objectiveParams = parsedQuestObjective[0]['Rows'][objectiveKey]['DescriptionParameters']
                    for i in range(len(objectiveParams)):
                        try:
                            if objectiveParams[i] == 'maxProgression' and not objectiveID == 'HarvestHalloweenPlant':
                                paramValueRaw = parsedValues['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['neededProgression']
                                try:
                                    if parsedQuestObjective[0]['Rows'][objectiveID]['IsProgressionPercentage'] == True:
                                        paramValue = int(paramValueRaw / 100)
                                        objectiveParams[i] = paramValue
                                    else:
                                        paramValue = paramValueRaw
                                except:
                                    paramValue = paramValueRaw
                                objectiveParams[i] = paramValue
                            if objectiveID == 'HarvestHalloweenPlant':
                                paramValue = parsedValues['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['neededProgression']
                                objectiveParams[i] = paramValue
                            if objectiveParams[i] == 'perk' or objectiveParams[i] == 'exclusivePerk':
                                for z in range(len(parsedValues['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['conditions'])):
                                    if (parsedValues['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['conditions'][z]['key'] == 'perk' or parsedValues['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['conditions'][z]['key'] == 'exclusivePerk'):
                                        perkID = parsedValues['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['conditions'][z]['value'][0]
                                        for perks in parsedPerks:
                                            if perkID == perks:
                                                paramValue = parsedPerks[perkID]['Name']
                                objectiveParams[i] = paramValue
                            if objectiveParams[i] == 'character':
                                for z in range(len(parsedValues['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['conditions'])):
                                    if parsedValues['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['conditions'][z]['key'] == 'character':
                                        characterID = parsedValues['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['conditions'][z]['value'][0]
                                        for x in range(len(parsedCharactersID)):
                                            if characterID == parsedCharactersID[x]['id']:
                                                characterInt = parsedCharactersID[x]['metaData']['character']
                                                paramValue = parsedCharacters[characterInt]['Name']
                                objectiveParams[i] = paramValue
                            for z in range(len(parsedValues['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['questEvent'])):
                                if str(objectiveParams[i]).lower() == str(parsedValues['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['questEvent'][z]['questEventId']).lower():
                                    paramValue = parsedValues['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['questEvent'][z]['repetition']
                                    objectiveParams[i] = paramValue
                                else:
                                    pass
                        except:
                            print('Failed')
                        objectiveDescription = description.format(*objectiveParams)
        else:
            for objectiveKey in parsedQuestObjective[0]['Rows']:
                if parsedValues['level'][level]['nodes'][nodeID]['clientInfoId'] == 'reward':
                    objectiveDescription = ''
                    rulesDescription = None
                if parsedValues['level'][level]['nodes'][nodeID]['clientInfoId'] == 'End':
                    objectiveDescription = parsedArchiveNode[0]['Rows']['End']['Description']['SourceString']
                    rulesDescription = None
                if parsedValues['level'][level]['nodes'][nodeID]['clientInfoId'] == 'Start':
                    objectiveDescription = parsedArchiveNode[0]['Rows']['Start']['Description']['SourceString']
                    rulesDescription = None



        return [nodeName, iconPath, objectiveDescription, playerRole, rulesDescription]

    def TomeNodes(parsedTome, level):
        ParsedNodes = {}

        for key, value in parsedTome.items():
            for nodeID in value['level'][level]['nodes']:
                try:
                    for objectiveID, objectiveValue in value['level'][level]['nodes'][nodeID]['objectives'].items():
                        try:
                            if value['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['isCommunityObjective'] == False:
                                nodeData = TomesDB.TomeNodesData(value, nodeID, objectiveID, level)
                                communityProgression = ''
                                communityBoolean = False
                            if value['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['isCommunityObjective'] == True:
                                communityProgression = value['level'][level]['nodes'][nodeID]['objectives'][objectiveID]['neededProgression']
                                communityBoolean = True
                        except:
                            try:
                                nodeData = TomesDB.TomeNodesData(value, nodeID, objectiveID, level)
                                communityProgression = ''
                                communityBoolean = False
                            except:
                                print('"ObjectiveID": ' + objectiveID + ' "NodeId": ' + nodeID + '\n')

                        try:
                            journal = value['level'][level]['nodes'][nodeID]['journal']
                        except:
                            journal = None
                        
                        ParsedNodes[nodeID] = {
                            "QuestID": objectiveID,
                            "Coordinates": value['level'][level]['nodes'][nodeID]['coordinates'],
                            "Neighbors": value['level'][level]['nodes'][nodeID]['neighbors'],
                            "Journals": journal,
                            "IsCommunityChallenge": communityBoolean,
                            "CommunityProgression": communityProgression,
                            "Name": nodeData[0],
                            "Description": nodeData[2],
                            "RulesDescription": nodeData[4],
                            "PlayerRole": nodeData[3],
                            "IconPath": 'images/' + nodeData[1],
                            "Reward": value['level'][level]['nodes'][nodeID]['reward']
                        }
                except:
                    try:
                        nodeData = TomesDB.TomeNodesData(value, nodeID, 'ignore', level)
                        communityProgression = ''
                        communityBoolean = False
                    except:
                        print("Except: " + nodeID + '\n')

                    try:
                        journal = value['level'][level]['nodes'][nodeID]['journal']
                    except:
                        journal = None


                    if value['level'][level]['nodes'][nodeID]['clientInfoId'] == 'End':
                        reward = value['level'][level]['endNodeRewards']
                    elif value['level'][level]['nodes'][nodeID]['clientInfoId'] == 'reward':
                        reward = value['level'][level]['nodes'][nodeID]['reward']
                    else:
                        reward = None
                    
                    ParsedNodes[nodeID] = {
                        "QuestID": value['level'][level]['nodes'][nodeID]['clientInfoId'],
                        "Coordinates": value['level'][level]['nodes'][nodeID]['coordinates'],
                        "Neighbors": value['level'][level]['nodes'][nodeID]['neighbors'],
                        "Journals": journal,
                        "Name": nodeData[0],
                        "Description": nodeData[2],
                        "RulesDescription": nodeData[4],
                        "PlayerRole": nodeData[3],
                        "IconPath": nodeData[1],
                        "Reward": reward
                    }


        return ParsedNodes

    def LevelArray(parsedTome, key):
        with open('output\Cosmetics.json', 'r') as cosmeticsJson:
            parsedCosmetics = json.load(cosmeticsJson)

        levelsArray = []
        for i in range(len(parsedTome[key]['level'])):
            nodes = TomesDB.TomeNodes(parsedTome, i)
            level = {}
            level['Nodes'] = nodes
            level['StartDate'] = parsedTome[key]['level'][i]['startDate']
            level['StartNodes'] = parsedTome[key]['level'][i]['start']
            level['EndNodes'] = parsedTome[key]['level'][i]['end']
            if parsedTome[key]['level'][i]['endNodeRewards'][1]['type'] == 'inventory':
                for cosmeticID, cosmeticValue in parsedCosmetics.items():
                    if parsedTome[key]['level'][i]['endNodeRewards'][1]['id'] == cosmeticID:
                        iconPath = cosmeticValue['IconFilePathList']
            level['EndNodeReward'] = iconPath

            levelsArray.append(level)

        return levelsArray

    def TomesDB(json1):
        if json1[0]['Name'] == 'ArchiveDB':
            ParsedArchives = {}
            
            for key, value in json1[0]['Rows'].items():
                with open('components\\Tomes\\' + key +'.json', 'r') as tome:
                    parsedTome = json.load(tome)

                try:
                    popupMessage = value['PurchasePassPopupMessage']['SourceString']
                except:
                    popupMessage = None
                
                levelsArray = TomesDB.LevelArray(parsedTome, key)
                    
                ParsedArchives[key] = {
                                        "Name": value['Title']['SourceString'],
                                        "Description": popupMessage,
                                        "Levels": levelsArray,
                                        "RiftID": parsedTome[key]['riftId'],
                                        "Version": parsedTome[key]['version']
                                    }

        return ParsedArchives