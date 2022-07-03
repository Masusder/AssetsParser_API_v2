# Local imports
from utils.format import Format

class ItemsDB:
    # Create Items
    def ItemsDB(json):
        if json[0]['Name'] == 'ItemDB':
            ParsedItems = {}

            for key, value in json[0]['Rows'].items():
                if (key == 'Item_Camper_OnryoTape' or key == 'Item_Blighted_Serum'):
                    pass
                else:
                    ability = Format.PrettyAbility(value['RequiredKillerAbility'])
                    type = Format.PrettyOfferingType(value['Type'])
                    rarity = Format.PrettyRarity(value['Rarity'])
                    role = Format.PrettyRole(value['Role'])
                    ParsedItems[key] = {
                                            "RequiredAbility": ability,
                                            "Role": role,
                                            "Rarity": rarity,
                                            "Type": type,
                                            "Name": value['UIData']['DisplayName']['SourceString'],
                                            "Description": value['UIData']['Description']['SourceString'],
                                            "IconFilePathList": value['UIData']['IconFilePathList'][0],
                                            "ID": value['ID']
                                        }

        return ParsedItems