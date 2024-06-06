import subprocess
import re
import pathlib



def find_occurrences(word, file, line):
    search = input("Enter the word you want to search for: ")
    word = re.compile(search)
    with open(file, 'r') as file:
        for line in file:
            occurrences = re.findall(word, line)
            if occurrences:
                print(f"Found {len(occurrences)} occurrences of '{word}' in {file}")
                for occurrence in occurrences:
                    print(occurrence)
            else:
                print(f"No occurrences of '{word}' found in {file}")


def main():



