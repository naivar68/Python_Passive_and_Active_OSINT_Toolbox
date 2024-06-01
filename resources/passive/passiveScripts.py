import subprocess
from bash import bash
import ipwhois
from ipwhois import IPWhois
from ipwhois.utils import get_countries
from ipwhois.net import Net
from ipwhois.asn import IPASN
import geolite
import geoip2
import geolite2utils
import requests
import sqlite3
import hashlib
import time
import binascii
from resources import (
    DatabaseSetup,
    writeToDB,
    User,
    UserNotes,
    Charts,
    EndProgram
)

from bs4 import BeautifulSoup

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

class SocialMediaDiscovery:
    def __init__(self, write_to_db, url, platforms):
        self.write_to_db = write_to_db
        self.url = url
        self.platforms = platforms


    def find_social_media(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')

        for link in links:
            href = link.get('href')
            if href:
                for platform in self.platforms:
                    if platform in href:
                        print(f"Found {platform} link: {href}")
                        self.write_to_db.c.execute("INSERT INTO UserNotes (NoteTitle, NoteContent) VALUES (?, ?)",
                                         ("social_media_discovery", href))
                        self.db_setup.conn.commit()
                    with open('/tmp/recon/notes/social_media_discovery.csv', 'a') as file:
                        file.write(f"Found {platform} link: {href}\n")
                        time.sleep(2)


class EmailDiscovery:
    def __init__(self, writeToDB, email_query):
        self.write_to_db = writeToDB
        self.email_query = email_query


    def find_emails(self):

        response = requests.get(self.email_query)
        soup = BeautifulSoup(response.text, 'html.parser')
        mailtos = soup.select('a[href^=mailto]')
        for i in mailtos:
            email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', i['href'])
            if not email:
                continue
            else:
                print(email[0])
                self.write_to_db.c.execute("INSERT INTO FoundEmails (EmailDiscovery, text) VALUES (?, ?)",
                                 ("email_discovery", email[0]))
                self.db_setup.conn.commit()
            with open('/tmp/recon/notes/email_discovery.csv', 'a') as file:
                file.write(f"Found email: {email[0]}\n")
                time.sleep(2)
