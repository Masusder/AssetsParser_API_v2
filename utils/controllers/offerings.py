# Local imports
from utils.format import Format

class OfferingsDB:
    # Create Offerings
    def OfferingDB(json):
        if json[0]['Name'] == 'OfferingDB':
            ParsedOfferings = {}

            for key, value in json[0]['Rows'].items():
                type = Format.PrettyOfferingType(value['OfferingType'])
                rarity = Format.PrettyRarity(value['Rarity'])
                role = Format.PrettyRole(value['Role'])
                available = Format.PrettyAvailable(value['Availability']['itemAvailability'])
                ParsedOfferings[key] = {
                                        "Type": type,
                                        "Tags": value['Tags'],
                                        "Available": available,
                                        "Name": value['UIData']['DisplayName']['SourceString'],
                                        "Description": value['UIData']['Description']['SourceString'],
                                        "Role": role,
                                        "Rarity": rarity,
                                        "Image": 'images/' + value['UIData']['IconFilePathList'][0]
                                    }

        return ParsedOfferings