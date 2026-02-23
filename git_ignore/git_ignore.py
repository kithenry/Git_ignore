# Create .gitignore file
# Add all extensions mentioned to it.

import os
import argparse

updates = ['.gitignore',
            '*~',
            '__pycache__',
            '*.db',
           '.env'
            ]


def write_to_file(file_uri, data):
    try:
        with open(file_uri,"w") as f:
            for item in data:
                f.write(item + "\n")
    except Exception as e:    
        return True


def read_ignore_file():
    with open('.gitignore') as f:
        items =  f.readlines()
        items = [item.strip('\n').strip() for item in items]
        return items

def get_or_create_ignore_file():
    # find if it exists
    # if it does not, create, else, skip
    # return True (false if theres an exception)
    if not os.path.exists('.gitignore'):
        return []
    else:
        return read_ignore_file()

    

def update_ignore_file(current_items, updates):
    current_items.extend(updates)
    update_list = set(current_items)
    return update_list


def create_or_update():
    current_items = get_or_create_ignore_file()
    update_list = update_ignore_file(current_items, updates)
    write_to_file(".gitignore", update_list)

def main():
    parser = argparse.ArgumentParser(description="Git_ignore management utility")
    parser.add_argument("action", help="Action to run. Default: Run -- Create or update ignore file")
    args = parser.parse_args()

    if args.action == "run":
        create_or_update()
    
