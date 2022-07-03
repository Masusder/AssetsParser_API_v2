# Lib imports
import json

class RiftsDB:
    # Create Rifts
    def RiftsDB(json1):
        if json1[0]['Name'] == 'ArchiveDB':
            with open('components/riftBanners.json', 'r') as banner:
                parsedBanners = json.load(banner)
            with open('components/archiveRewardData.json', 'r') as archiveRewardData:
                parsedRewardData = json.load(archiveRewardData)
            ParsedRifts = {}

            for key, value in json1[0]['Rows'].items():
                if key == 'Halloween2021' or key == 'Anniversary2022':
                    continue
                else:
                    with open('components\\Rifts\\Rift' + key +'.json', 'r') as rift:
                        parsedRift = json.load(rift)

                    ParsedRifts[key] = {
                                            "Name": value['Title']['SourceString'],
                                            "Banner": parsedBanners[key][0],
                                            "Requirement": parsedRift[key]['requirement'],
                                            "EndDate": parsedRewardData[key]['endDate'],
                                            "TierInfo": parsedRift[key]['tierInfo']
                                        }

        return ParsedRifts