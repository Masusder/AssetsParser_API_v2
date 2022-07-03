from colorama import Fore

class Style:
    BOLD = '\033[1m'
    END = '\033[0m'

class UI:
    def start():
        print(Fore.CYAN + "   _                _           ___                         ")
        print(Fore.CYAN + "  /_\  ___ ___  ___| |_ ___    / _ \__ _ _ __ ___  ___ _ __ ")
        print(Fore.CYAN + " //_\ / __/ __|/ _ \ __/ __|  / /_)/ _` | '__/ __|/ _ \ '__|")
        print(Fore.CYAN + "/  _  \__ \__ \  __/ |_\__ \ / ___/ (_| | |  \__ \  __/ |   ")
        print(Fore.CYAN + "\_/ \_/___/___/\___|\__|___/ \/    \__,_|_|  |___/\___|_|   ")
        print(Fore.CYAN + "                                                            ")
        print()
        print("Welcome to parser of Dead By Daylight game assets.")
        print("This tool is used to create full DBD API.")
        print(Fore.CYAN + "Made by: " + Fore.WHITE + "Masus")

    def menu(prompt, options):
        print("\n" + Fore.CYAN + prompt + Fore.WHITE)
        while True:
            for i in range(len(options)):
                print("{}. {}".format(options[i][0], options[i][1]))
            choice = input("\n>>> ")
            for i in range(len(options)):
                if(choice == options[i][0]):
                    try:
                        number = int(choice)
                        return number
                    except ValueError:
                        return choice

            print(Fore.RED + "Invalid input!\n" + Fore.WHITE)
