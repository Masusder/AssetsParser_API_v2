# Lib imports
import glob
import json
import sys
from jsonmerge import merge
from colorama import Fore
from utils.controllers.dlc import DlcDB

# Local imports
from utils.ui import UI, Style

# Controllers
from utils.controllers.cosmetics import CosmeticsDB
from utils.controllers.perks import PerksDB
from utils.controllers.characters import CharactersDB
from utils.controllers.journals import JournalsDB
from utils.controllers.maps import MapsDB
from utils.controllers.addons import AddonsDB
from utils.controllers.offerings import OfferingsDB
from utils.controllers.tomes import TomesDB
from utils.controllers.rifts import RiftsDB
from utils.controllers.items import ItemsDB

def main():
    UI.start()
    while(True):
        choice = UI.menu(
            "Choose an option:", [
                ("0", "Create Everything"),
                ("1", "Create Cosmetics"),
                ("2", "Create Perks"),
                ("3", "Create Characters"),
                ("4", "Create Journals"),
                ("5", "Create Maps"),
                ("6", "Create DLC"),
                ("7", "Create Addons"),
                ("8", "Create Offerings"),
                ("9", "Create Tomes"),
                ("10", "Create Rifts"),
                ("11", "Create Items"),
                ("12", "Exit")
            ]
        )
    
        # Cosmetics
        if choice == 1 or choice == 0:
            cosmetics = {}
            cosmetics_list = []
            cosmetics_list.extend(glob.glob("DeadByDaylight\Content\Data\Store\*\*\OutfitDB.json"))
            cosmetics_list.extend(glob.glob('DeadByDaylight\Content\Data\OutfitDB.json'))
            cosmetics_list.extend(glob.glob("DeadByDaylight\Content\Data\Store\*\*\CustomizationItemDB.json"))
            cosmetics_list.extend(glob.glob("components\currencies.json"))

            item_list = []
            item_list.extend(glob.glob("DeadByDaylight\Content\Data\Dlc\*\CustomizationItemDB.json"))
            item_list.extend(glob.glob("DeadByDaylight\Content\Data\Dlc\*\Charms\CustomizationItemDB.json"))
            item_list.extend(glob.glob("DeadByDaylight\Content\Data\Dlc\*\Charms\Secret\CustomizationItemDB.json"))
            item_list.extend(glob.glob('DeadByDaylight\Content\Data\CustomizationItemDB.json'))

            for file in cosmetics_list:
                print(Fore.LIGHTGREEN_EX + file + Fore.WHITE)
                try:
                    with open(file, 'r', encoding='utf-8') as file:
                        json_ = json.load(file)
                        parsed = CosmeticsDB.CosmeticsDB(json_)
                    cosmetics = merge(cosmetics, parsed)
                except Exception as e:
                    print(Fore.RED + e + Fore.WHITE)

            for file2 in item_list:
                print(Fore.LIGHTGREEN_EX + file2 + Fore.WHITE)
                try:
                    with open(file2, 'r', encoding='utf-8') as file2:
                        json_ = json.load(file2)
                        parsed2 = CosmeticsDB.DefaultItemCosmeticsDB(json_)
                    cosmetics = merge(cosmetics, parsed2)
                except Exception as f:
                    print(Fore.RED + f + Fore.WHITE)
            print()
            print(Style.BOLD + 'Total len of all items is', len(cosmetics.items()))
            print('-----------------------------------------------' + Style.END)
            with open("output\Cosmetics.json", "w+") as text_file:
                text_file.write(json.dumps(cosmetics, indent=4))
        
        # Perks
        if choice == 2 or choice == 0:
            perks = {}
            perks_list = []
            perks_list.extend(glob.glob("DeadByDaylight\Content\Data\PerkDB.json"))
            perks_list.extend(glob.glob("DeadByDaylight\Content\Data\Dlc\*\PerkDB.json"))

            for file in perks_list:
                print(Fore.LIGHTGREEN_EX + file + Fore.WHITE)
                try:
                    with open(file, 'r', encoding='utf-8') as file:
                        json_ = json.load(file)
                        parsed = PerksDB.PerksDB(json_)
                    perks = merge(perks, parsed)
                except Exception as e :
                    print(Fore.RED + e + Fore.WHITE)
            print()
            print(Style.BOLD + 'Total len of all items is', len(perks.items()))
            print('-----------------------------------------------' + Style.END)
            with open("output\Perks.json", "w+") as text_file:
                text_file.write(json.dumps(perks, indent=4))

        # Characters
        if choice == 3 or choice == 0:
            characters = {}
            characters_list = []
            characters_list.extend(glob.glob("DeadByDaylight\Content\Data\CharacterDescriptionDB.json"))
            characters_list.extend(glob.glob("DeadByDaylight\Content\Data\Dlc\*\CharacterDescriptionDB.json"))

            for file in characters_list:
                print(Fore.LIGHTGREEN_EX + file + Fore.WHITE)
                try:
                    with open(file, 'r', encoding='utf-8') as file:
                        json_ = json.load(file)
                        parsed = CharactersDB.CharactersDB(json_)
                    characters = merge(characters, parsed)
                except Exception as e :
                    print(Fore.RED + e + Fore.WHITE)
            print()
            print(Style.BOLD + 'Total len of all items is', len(characters.items()))
            print('-----------------------------------------------' + Style.END)
            with open("output\Characters.json", "w+") as text_file:
                text_file.write(json.dumps(characters, indent=4))

        # Archive Journals
        if choice == 4 or choice == 0:
            journals = {}
            journals_list = []
            journals_list.extend(glob.glob("DeadByDaylight\Content\Data\Archives\*\ArchiveJournalDB.json"))

            for file in journals_list:
                print(Fore.LIGHTGREEN_EX + file + Fore.WHITE)
                try:
                    with open(file, 'r', encoding='utf-8') as file:
                        json_ = json.load(file)
                        parsed = JournalsDB.ArchiveJournalDB(json_)
                    journals = merge(journals, parsed)
                except Exception as e :
                    print(Fore.RED + e + Fore.WHITE)
            print()
            print(Style.BOLD + 'Total len of all items is', len(journals.items()))
            print('-----------------------------------------------' + Style.END)
            with open("output\Journals.json", "w+") as text_file:
                text_file.write(json.dumps(journals, indent=4))

        # Maps
        if choice == 5 or choice == 0:
            maps = {}
            maps_list = []
            maps_list.extend(glob.glob("DeadByDaylight\Content\Data\ProceduralMaps.json"))

            for file in maps_list:
                print(Fore.LIGHTGREEN_EX + file + Fore.WHITE)
                try:
                    with open(file, 'r', encoding='utf-8') as file:
                        json_ = json.load(file)
                        parsed = MapsDB.ProceduralMapsDB(json_)
                    maps = merge(maps, parsed)
                except Exception as e :
                    print(Fore.RED + e + Fore.WHITE)
            print()
            print(Style.BOLD + 'Total len of all items is', len(maps.items()))
            print('-----------------------------------------------' + Style.END)
            with open("output\Maps.json", "w+") as text_file:
                text_file.write(json.dumps(maps, indent=4))

        # DLC
        if choice == 6 or choice == 0:
            dlc = {}
            dlc_list = []
            dlc_list.extend(glob.glob("DeadByDaylight\Content\Data\DlcDB.json"))
            dlc_list.extend(glob.glob("DeadByDaylight\Content\Data\*\*\DlcDB.json"))

            for file in dlc_list:
                print(Fore.LIGHTGREEN_EX + file + Fore.WHITE)
                try:
                    with open(file, 'r', encoding='utf-8') as file:
                        json_ = json.load(file)
                        parsed = DlcDB.DlcDB(json_)
                    dlc = merge(dlc, parsed)
                except Exception as e :
                    print(Fore.RED + e + Fore.WHITE)
            print()
            print(Style.BOLD + 'Total len of all items is', len(dlc.items()))
            print('-----------------------------------------------' + Style.END)
            with open("output\DLC.json", "w+") as text_file:
                text_file.write(json.dumps(dlc, indent=4))

        # Addons
        if choice == 7 or choice == 0:
            addons = {}
            addons_list = []
            addons_list.extend(glob.glob("DeadByDaylight\Content\Data\ItemAddonDB.json"))
            addons_list.extend(glob.glob("DeadByDaylight\Content\Data\*\*\ItemAddonDB.json"))

            for file in addons_list:
                print(Fore.LIGHTGREEN_EX + file + Fore.WHITE)
                try:
                    with open(file, 'r', encoding='utf-8') as file:
                        json_ = json.load(file)
                        parsed = AddonsDB.ItemAddonsDB(json_)
                    addons = merge(addons, parsed)
                except Exception as e :
                    print(Fore.RED + e + Fore.WHITE)
            print()
            print(Style.BOLD + 'Total len of all items is', len(addons.items()))
            print('-----------------------------------------------' + Style.END)
            with open("output\Addons.json", "w+") as text_file:
                text_file.write(json.dumps(addons, indent=4))

        # Offerings
        if choice == 8 or choice == 0:
            offerings = {}
            offerings_list = []
            offerings_list.extend(glob.glob("DeadByDaylight\Content\Data\OfferingDB.json"))
            offerings_list.extend(glob.glob("DeadByDaylight\Content\Data\*\*\OfferingDB.json"))

            for file in offerings_list:
                print(Fore.LIGHTGREEN_EX + file + Fore.WHITE)
                try:
                    with open(file, 'r', encoding='utf-8') as file:
                        json_ = json.load(file)
                        parsed = OfferingsDB.OfferingDB(json_)
                    offerings = merge(offerings, parsed)
                except Exception as e :
                    print(Fore.RED + e + Fore.WHITE)
            print()
            print(Style.BOLD + 'Total len of all items is', len(offerings.items()))
            print('-----------------------------------------------' + Style.END)
            with open("output\Offerings.json", "w+") as text_file:
                text_file.write(json.dumps(offerings, indent=4))

        # Tomes
        if choice == 9 or choice == 0:
            tomes = {}
            tomes_list = []
            tomes_list.extend(glob.glob("DeadByDaylight\Content\Data\Archives\*\ArchiveDB.json"))

            for file in tomes_list:
                print(Fore.LIGHTGREEN_EX + file + Fore.WHITE)
                try:
                    with open(file, 'r', encoding='utf-8') as file:
                        json_ = json.load(file)
                        parsed = TomesDB.TomesDB(json_)
                    tomes = merge(tomes, parsed)
                except Exception as e :
                    print(Fore.RED + e + Fore.WHITE)
            print()
            print(Style.BOLD + 'Total len of all items is', len(tomes.items()))
            print('-----------------------------------------------' + Style.END)
            with open("output\Tomes.json", "w+") as text_file:
                text_file.write(json.dumps(tomes, indent=4))

        # Rifts
        if choice == 10 or choice == 0:
            rifts = {}
            rifts_list = []
            rifts_list.extend(glob.glob("DeadByDaylight\Content\Data\Archives\*\ArchiveDB.json"))

            for file in rifts_list:
                print(Fore.LIGHTGREEN_EX + file + Fore.WHITE)
                try:
                    with open(file, 'r', encoding='utf-8') as file:
                        json_ = json.load(file)
                        parsed = RiftsDB.RiftsDB(json_)
                    rifts = merge(rifts, parsed)
                except Exception as e :
                    print(Fore.RED + e + Fore.WHITE)
            print()
            print(Style.BOLD + 'Total len of all items is', len(rifts.items()))
            print('-----------------------------------------------' + Style.END)
            with open("output\Rifts.json", "w+") as text_file:
                text_file.write(json.dumps(rifts, indent=4))

        # Items
        if choice == 11 or choice == 0:
            items = {}
            items_list = []
            items_list.extend(glob.glob("DeadByDaylight\Content\Data\ItemDB.json"))
            items_list.extend(glob.glob("DeadByDaylight\Content\Data\*\*\ItemDB.json"))

            for file in items_list:
                print(Fore.LIGHTGREEN_EX + file + Fore.WHITE)
                try:
                    with open(file, 'r', encoding='utf-8') as file:
                        json_ = json.load(file)
                        parsed = ItemsDB.ItemsDB(json_)
                    items = merge(items, parsed)
                except Exception as e :
                    print(Fore.RED + e + Fore.WHITE)
            print()
            print(Style.BOLD + 'Total len of all items is', len(items.items()))
            print('-----------------------------------------------' + Style.END)
            with open("output\Items.json", "w+") as text_file:
                text_file.write(json.dumps(items, indent=4))
        
        if choice == 12:
            sys.exit()

if __name__ == "__main__":
    main()