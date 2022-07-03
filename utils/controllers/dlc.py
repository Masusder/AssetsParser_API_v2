# Local imports
from utils.format import Format

class DlcDB:
    # Create DLC
    def DlcDB(json):
        if json[0]['Name'] == 'DlcDB':
            ParsedDLC = {}

            for key, value in json[0]['Rows'].items():
                ParsedDLC[key] = {
                                        "Name": value['Description'],
                                        "Description": Format.ParseDLCDescription(value),
                                        "SteamId": value['DlcIdSteam'],
                                        "EpicId": value['DlcIdEpic'],
                                        "DMMId": value['DlcIdDmm'],
                                        "PS4Id": value['DlcIdPS4'],
                                        "Xbox1Id": value['DlcIdXB1'],
                                        "XboxSeriesXId": value['DlcIdXSX'],
                                        "SwitchId": value['DlcIdSwitch'],
                                        "WindowsStoreId": value['DlcIdGRDK'],
                                        "PS5Id": value['DlcIdPS5'],
                                        "StadiaId": value['DlcIdStadia'],
                                        "SortOrder": value['UISortOrder']
                                    }

        return ParsedDLC