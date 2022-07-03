# Lib imports
import json

# Local imports
from utils.format import Format

class CosmeticsDB:
    # Some Cosmetic Pieces
    def DefaultItemCosmeticsDB(json1):
        ParsedStore = {}

        if json1[0]['Name'] == 'CustomizationItemDB':

            for key, value in json1[0]['Rows'].items():

                itemRarity = Format.PrettyRarity(value['Rarity'])
                type = Format.PrettyCategory(value['Category'])
                if key == 'NK_Torso01_Mods':
                    pass
                else:
                    ParsedStore[key] = { 
                                            "CosmeticId": key,
                                            "CosmeticName": value['UIData']['DisplayName']['SourceString'],
                                            "Description": Format.ParseCosmeticsDescription(value),
                                            "IconFilePathList": 'images/' + value['UIData']['IconFilePathList'][0],
                                            "CollectionName": Format.ParseCollectionName(value),
                                            "Type": type,
                                            "Character": value['AssociatedCharacter'],
                                            "Purchasable": False,
                                            "Rarity": itemRarity,
                                            "Prices": []
                                        }

        return ParsedStore


    # Create Cosmetics
    def CosmeticsDB(json1):
        ParsedStore = {}

        if json1[0]['Name'] == 'CustomizationItemDB':

            with open("components\catalog.json", 'r') as catalog:
                parsedCatalog = json.load(catalog)

            for key, value in json1[0]['Rows'].items():

                for outKey in parsedCatalog:

                    if key == outKey['id']:
                        appendPrice = []
                        purchasable = outKey['purchasable']
                        type = outKey['metaData']['type']
                        startDate = outKey['metaData']['newStartDate']
                        endDate = outKey['metaData']['newEndDate']

                        if outKey['defaultCost'] == []:
                            Cells = None
                            Shards = None
                        else:
                            for price in outKey['defaultCost']:

                                try:
                                    if price['currencyId'] == 'Cells':
                                        Cells = price['price']
                                    else:
                                        Cells = None
                                except:
                                    pass

                                try:
                                    if price['currencyId'] == 'Shards':
                                        Shards = price['price']
                                    else:
                                        Shards = None
                                except:
                                    pass

                                if Cells == None:
                                    pass
                                else:
                                    priceCells = {
                                        "Cells": Cells
                                    }

                                    appendPrice.append(priceCells)
                                if Shards == None:
                                    pass
                                else:
                                    priceShards = {
                                        "Shards": Shards
                                    }

                                    appendPrice.append(priceShards)

                itemRarity = Format.PrettyRarity(value['Rarity'])
                if key == 'NK_Torso01_Mods':
                    pass
                else:
                    ParsedStore[key] = { 
                                            "CosmeticId": key,
                                            "CosmeticName": value['UIData']['DisplayName']['SourceString'],
                                            "Description": Format.ParseCosmeticsDescription(value),
                                            "IconFilePathList": 'images/' + value['UIData']['IconFilePathList'][0],
                                            "CollectionName": Format.ParseCollectionName(value),
                                            "Type": type,
                                            "Character": value['AssociatedCharacter'],
                                            "Purchasable": purchasable,
                                            "EndDate": endDate,
                                            "StartDate": startDate,
                                            "Rarity": itemRarity,
                                            "Prices": appendPrice
                                        }
                                    
        elif json1[0]['Name'] == 'OutfitDB':

            with open("components\getOutfits.json", 'r') as outfits:
                parsedOutfits = json.load(outfits)

            with open("components\CharactersID.json", 'r') as CharactersID:
                parsedCharIDs = json.load(CharactersID)

            with open("components\catalog.json", 'r') as catalog:
                parsedCatalog = json.load(catalog)

            for key, value in json1[0]['Rows'].items():

                for catalogKey in parsedCatalog:

                    if str(key).lower() == str(catalogKey['id']).lower():
                        type = catalogKey['categories']
                        prettyType = Format.PrettyPerkTag(type)

                        isLinked = catalogKey['metaData']['unbreakable']

                        startDate = catalogKey['metaData']['newStartDate']
                        endDate = catalogKey['metaData']['newEndDate']

                        purchasable = catalogKey['purchasable']

                    try: 
                        if str(key).lower() == str(catalogKey['metaData']['outfitId']).lower():
                            rarity = catalogKey['metaData']['rarity']
                    except:
                        pass
                
                for outKey in parsedOutfits['outfits']:
                    
                    if str(outKey['id']).lower() == str(key).lower():
                        associatedCharacter = outKey['character']

                        for outKeyCharacters in parsedCharIDs:
                            if outKeyCharacters['id'] == associatedCharacter:
                                stringCharacterID = outKeyCharacters['metaData']['character']
                                characterToID = int(stringCharacterID)

                    if str(outKey['id']).lower() == str(key).lower():
                        appendPrice = []

                        if outKey['defaultCost'] == []:
                            Cells = None
                            Shards = None

                        else:
                            for price in outKey['defaultCost']:

                                try:
                                    if price['currencyId'] == 'Cells':
                                        Cells = price['price']
                                    else:
                                        Cells = None
                                except:
                                    pass

                                try:
                                    if price['currencyId'] == 'Shards':
                                        Shards = price['price']
                                    else:
                                        Shards = None
                                except:
                                    pass

                                if Cells == None:
                                    pass
                                else:
                                    priceCells = {
                                        "Cells": Cells
                                    }

                                    appendPrice.append(priceCells)
                                if Shards == None:
                                    pass
                                else:
                                    priceShards = {
                                        "Shards": Shards
                                    }

                                    appendPrice.append(priceShards)

                if key == 'K24_outfit_01':
                    pass
                else:
                    ParsedStore[key] = { 
                                            "CosmeticId": key,
                                            "CosmeticName": value['UIData']['DisplayName']['SourceString'],
                                            "Description": Format.ParseCosmeticsDescription(value),
                                            "IconFilePathList": 'images/' + value['UIData']['IconFilePathList'][0],
                                            "CollectionName": value['CollectionName']['SourceString'],
                                            "Type": prettyType,
                                            "Character": characterToID,
                                            "Unbreakable": isLinked,
                                            "Purchasable": purchasable,
                                            "EndDate": endDate,
                                            "StartDate": startDate,
                                            "Rarity": rarity,
                                            "OutfitItems": value['OutfitItems'],
                                            "Prices": appendPrice
                                        }

        elif json1[0]['Name'] == 'Append':

            for key, value in json1[0]['Rows'].items():

                ParsedStore[key] = {        
                                            "Type": "Currency",
                                            "CosmeticId": value['CosmeticId'],
                                            "CosmeticName": value['CosmeticName'],
                                            "Description": "",
                                            "IconFilePathList": value['IconFilePathList'],
                                        }

        return ParsedStore