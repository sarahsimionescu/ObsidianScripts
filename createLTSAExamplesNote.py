import os
import sys

LTSA_PATH = ""  # enter path to LTSA files

FILE_NAME = "./note.md"  # making a local demo note

for root, subFolders, files in os.walk(LTSA_PATH):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, "r") as f1, open(FILE_NAME, "a") as f2:
            f2.write("#### " + str(file) + "\n```\n")
            lines = f1.readlines()
            for line in lines:
                f2.write(line)
            f2.write("\n```\n")
