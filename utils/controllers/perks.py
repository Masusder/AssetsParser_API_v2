# Lib imports
from collections import OrderedDict

# Local imports
from utils.format import Format

class PerksDB:
    # Create Perks
    def PerksDB(json):
        if json[0]['Name'] == 'PerkDB':
            ParsedPerks = {}

            for key, value in json[0]['Rows'].items():
                tag = Format.PrettyPerkTag(value['Tags'])
                role = Format.PrettyAbility(value['Role'])
                tunablesArray = []
                for i in value['PerkLevelTunables']:
                    perkLevelTunables = i['Tunables']
                    tunablesArray.append(perkLevelTunables)

                finalArray = []
                tunablesArray1 = []
                tunablesArray2 = []
                tunablesArray3 = []
                tunablesArray4 = []
                try:
                    tunablesArray1.append(tunablesArray[0][0])

                    tunablesArray2.append(tunablesArray[0][1])

                    tunablesArray3.append(tunablesArray[0][2])

                    tunablesArray4.append(tunablesArray[0][3])

                except:
                    pass

                try:
                    tunablesArray1.append(tunablesArray[1][0])

                    tunablesArray2.append(tunablesArray[1][1])

                    tunablesArray3.append(tunablesArray[1][2])

                    tunablesArray4.append(tunablesArray[1][3])
                except:
                    pass

                try:
                    tunablesArray1.append(tunablesArray[2][0])

                    tunablesArray2.append(tunablesArray[2][1])

                    tunablesArray3.append(tunablesArray[2][2])

                    tunablesArray4.append(tunablesArray[2][3])
                except:
                    pass

                try:
                    tunablesArray1.append(tunablesArray[3][0])

                    tunablesArray2.append(tunablesArray[3][1])

                    tunablesArray3.append(tunablesArray[3][2])

                    tunablesArray4.append(tunablesArray[3][3])
                except:
                    pass
                
                arrayFormated1 = list(OrderedDict.fromkeys(tunablesArray1))
                arrayFormated2 = list(OrderedDict.fromkeys(tunablesArray2))
                arrayFormated3 = list(OrderedDict.fromkeys(tunablesArray3))
                arrayFormated4 = list(OrderedDict.fromkeys(tunablesArray4))
                
                ignoreMe = []

                finalArray.append(arrayFormated1)
                if not ignoreMe == arrayFormated2:
                    finalArray.append(arrayFormated2)
                if not ignoreMe == arrayFormated3:
                    finalArray.append(arrayFormated3)
                if not ignoreMe == arrayFormated4:
                    finalArray.append(arrayFormated4)

                category = []
                if not category:
                    for i in range(len(value['PerkCategory'])):
                        category = Format.PrettyCategory(value['PerkCategory'][i])

                ParsedPerks[key] = { 
                                        "Categories": category,
                                        "Character": value['AssociatedPlayerIndex'],
                                        "Tag": tag,
                                        "Role": role,
                                        "Name": value['UIData']['DisplayName']['SourceString'],
                                        "Description": Format.ParsePerksDescription(value),
                                        "Tunables": finalArray,
                                        "IconFilePathList": 'images/' + value['UIData']['IconFilePathList'][0],
                                        "TeachableLevel": value['TeachableOnBloodweblevel']
                                    }

        return ParsedPerks