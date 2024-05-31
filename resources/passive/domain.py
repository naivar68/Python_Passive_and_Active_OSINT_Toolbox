import subprocess
from bash import bash
import netstat
import ipwhois
from ipwhois import IPWhois
from geoip import geolite2
import sqlite3
import hashlib
import time
import binasciifrom database_setup import DatabaseSetup

class Domain:
    def __init__(self, username):
        self.db_setup = DatabaseSetup()
        self.username = username

    def run_command(self, command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return output.decode('utf-8')

    def netstat(self):
        subprocess.system("cls" if os.name == "nt" else "clear")
        domain_name = input("Enter the domain name: ")
        output = self.run_command("netstat -antup")
        print(output)
        self.db_setup.c.execute("INSERT INTO UserNotes (NoteTitle, NoteContent) VALUES (?, ?)", (self.username + "_netstat", output))
        self.db_setup.conn.commit()
        print("Note saved successfully")
        time.sleep(2)

    def geoip(self, ip_address):
        output = geolite2.lookup(ip_address)
        print(output)
        output_chart = pandas.DataFrame(output)
        output_chart.to_csv(self.username + "_geoip.csv")
        print("GeoIP data saved to " + self.username + "_geoip.csv")

        self.db_setup.c.execute("INSERT INTO UserNotes (NoteTitle, NoteContent) VALUES (?, ?)", (self.username + "_geoip", output))
        self.db_setup.conn.commit()
        Print("Note saved successfully")
        time.sleep(2)

    def whois_lookup(self, domain_name):
        output = IPWhois(domain_name)
        output = output.lookup_whois()
        print(output)
        print(f"For the following domain: {domain_name}")
        self.db_setup.c.execute("INSERT INTO UserNotes (NoteTitle, NoteContent) VALUES (?, ?)", (self.username + "_whois_lookup", output))
        self.db_setup.conn.commit()
        print("Note saved successfully")
        time.sleep(2)

