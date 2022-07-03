# Local imports
from utils.format import Format

class CharactersDB:
    # Create Characters
    def CharactersDB(json):
        if json[0]['Name'] == 'CharacterDescriptionDB':
            ParsedCharacters = {}

            for key, value in json[0]['Rows'].items():
                role = Format.PrettyRole(value['Role'])
                difficulty = Format.PrettyDifficulty(value['Difficulty'])
                gender = Format.PrettyGender(value['Gender'])
                if key == '-1':
                    pass
                else:
                    ParsedCharacters[key] = { 
                                            "ID": value['IdName'],
                                            "Name": value['DisplayName']['SourceString'],
                                            "Role": role,
                                            "Gender": gender,
                                            "ParentItem": value['DefaultItem'],
                                            "DLC": value['ChapterDlcId'],
                                            "Difficulty": difficulty,
                                            "BackStory": value['BackStory']['SourceString'],
                                            "Biography": value['Biography']['SourceString'],
                                            "IconFilePath": 'images/' + value['IconFilePath'],
                                            "BackgroundImagePath": 'images/' + value['BackgroundImagePath']
                                        }

        return ParsedCharacters