import re
import subprocess
import pathlib
from database_setup import endProgram


subprocess.system("cls" if subprocess.os.name == "nt" else "clear")

print("Welcome to the Cleanser tool.")
print("This tool will clean up .bashrc and PowerShell logs.")
print("Please ensure you have the necessary permissions to run this tool.")
print("This tool will remove any log entries in .bashrc and PowerShell logs.")
print("This tool will not remove any other entries.")
print("Please ensure you have a backup of your logs before running this tool.")
print("This tool will not be held responsible for any data loss.")
print("\nDo you need to cleanse .bashrc or PowerShell logs?")
print("1. .bashrc")
print("2. PowerShell logs")
print("3. Exit")
choice = input("Enter your choice: ")

if choice == "1":
    linux_bashrc()
elif choice == "2":
    powershell_logs()
elif choice == "3":
    endProgram()
else:
    print("Invalid choice. Exiting...")
    endProgram()

# Get the home directory and username
home = str(pathlib.Path.home())
username = subprocess.os.getlogin()
print(f"Home directory: {home}\n Username: {username}\n")
print("Cleaning up .bashrc and PowerShell logs...\n")
# Define regular expressions for .bashrc and PowerShell log entries.
bashrc_regex = r'echo "(?P<user>.*)">>?(?P<file>.*)'
powershell_regex = r'[sS]et-Variable -Name "(?P<user>.*)" -Value "(?P<value>.*)"'

# Find .bashrc entries
def linux_bashrc():
    with open(f'{home}/{username}/.bashrc', 'r') as file:
        bashrc_matches = re.findall(bashrc_regex, file.read())

    if bashrc_matches:
        print("Bashrc matches found:")
        for match in bashrc_matches:
            print(match)
            # Remove the log entries
            subprocess.system(f"sudo rm -rf {match[0:]}")
    else:
        print("No bashrc matches found.")
    print("\nCleanup complete.")
    endProgram()



# Find PowerShell log entries
def powershell_logs():
    with open('C:/Windows/System32/config/systemprofile/.bashrc', 'r') as file:
        powershell_matches = re.findall(powershell_regex, file.read())

    if powershell_matches:
        print("\nPowerShell matches found:")
        for match in powershell_matches:
            print(match)
            # Remove the log entries
            subprocess.system(f"del {match[0:]}")
    else:
        print("No PowerShell matches found.")
    print("\nCleanup complete.")
    endProgram()
