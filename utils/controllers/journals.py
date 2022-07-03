# Lib imports
import json

class JournalsDB:
    # Create Journals
    def Entries(object, tomeID):
        with open('components\journalsAudio.json', 'r') as audioJson:
            parsedAudio = json.load(audioJson)

        SecondObjectArray = []

        for i in range(len(object['Entries'])):
            try:
                if parsedAudio[tomeID][object['VignetteId']]:
                    audioPath = parsedAudio[tomeID][object['VignetteId']][i]
            except:
                audioPath = None
            secondObj = {
                "Title": object['Entries'][i]['Title']['SourceString'],
                "Text": object['Entries'][i]['Text']['SourceString'],
                "AudioPath": audioPath
            }
            SecondObjectArray.append(secondObj)


        return SecondObjectArray

    def ArchiveJournalDB(json1):
        if json1[0]['Name'] == 'ArchiveJournalDB':
            with open('output\Tomes.json', 'r') as tomesJson:
                parsedTomes = json.load(tomesJson)

            ParsedJournals = {}
            ObjectArray = []
            ObjectArrayEvent = []

            for key, value in json1[0]['Rows'].items():
                tomeName = parsedTomes[key]['Name']

                if key == 'Halloween2021' or key == 'Anniversary2022':
                    for object in value['Vignettes']:
                        entriesArray = JournalsDB.Entries(object, key)
                        obj = {
                            "VignetteId": object['VignetteId'],
                            "Name": object['Title']['SourceString'],
                            "SubTitle": object['Subtitle']['SourceString'],
                            "Entries": entriesArray
                        }
                        ObjectArrayEvent.append(obj)

                    ObjectArray = ObjectArrayEvent
                else:
                    for object in value['Vignettes']:
                        entriesArray = JournalsDB.Entries(object, key)
                        obj = {
                            "VignetteId": object['VignetteId'],
                            "Name": object['Title']['SourceString'],
                            "SubTitle": object['Subtitle']['SourceString'],
                            "Entries": entriesArray
                        }
                        ObjectArray.append(obj)

                ParsedJournals[key] = {
                                        "TomeName": tomeName,
                                        "Vignettes": ObjectArray
                                    }
        return ParsedJournals