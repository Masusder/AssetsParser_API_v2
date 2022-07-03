# Local imports
from utils.format import Format

class AddonsDB:
    # Create Addons
    def ItemAddonsDB(json):
        if json[0]['Name'] == 'ItemAddonDB':
            ParsedAddons = {}

            for key, value in json[0]['Rows'].items():
                type = Format.PrettyType(value['Type'])
                role = Format.PrettyRole(value['Role'])
                rarity = Format.PrettyRarity(value['Rarity'])
                ability = Format.PrettyAbility(value['RequiredKillerAbility'])
                ParsedAddons[key] = {
                                        "Type": type,
                                        "ParentItem": value['ParentItem']['ItemIDs'],
                                        "KillerAbility": ability,
                                        "Name": value['UIData']['DisplayName']['SourceString'],
                                        "Description": value['UIData']['Description']['SourceString'],
                                        "Role": role,
                                        "Rarity": rarity,
                                        "CanBeUsedAfterEvent": value['CanUseAfterEventEnd'],
                                        "Bloodweb": value['Bloodweb'],
                                        "Image": 'images/' + value['UIData']['IconFilePathList'][0]
                                    }

        return ParsedAddons