import os
import sys

VAULT_PATH="./" # enter vault path here

IGNORELIST = [ ]

for root, subFolders, files in os.walk(VAULT_PATH):
    for file in files:
        file_path = os.path.join(root, file)
        if file.endswith('.md') and file not in IGNORELIST:
            print("'",file,"',")
            with open(file_path, "r") as f:
                lines = f.readlines()
            tags = False
            counter = 0
            for line in lines:
                if line.startswith("---"):
                    tags = True
                    break
                else:
                    counter += 1
            if tags == True:
                lines[counter] += "dg-publish: true\n"
            else:
                if(len(lines) > 0):
                    lines[0] = "---\ndg-publish: true\n---\n" + lines[0]
                else:
                    lines.append("---\ndg-publish: true\n---\n") 
            with open(file_path, "w") as f:
                f.writelines(lines)