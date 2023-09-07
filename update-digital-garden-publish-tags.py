import os
import re
import subprocess

#BEFORE RUNNING THIS CODE - COMMIT TO GIT

def parse_gitignore():
    ignored_files = subprocess.check_output("git ls-files --other", shell=True).splitlines()
    ignored_files = [file.decode('utf-8').replace('/', '\\') for file in ignored_files]
    return ignored_files

def is_ignored(file_path, ignored_files):
    if file_path in ignored_files:
        return True
    else:
        return False

def modify_md_header(file_path, publish):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            content = f.read()
        except UnicodeDecodeError:
            print(f'---------------------------- Could not read {file_path}')
            return

    # check if .md file OR if within an Excalidraw folder
    if not file_path.endswith('.md') or '\\Excalidraw\\' in file_path:
        return

    header_pattern = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)
    dg_publish_pattern = re.compile(r'^dg-publish:.*\n?', re.MULTILINE)

    # Remove any existing dg-publish lines
    content = re.sub(dg_publish_pattern, '', content)

    # Add the dg-publish line in the header
    if re.search(header_pattern, content):
        content = re.sub(header_pattern, fr'---\n\1\ndg-publish: {str(publish).lower()}\n---\n', content)
    else:
        content = f'---\ndg-publish: {str(publish).lower()}\n---\n' + content

    with open(file_path, 'w') as f:
        try:
            f.write(content)
        except UnicodeEncodeError:
            print(f'---------------------------- Could not write {file_path}')
            return

    print(f'{"✔️  " if publish else "❌  "}Updated {file_path} to {"publish" if publish else "not publish"}')



folder_path = r'NOTES'


ignored_files = parse_gitignore()

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            ignored = is_ignored(file_path, ignored_files)
            modify_md_header(file_path, not ignored)

