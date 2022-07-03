class Format:
    # Format Rarity
    def PrettyRarity(Rare):
        # EItemRarity::VeryRare
        ret = Rare.split('::')

        return ret[1]

    # Format Availability
    def PrettyAvailable(available):
        ret = available.split('::')

        return ret[1]

    # Format Character Role
    def PrettyRole(Role):
        ret = Role.split('::')
        roleList = {
                'VE_Camper': 'Camper',
                'VE_Slasher':'Killer', 
                'VE_Observer': 'Observer',
                'VE_None': 'None'
            }

        return roleList[ret[1]]

    # Format Difficulty
    def PrettyDifficulty(Diff):
        ret = Diff.split('::')
        diffList = {
                'VE_None': 'None',
                'VE_Easy': 'Easy',
                'VE_Intermediate':'Medium', 
                'VE_Hard': 'Hard',
                'VE_VeryHard': 'VeryHard'
            }

        return diffList[ret[1]]

    # Format Character Gender
    def PrettyGender(Gender):
        # EGender::VE_Male
        ret = Gender.split('::')
        genderList = {
                'VE_Male': 'Male',
                'VE_Female':'Female', 
                'VE_NotHuman': 'Not Human',
                'VE_Multiple': 'Multiple',
                'VE_Undefined': 'Undefined'
            }

        return genderList[ret[1]]

    # Format Perk Category
    def PrettyCategory(Category):
        try:
            ret = Category.split('::')
            string = ''.join(map(str, ret[1]))
        except:
            Category = None

        return string

    # Format Addon Type
    def PrettyType(Type):
        stringOne = ''.join(map(str, Type))
        splitString = stringOne.split('::')
        stringTwo = ''.join(splitString[1])

        return stringTwo

    # Format Addon Type
    def PrettyOfferingType(Type):
        ret = Type.split('::')

        return ret[1]

    # Format Perk Tag
    def PrettyPerkTag(Tag):
        stringOne = ''.join(map(str, Tag))

        return stringOne

    # Format Ability
    def PrettyAbility(Ability):
        ret = Ability.split('::VE_')

        return ret[1]

    # Cosmetics Description Format
    def ParseCosmeticsDescription(value):
        try:
            Description = value['UIData']['Description']['SourceString']
        except:
            Description = value['CollectionDescription']['SourceString']
        
        return Description

    # Cosmetics Collection Name Format
    def ParseCollectionName(value):
        try:
            CollName = value['CollectionName']['SourceString']
        except:
            CollName = None
        
        return CollName

    # Perks Description Format
    def ParsePerksDescription(value):
        try:
            Description = value['UIData']['Description']['SourceString']
        except:
            Description = value['PerkLevel3Description']['SourceString']
        
        return Description

    # DLC Name Format
    def ParseDLCDescription(value):
        try:
            Description = value['UnlockDescription']['SourceString']
        except:
            Description = None
        
        return Description