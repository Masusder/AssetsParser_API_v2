class MapsDB:
    # Create Maps
    def ProceduralMapsDB(json):
        if json[0]['Name'] == 'ProceduralMaps':
            ParsedMaps = {}

            for key, value in json[0]['Rows'].items():
                ParsedMaps[key] = {
                                        "Realm": value['ThemeName']['SourceString'],
                                        "MapId": value['MapId'],
                                        "Name": value['Name']['SourceString'],
                                        "Description": value['Description']['SourceString'],
                                        "HookMinDistance": value['HookMinDistance'],
                                        "HookMinCount": value['HookMinCount'],
                                        "HookMaxCount": value['HookMaxCount'],
                                        "PalletsMinDistance": value['BookShelvesMinDistance'],
                                        "PalletsMinCount": value['BookShelvesMinCount'],
                                        "PalletsMaxCount": value['BookShelvesMaxCount'],
                                        "DLC": value['DlcIDString'],
                                        "Thumbnail": 'images/' + value['ThumbnailPath']
                                    }

        return ParsedMaps