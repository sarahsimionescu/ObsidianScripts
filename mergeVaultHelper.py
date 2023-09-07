import os


def get_md_files_in_folder(folder_path):
    """
    Return a list of full paths to .md files recursively found in the given folder_path.
    """
    md_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                md_files.append(full_path)

    return md_files


def get_matching_files(folder1, folder2):
    """
    Return a list of .md files in folder1 that have the same name as files in folder2.
    """
    folder1_files = {os.path.basename(f): f for f in get_md_files_in_folder(folder1)}
    folder2_files = {os.path.basename(f): f for f in get_md_files_in_folder(folder2)}

    matching_files = []

    for file_name, file_path in folder1_files.items():
        if file_name in folder2_files:
            matching_files.append(file_path)

    return matching_files


# jupyter nbconvert --to markdown Review.ipynb

folder2 = r"path to vault"
folder1 = r"path to vault"

matching = get_matching_files(folder1, folder2)

if matching:
    print("\nMatching .md files found:")
    for f in matching:
        print(os.path.basename(f))
else:
    print("\nNo matching .md files found.")
