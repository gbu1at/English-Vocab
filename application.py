from colorama import Fore, Style
import random
from functions import percentageMatches
import os


class Application:
    SEPARATOR = "$"

    def __init__(self, file_name, file_copy_name):
        self.file_name = file_name
        self.file_copy_name = file_copy_name

    def get_data_in_dictionary(self):
        dictionary = dict()
        with open(self.file_name, "r") as file:
            for line in file.readlines():
                rus_phrase, english_phrase = line.split(self.SEPARATOR)
                english_phrase = english_phrase.replace("\n", "")
                dictionary[rus_phrase] = english_phrase
        return dictionary

    def to_translate(self, ru=False):
        dictionary = self.get_data_in_dictionary()

        if ru:
            new_dictionary = dict()
            for ru, en in dictionary.items():
                new_dictionary[en] = ru
            dictionary = new_dictionary

        flag = True
        while flag:
            phrase = random.choice(list(dictionary))
            translation_phrase = dictionary[phrase].lower().replace(" ", "")
            print(f"{phrase}    -    ", end="")
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
                    print(f"correct answer    -    {dictionary[phrase]}")
                    print(f"{phrase}    -    ", end="")
                else:
                    user_translation_phrase = s.lower().replace(" ", "")
                    if translation_phrase != user_translation_phrase:
                        print(Fore.RED + "Wrong!" + Style.RESET_ALL)
                        print(f"{percentageMatches(translation_phrase, user_translation_phrase)}%")
                        print(f"{phrase}    -    ", end="")
                    else:
                        print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
                        break

    def copy_file(self):
        with open(self.file_name, "r") as file:
            data = file.readlines()

        with open(self.file_copy_name, "w") as file:
            file.writelines(data)

    def push_words_file(self, dictonaty: dict):
        with open(self.file_name, "a") as file:
            for key, val in dictonaty.items():
                file.write(f"{key} {self.SEPARATOR} {val}\n")

    def add(self):

        self.copy_file()

        dictionary = dict()
        while True:
            command = input("Which command do you want use? (push/del/add/exit/clear)    -    ")
            if command == "push":
                size = len(dictionary)
                self.push_words_file(dictionary)
                dictionary = dict()
                print(f"push worked correctly. {size} phrases have been pushed")

            elif command == "del":
                key = input()
                del dictionary[key]

                print("del worked correctly")

            elif command == "add":
                rus_word = input("russian phrase...    ")
                en_word = input("english phrase...    ")

                dictionary[rus_word] = en_word

                print("add worked correctly")

            elif command == "exit":
                self.push_words_file(dictionary)

                print("stop worked correctly")

                break

            elif command == "clear":
                os.system("clear")

            else:
                print(Fore.RED + "Wrong command!" + Style.RESET_ALL)

    def print_all_words(self):
        print("\n")
        dictionary = self.get_data_in_dictionary()
        for rus, en in dictionary.items():
            print(f"{rus}    -    {en}")
        print(f"{dictionary.__len__()} phrases\n\n")

    def start_application(self):
        while True:
            command = input("Which command do you want use? (translate/add/exit/clear/all_words)    -    ")
            if command == "add":
                self.add()
            elif command == "clear":
                os.system("clear")
            elif command == "translate":
                par = input()
                if par == "ru":
                    self.to_translate(True)
            elif command == "exit":
                break
            elif command == "all_words":
                self.print_all_words()
            else:
                print(Fore.RED + "Wrong command!" + Style.RESET_ALL)
