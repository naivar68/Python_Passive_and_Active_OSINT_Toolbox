import binascii
import hashlib
import sqlite3
import subprocess
import matplotlib.pyplot as plt
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import streamlit as st



class CreateFolders:
    def __init__(self, folder_name='OSINT-Recon'):
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
    def __init__(self, db_name='OSINT.db'):
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
        self.conn = sqlite3.connect(self.db_name)
        self.c.execute('''CREATE TABLE IF NOT EXISTS UserReports    
                        (ReportTitle text, ReportContent text)''')
        self.conn.commit()
        self.conn.close()

    def create_user_report(self, report_title, report_content):
        self.conn = sqlite3.connect('OSINT.db')
        self.conn = conn.cursor()
        c.execute("INSERT INTO UserReports VALUES (?, ?)", (report_title, report_content))
        self.conn.commit()
        self.conn.close()
        return f"Report {report_title} created and saved."

    def commit_and_close(self):
        # Commit the changes and close the connection
        self.conn.commit()
        self.conn.close()


class Charts:
    def __init__(self, username):
        self.username = username
        self.conn = sqlite3.connect('OSINT.db')
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS UserNotes (Charts glob, Chart_Graphic TEXT)")
        self.conn.commit()
        self.conn.close()

    def chart_data(self, chart_name):
        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        c.execute("SELECT Chart_Graphic FROM Charts WHERE Chart_Graphic = ?", (chart_name,))
        chart_data = self.c.fetchall()
        self.conn.close()
        return chart_data

    def create_chart(self, chart_name, chart_data):
        self.conn = sqlite3.connect('OSINT.db')
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO Charts (Chart_Graphic, Chart_Data) VALUES (?, ?)", (chart_name, chart_data))
        self.conn.commit()
        self.conn.close()
        return True

    def bar_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='bar')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        self.conn = sqlite3.connect('OSINT.db')
        c = conn.cursor()
        c.execute("INSERT INTO Charts (Chart_Graphic, Chart_Data) VALUES (?, ?)", (chart_name, chart_name + ".png"))
        self.conn.commit()
        self.conn.close()

    def line_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='line')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        c.execute("INSERT INTO Charts (Chart_Graphic, Chart_Data) VALUES (?, ?)", (chart_name, chart_name + ".png"))
        c.commit()
        c.close()


    def scatter_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='scatter')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        c.execute("INSERT INTO Charts (Chart_Graphic, Chart_Data) VALUES (?, ?)", (chart_name, chart_name + ".png"))
        c.commit()
        c.close()


    def pie_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='pie')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        c.execute("INSERT INTO Charts (Chart_Graphic, Chart_Data) VALUES (?, ?)", (chart_name, chart_name + ".png"))
        c.commit()
        c.close()


    def hist_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='hist')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        c.execute("INSERT INTO Charts (Chart_Graphic, Chart_Data) VALUES (?, ?)", (chart_name, chart_name + ".png"))
        c.commit()
        c.close()


    def box_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='box')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        c.execute("INSERT INTO Charts (Chart_Graphic, Chart_Data) VALUES (?, ?)", (chart_name, chart_name + ".png"))
        c.commit()
        c.close()


    def area_chart(self, chart_name, chart_data):
        chart_data = pd.read_csv(chart_data)
        chart_data.plot(kind='area')
        plt.title(chart_name)
        plt.savefig(chart_name + ".png")
        plt.show()
        self.create_chart(chart_name, chart_name + ".png")
        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        c.execute("INSERT INTO Charts (Chart_Graphic, Chart_Data) VALUES (?, ?)", (chart_name, chart_name + ".png"))
        c.commit()
        c.close()


