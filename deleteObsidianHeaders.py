import os
import sys

VAULT_PATH = "insert path here"


for root, subFolders, files in os.walk(VAULT_PATH):
    for file in files:
        file_path = os.path.join(root, file)
        if file.endswith('.md'):
            with open(file_path, "r") as f:
                lines = f.readlines()
            counter = 0
            with open(file_path, 'w') as f:
                for line in lines:
                    if line.startswith("# ") and counter == 0:
                        print("Deleted ", line, " from ", file)
                        counter = 1
                    else:
                        f.write(line)
