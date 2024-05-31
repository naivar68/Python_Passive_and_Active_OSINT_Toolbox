from bs4 import BeautifulSoup
import requests
import time
from database_setup import db_setup, writeToDB, read_from_db



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
        response = requests.get(self.domain)
        soup = BeautifulSoup(response.text, 'html.parser')
        mailtos = soup.select('a[href^=mailto]')
        for i in mailtos:
            email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', i['href'])
            if not email:
                continue
            else:
                print(email[0])

                self.db_setup.c.execute("INSERT INTO UserNotes (NoteTitle, NoteContent) VALUES (?, ?)", ("email_discovery", email[0]))
                self.db_setup.conn.commit()
            with open('/tmp/recon/notes/email_discovery.csv', 'a') as file:
                file.write(f"Found email: {email[0]}\n")
                time.sleep(2)




