''' 
Created by Ryan Coulson.

Given a directory, scan through all the files and return a list of
all files that include a certain keyword. '''

import os

directory = input("Enter directory to search: ")
os.chdir('../' + directory)
files = [i for i in os.listdir() if i[len(i)-3:] == '.py']   # this is kinda meh, fix later

keywords = input("Enter keywords (separate by comma): ")

while keywords != '!q':
    parsed_keywords = [i.strip() for i in keywords.split(",")]

    found_keys = {}
    found, count = 0, 0


    for file in files:
        f = open(file)
        words = f.read().lower()

        for key in parsed_keywords:
            if key in words:
                if key not in found_keys:
                    found_keys[key] = [file]
                else:
                    found_keys[key].append(file)
                found += 1
        count += 1
        f.close()

    print('='*20)    
    print('Done. Found ', found, ' results for `', ', '.join(parsed_keywords) ,\
          '` in ', count,' files.', sep='')
    print('='*20)
    print('Results:')

    for key in found_keys:
        print('='*5, key.upper(), '='*5)
        for file in found_keys[key]:
            print(file)

    keywords = input("Enter keywords (separate by comma): ")

