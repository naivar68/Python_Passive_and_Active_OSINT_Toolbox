import sqlite3
import hashlib
import binascii
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class CreateFolders:
    def __init__(self):
        self.folders = ['screenshots', 'notes', 'reports']
        self.create_folders()

    def create_folders(self):
        for folder in self.folders:
            try:
                subprocess.run(f'mkdir {folder}', shell=True)
            except FileExistsError:
                pass

    def run_command(self, command):
        subprocess.run(command, shell=True)



class DatabaseSetup:
    def __init__(self, db_name='recon.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

    def create_tables(self):
        # Create table: Users
        self.c.execute('''CREATE TABLE IF NOT EXISTS Users
                        (Username text, Password text)''')
        # Create table: UserCredentials
        self.c.execute('''CREATE TABLE IF NOT EXISTS UserCredentials
                        (Username text, Password text)''')

        # Create table: Domain
        self.c.execute('''CREATE TABLE IF NOT EXISTS Domain
                        (DomainName text, SubDomain text)''')

        # Create table: SubDomains
        self.c.execute('''CREATE TABLE IF NOT EXISTS SubDomains
                        (SubDomainName text)''')

        # Create table: OpenPorts
        self.c.execute('''CREATE TABLE IF NOT EXISTS OpenPorts
                        (PortNumber int, ServiceName text)''')

        # Create table: ServicesRunning
        self.c.execute('''CREATE TABLE IF NOT EXISTS ServicesRunning
                        (ServiceName text, ProcessID int)''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS ScreenshotsTaken
                                (Screenshots glob, ScreenshotName text)''')

        # Create table: Whois
        self.c.execute('''CREATE TABLE IF NOT EXISTS Whois
                        (DomainName text, WhoisInfo text)''')

        # Create table: GeoIP
        self.c.execute('''CREATE TABLE IF NOT EXISTS GeoIP
                        (IPAddress text, GeoIPInfo text)''')

        # Crerate table: SocialMedia
        self.c.execute('''CREATE TABLE IF NOT EXISTS SocialMedia
                        (SocialMediaName text, SocialMediaLink text)''')

        # Create table: found emails
        self.c.execute('''CREATE TABLE IF NOT EXISTS FoundEmails
                        (EmailDiscovery text)''')

        # Create table: UserNotes
        self.c.execute('''CREATE TABLE IF NOT EXISTS UserNotes
                        (NoteTitle text, NoteContent text)''')



# Create table: UserReports
        self.conn = sqlite3.connect(self.recon.db)
        self.c.execute('''CREATE TABLE IF NOT EXISTS UserReports    
                        (ReportTitle text, ReportContent text)''')
        self.conn.commit()
        self.conn.close()


    def create_chart(self, chart_title, chart_data):
        df = pd.DataFrame(chart_data)
        df.plot(kind='bar')
        plt.title(chart_title)
        plt.show()
        with open('chart.png', 'wb') as f:
            plt.savefig(Charts/f)
        plt.close()
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("INSERT INTO ScreenshotsTaken VALUES (?, ?)", ('chart.png', chart_title))
        conn.commit()
        conn.close()

        return f"Chart created and saved as {chart_title}.png"

    def create_user_report(self, report_title, report_content):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("INSERT INTO UserReports VALUES (?, ?)", (report_title, report_content))
        conn.commit()
        conn.close()
        return f"Report {report_title} created and saved."




    def commit_and_close(self):
        # Commit the changes and close the connection
        self.conn.commit()
        self.conn.close()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def hash_password(password):
        # Hash a password for storing.
        salt = hashlib.sha256()
        salt.update(password.encode('utf-8'))
        return binascii.hexlify(salt.digest())

    @staticmethod
    def verify_password(hashed_password, user_password):
        # Verify a stored password against one provided by user
        return hashed_password == User.hash_password(user_password)

    def create_user_credentials(self):
        hashed_password = self.hash_password(self.password)
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("INSERT INTO UserCredentials VALUES (?, ?)", (self.username, hashed_password))
        conn.commit()
        conn.close()
        return f"User {self.username} created."

    def login(self):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("SELECT * FROM UserCredentials WHERE Username = ?", (self.username,))
        user = c.fetchone()
        conn.close()
        if user:
            if self.verify_password(user[1], self.password):
                return f"User {self.username} logged in."
            else:
                return "Invalid password."
        else:
            return "User not found."

    def delete_user(self):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("DELETE FROM UserCredentials WHERE Username = ?", (self.username,))
        conn.commit()
        conn.close()
        return f"User {self.username} deleted."

    def change_password(self, new_password):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        hashed_password = self.hash_password(new_password)
        c.execute("UPDATE UserCredentials SET Password = ? WHERE Username = ?", (hashed_password, self.username))
        conn.commit()
        conn.close()
        return f"Password for user {self.username} changed."

    def sceenshots_taken(self):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("SELECT * FROM ScreenshotsTaken")
        return c.fetchall()

    def take_screenshot(self, target, screenshot_name):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(target)
        driver.save_screenshot(f"images/{screenshot_name}.png")
        driver.quit()

        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("INSERT INTO ScreenshotsTaken VALUES (?, ?)", (screenshot_name, screenshot_name))
        conn.commit()
        conn.close()
        return f"Screenshot {screenshot_name} taken and saved."

    def show_notes(self):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("SELECT * FROM UserNotes")
        return c.fetchall()

    def add_note(self, note_title, note_content):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("INSERT INTO UserNotes VALUES (?, ?)", (note_title, note_content))
        conn.commit()
        conn.close()
        return f"Note {note_title} added."

    def delete_note(self, note_title):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("DELETE FROM UserNotes WHERE NoteTitle = ?", (note_title,))
        conn.commit()
        conn.close()
        return f"Note {note_title} deleted."

    def show_reports(self):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("SELECT * FROM UserReports")
        return c.fetchall()

    def add_report(self, report_title, report_content):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("INSERT INTO UserReports VALUES (?, ?)", (report_title, report_content))
        conn.commit()
        conn.close()
        return f"Report {report_title} added."

    def delete_report(self, report_title):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("DELETE FROM UserReports WHERE ReportTitle = ?", (report_title,))
        conn.commit()
        conn.close()
        return f"Report {report_title} deleted."

    def show_charts(self):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        c.execute("SELECT * FROM ScreenshotsTaken")
        return c.fetchall()





class writeToDB:
    def __init__(self, db_name='recon.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

    def write_to_db(self, table, data):
        self.c.execute(f"INSERT INTO {table} VALUES (?, ?)", data)
        self.conn.commit()
        self.conn.close()

    def read_from_db(self, table):
        self.c.execute(f"SELECT * FROM {table}")
        return self.c.fetchall()

    def read_from_db_where(self, table, column, value):
        self.c.execute(f"SELECT * FROM {table} WHERE {column} = ?", (value,))
        return self.c.fetchall()

    def delete_from_db(self, table, column, value):
        self.c.execute(f"DELETE FROM {table} WHERE {column} = ?", (value,))
        self.conn.commit()
        self.conn.close()

    def update_db(self, table, column, value, new_value):
        self.c.execute(f"UPDATE {table} SET {column} = ? WHERE {column} = ?", (new_value, value))
        self.conn.commit()
        self.conn.close()

    def create_table(self, table, columns):
        self.c.execute(f"CREATE TABLE IF NOT EXISTS {table} {columns}")
        self.conn.commit()
        self.conn.close()

    def drop_table(self, table):
        self.c.execute(f"DROP TABLE {table}")
        self.conn.commit()
        self.conn.close()

    def show_tables(self):
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return self.c.fetchall()

class EndProgram:
    def __init__(self):
        print("Program has ended.")
        exit(0)
        conn.close()









