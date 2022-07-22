# Lib imports
import json
from colorama import Fore
from jsonmerge import merge
from os import path

# Local imports
from utils.ui import Style

class Export:
    # Export function
    def Export(dataExport, dataList, function, fileName, returnData):
        for file in dataList:
            # Print file path
            print(Fore.LIGHTGREEN_EX + file + Fore.WHITE)
            # Create data
            try:
                with open(file, 'r', encoding='utf-8') as file:
                    json_ = json.load(file)
                    parsed = function(json_)
                dataExport = merge(dataExport, parsed)
            except Exception as e:
                print(e)
        
        outputPath = path.join('output', fileName)
        if returnData == True:
            # Optionally return data for further manipulation
            return dataExport
        elif returnData == False:
            # Print amount of rows
            print()
            print(Style.BOLD + 'Total len of all items is', len(dataExport.items()))
            print('-----------------------------------------------' + Style.END)
            # Create API output
            with open(outputPath, "w+") as text_file:
                text_file.write(json.dumps(dataExport, indent=4))