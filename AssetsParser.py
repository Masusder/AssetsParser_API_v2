# Lib imports
import glob
import sys

# Local imports
from utils.ui import UI
from utils.export import Export

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
from utils.controllers.dlc import DlcDB

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

        emptyDataObject = {}
    
        # Cosmetics
        if choice == 1 or choice == 0:
            cosmetics_list = []
            cosmetics_list.extend(glob.glob("DeadByDaylight\Content\Data\Store\*\*\OutfitDB.json"))
            cosmetics_list.extend(glob.glob('DeadByDaylight\Content\Data\OutfitDB.json'))
            cosmetics_list.extend(glob.glob("DeadByDaylight\Content\Data\Store\*\*\CustomizationItemDB.json"))
            cosmetics_list.extend(glob.glob("components\currencies.json"))

            dataExport = Export.Export(emptyDataObject, cosmetics_list, CosmeticsDB.CosmeticsDB, 'Cosmetics.json', True)

            item_list = []
            item_list.extend(glob.glob("DeadByDaylight\Content\Data\Dlc\*\CustomizationItemDB.json"))
            item_list.extend(glob.glob("DeadByDaylight\Content\Data\Dlc\*\Charms\CustomizationItemDB.json"))
            item_list.extend(glob.glob("DeadByDaylight\Content\Data\Dlc\*\Charms\Secret\CustomizationItemDB.json"))
            item_list.extend(glob.glob('DeadByDaylight\Content\Data\CustomizationItemDB.json'))
            item_list.extend(glob.glob('DeadByDaylight\Content\Data\Main\Charms\PerkCharms\CustomizationItemDB.json'))

            Export.Export(dataExport, item_list, CosmeticsDB.DefaultItemCosmeticsDB, 'Cosmetics.json', False)
        
        # Perks
        if choice == 2 or choice == 0:
            perks_list = []
            perks_list.extend(glob.glob("DeadByDaylight\Content\Data\PerkDB.json"))
            perks_list.extend(glob.glob("DeadByDaylight\Content\Data\Dlc\*\PerkDB.json"))

            Export.Export(emptyDataObject, perks_list, PerksDB.PerksDB, 'Perks.json', False)

        # Characters
        if choice == 3 or choice == 0:
            characters_list = []
            characters_list.extend(glob.glob("DeadByDaylight\Content\Data\CharacterDescriptionDB.json"))
            characters_list.extend(glob.glob("DeadByDaylight\Content\Data\Dlc\*\CharacterDescriptionDB.json"))

            Export.Export(emptyDataObject, characters_list, CharactersDB.CharactersDB, 'Characters.json', False)

        # Archive Journals
        if choice == 4 or choice == 0:
            journals_list = []
            journals_list.extend(glob.glob("DeadByDaylight\Content\Data\Archives\*\ArchiveJournalDB.json"))

            Export.Export(emptyDataObject, journals_list, JournalsDB.ArchiveJournalDB, 'Journals.json', False)

        # Maps
        if choice == 5 or choice == 0:
            maps_list = []
            maps_list.extend(glob.glob("DeadByDaylight\Content\Data\ProceduralMaps.json"))

            Export.Export(emptyDataObject, maps_list, MapsDB.ProceduralMapsDB, 'Maps.json', False)

        # DLC
        if choice == 6 or choice == 0:
            dlc_list = []
            dlc_list.extend(glob.glob("DeadByDaylight\Content\Data\DlcDB.json"))
            dlc_list.extend(glob.glob("DeadByDaylight\Content\Data\*\*\DlcDB.json"))

            Export.Export(emptyDataObject, dlc_list, DlcDB.DlcDB, 'DLC.json', False)

        # Addons
        if choice == 7 or choice == 0:
            addons_list = []
            addons_list.extend(glob.glob("DeadByDaylight\Content\Data\ItemAddonDB.json"))
            addons_list.extend(glob.glob("DeadByDaylight\Content\Data\*\*\ItemAddonDB.json"))

            Export.Export(emptyDataObject, addons_list, AddonsDB.ItemAddonsDB, 'Addons.json', False)

        # Offerings
        if choice == 8 or choice == 0:
            offerings_list = []
            offerings_list.extend(glob.glob("DeadByDaylight\Content\Data\OfferingDB.json"))
            offerings_list.extend(glob.glob("DeadByDaylight\Content\Data\*\*\OfferingDB.json"))

            Export.Export(emptyDataObject, offerings_list, OfferingsDB.OfferingDB, 'Offerings.json', False)

        # Tomes
        if choice == 9 or choice == 0:
            tomes_list = []
            tomes_list.extend(glob.glob("DeadByDaylight\Content\Data\Archives\*\ArchiveDB.json"))

            Export.Export(emptyDataObject, tomes_list, TomesDB.TomesDB, 'Tomes.json', False)

        # Rifts
        if choice == 10 or choice == 0:
            rifts_list = []
            rifts_list.extend(glob.glob("DeadByDaylight\Content\Data\Archives\*\ArchiveDB.json"))

            Export.Export(emptyDataObject, rifts_list, RiftsDB.RiftsDB, 'Rifts.json', False)

        # Items
        if choice == 11 or choice == 0:
            items_list = []
            items_list.extend(glob.glob("DeadByDaylight\Content\Data\ItemDB.json"))
            items_list.extend(glob.glob("DeadByDaylight\Content\Data\*\*\ItemDB.json"))

            Export.Export(emptyDataObject, items_list, ItemsDB.ItemsDB, 'Items.json', False)
        
        # Exit
        if choice == 12:
            sys.exit()

if __name__ == "__main__":
    main()