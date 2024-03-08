from colorama import Fore, Style
import re
from application import Application
import os



if __name__ == "__main__":
    while True:
        command = input("Which command do you want use? (go/create/exit/clear)    -    ")

        if command == "exit":
            break

        elif command == "clear":
            os.system("clear")

        elif command == "create":
            newFileName = input("Write the file name...\t")
            if newFileName == "cancel": continue

            with open(f"VOC/{newFileName}.txt", "w") as f:
                pass

            continue

        elif command == "go":

            listFileNames = set(map(lambda fileName: fileName.split(".txt")[0].split("Copy")[0], os.listdir("VOC")))

            print()
            print(*listFileNames, sep="\n")
            print()

            f = input("Write the file name...\t")

            if f == "cancel": continue

            FileName = "VOC/" + f
            FileCopyName = FileName + "Copy.txt"
            FileName += ".txt"

            if not os.path.isfile(FileName):
                print(Fore.RED + "Wrong path to file!" + Style.RESET_ALL)
                continue

            Application(FileName, FileCopyName).startApplication()

        else:
            print("Wrong command")