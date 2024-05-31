from social_media_discovery import EmailDiscovery
from database_setup import writeToDB, read_from_db
from email_queries import email_queries
import time
import subprocess




class EmailDiscovery:
    def __init__(self, email_query):
        self.email_query = email_query
        self.emails = []
        self.emails_found = []
        self.emails_not_found = []
        self.emails_not_valid = []
        self.emails_valid = []
    def email_discovery():
        query = input("Enter email query: [ex. 'company.com'] ")
        email_discovery = EmailDiscovery(query)
        email_discovery.find_emails()
        print(f"Email discovery for {query} complete.")
        time.sleep(1)
        writeToDB.conn.connect()
        writeToDB.c.execute("SELECT * FROM UserNotes WHERE NoteTitle = 'email_discovery'")
        email_results = writeToDB.c.fetchall()
        print(email_results)
        writeToDB.conn.close()
        time.sleep(1)
        print("Email discovery complete.")
        time.sleep(1)
        return email_results