class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @staticmethod
    def hash_password(password):
        # Hash a password for storing.
        salt = hashlib.sha256()
        salt.update(password.encode('utf-8'))
        return binascii.hexlify(salt.digest())





    @staticmethod
    def signup(self, username, password):
        self.initialize.db()
        self.CreateFolders()

        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        c.execute("INSERT INTO UserCredentials VALUES (?, ?)", (self.username, self.hash_password(self.password)))
        c.commit()
        c.close()
        return True




    @staticmethod
    def verify_password(hashed_password, user_password):
        # Verify a stored password against one provided by user
        return hashed_password == User.hash_password(user_password)

    @staticmethod

    def login(self):
        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        c.execute("SELECT * FROM UserCredentials WHERE Username = ?", (self.username,))
        user = c.fetchone()
        c.close()
        if user:
            if self.verify_password(user[1], self.password):
                return f"User {self.username} logged in."
            else:
                return "Invalid password."
        else:
            return "User not found."

    def delete_user(self):
        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        c.execute("DELETE FROM UserCredentials WHERE Username = ?", (self.username,))
        c.commit()
        c.close()
        return f"User {self.username} deleted."

    def change_password(self, new_password):
        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        hashed_password = self.hash_password(new_password)
        c.execute("UPDATE UserCredentials SET Password = ? WHERE Username = ?", (hashed_password, self.username))
        c.commit()
        c.close()
        return f"Password for user {self.username} changed."

    def sceenshots_taken(self):
        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        c.execute("SELECT * FROM ScreenshotsTaken")
        return c.fetchall()

    def take_screenshot(self, target, screenshot_name):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(target)
        driver.save_screenshot(f"images/{screenshot_name}.png")
        driver.quit()

        self.conn = sqlite3.connect('OSINT.db')
        c = self.conn.cursor()
        c.execute("INSERT INTO ScreenshotsTaken VALUES (?, ?)", (screenshot_name, screenshot_name))
        c.commit()
        c.close()
        return f"Screenshot {screenshot_name} taken and saved."


class UserNotes:
    def __init__(self, Title, Content):
        self.db_conn = sqlite3.connect('OSINT.db')
        self.Title = Title
        self.Content = Content

    def authenticate(self):
        return User.login(self.username, self.password)

    def add_note(self, title, content, username, password):
        if not self.authenticate():
            return "Invalid credentials"
        else:
            self.conn = sqlite3.connect('OSINT.db')
            c = self.conn.cursor()
            c.execute("INSERT INTO UserNotes VALUES (?, ?)", (title, content))
            c.commit()
            c.close()
            return f"Note {title} added."



    def modify_note(self, title, new_title, new_content):
        if not self.authenticate():
            return "Invalid credentials"
        else:
            self.conn = sqlite3.connect('OSINT.db')
            c = self.conn.cursor()
            c.execute("UPDATE UserNotes SET NoteTitle = ?, NoteContent = ? WHERE NoteTitle = ?", (new_title, new_content, title))
            c.commit()
            c.close()
            return f"Note {title} modified."





    def delete_note(self, title, content, username, password):
        if not self.authenticate():
            return "Invalid credentials"
        else:
            self.conn = sqlite3.connect('OSINT.db')
            c = self.conn.cursor()
            c.execute("DELETE FROM UserNotes WHERE NoteTitle = ?", (title,))
            c.commit()
            c.close()
            return f"Note {title} deleted."




    def get_notes(self, title, content, username, password):
        if not self.authenticate():
            return "Invalid credentials"
        else:
            self.conn = sqlite3.connect('OSINT.db')
            c = self.conn.cursor()
            c.execute("SELECT * FROM UserNotes")
            return c.fetchall()





class writeToDB:
    def __init__(self, db_name='OSINT.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

    def write_to_db(self, table, data):
        self.conn = sqlite3.connect(self.db_name)
        c = self.conn.cursor()
        self.c.execute(f"INSERT INTO {table} VALUES (?, ?)", data)
        self.conn.commit()
        self.conn.close()

    def read_from_db(self, tables):
        self.conn = sqlite3.connect(self.db_name)
        c = self.conn.cursor()
        self.c.execute(f"SELECT * FROM {tables}")
        return self.c.fetchall()

    def read_from_db_where(self, table, column, value):
        self.conn = sqlite3.connect(self.db_name)
        c = self.conn.cursor()
        self.c.execute(f"SELECT * FROM {table} WHERE {column} = ?", (value,))
        return self.c.fetchall()

    def delete_from_db(self, table, column, value):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        self.c.execute(f"DELETE FROM {table} WHERE {column} = ?", (value,))
        self.conn.commit()
        self.conn.close()

    def update_db(self, table, column, value, new_value):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        self.c.execute(f"UPDATE {table} SET {column} = ? WHERE {column} = ?", (new_value, value))
        self.conn.commit()
        self.conn.close()

    def create_table(self, table, columns):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        self.c.execute(f"CREATE TABLE IF NOT EXISTS {table} {columns}")
        self.conn.commit()
        self.conn.close()

    def drop_table(self, table):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        self.c.execute(f"DROP TABLE {table}")
        self.conn.commit()
        self.conn.close()

    def show_tables(self):
        conn = sqlite3.connect('recon.db')
        c = conn.cursor()
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return self.c.fetchall()


class EndProgram:
    def __init__(self):
        print("Program has ended.")
        exit(0)
        self.conn.close()

if __name__ == '__main__':
    db = DatabaseSetup()
    db.create_tables()
    folders = CreateFolders()
    db.commit_and_close()
    print("Database and folders created.")
    print("Program has ended.")
    exit(0)
