from colorama import Fore, Style
import random
from functions import percentageMatches
import os


class Application:
    SEPARATOR = "$"

    def __init__(self, FileName, FileCopyName):
        self.FileName = FileName
        self.FileCopyName = FileCopyName

    def getDataInMap(self):
        map = dict()
        with open(self.FileName, "r") as file:
            for line in file.readlines():
                rusPhrase, englishPhrase = line.split(self.SEPARATOR)
                englishPhrase = englishPhrase.replace("\n", "")
                map[rusPhrase] = englishPhrase
        return map


    def toTranslate(self):
        map = self.getDataInMap()
        flag = True
        while flag:
            rusPhrase = random.choice(list(map))
            answer = map[rusPhrase].lower().replace(" ", "")
            print(f"{rusPhrase}    -    ", end="")
            while True:
                s = input()
                if s == "exit":
                    flag = False
                    break
                elif s == "clear":
                    os.system('clear')
                    break
                elif s == "next":
                    break
                elif s == "?":
                    print(f"correct answer    -    {map[rusPhrase]}")
                    print(f"{rusPhrase}    -    ", end="")
                else:
                    userAnswer = s.lower().replace(" ", "")
                    if answer != userAnswer:
                        print(Fore.RED + "Wrong!" + Style.RESET_ALL)
                        print(f"{percentageMatches(answer, userAnswer)}%")
                        print(f"{rusPhrase}    -    ", end="")
                    else:
                        print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
                        break



    def copyFile(self):
        with open(self.FileName, "r") as file:
            data = file.readlines()

        with open(self.FileCopyName, "w") as file:
            file.writelines(data)


    def pushWordsFile(self, map: dict):
        with open(self.FileName, "a") as file:
            for key, val in map.items():
                file.write(f"{key} {self.SEPARATOR} {val}\n")

    def add(self):

        self.copyFile()

        map = dict()
        while True:
            command = input("Which command do you want use? (push/del/add/exit/clear)    -    ")
            if command == "push":
                size = len(map)
                self.pushWordsFile(map)
                map = dict()
                print(f"push worked correctly. {size} phrases have been pushed")


            elif command == "del":
                key = input()
                del map[key]

                print("del worked correctly")


            elif command == "add":
                rusWord = input("russian phrase...    ")
                enWord = input("english phrase...    ")

                map[rusWord] = enWord

                print("add worked correctly")


            elif command == "exit":
                self.pushWordsFile(map)

                print("stop worked correctly")

                break

            elif command == "clear":
                os.system("clear")

            else:
                print(Fore.RED + "Wrong command!" + Style.RESET_ALL)


    def printAllWords(self):
        print("\n")
        map = self.getDataInMap()
        for rus, en in map.items():
            print(f"{rus}    -    {en}")
        print(f"{map.__len__()} phrases\n\n")


    def startApplication(self):
        while True:
            command = input("Which command do you want use? (translate/add/exit/clear/all_words)    -    ")
            if command == "add":
                self.add()
            elif command == "clear":
                os.system("clear")
            elif command == "translate":
                self.toTranslate()
            elif command == "exit": break
            elif command == "all_words":
                self.printAllWords()
            else:
                print(Fore.RED + "Wrong command!" + Style.RESET_ALL)
