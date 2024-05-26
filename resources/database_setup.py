import sqlite3
import pathlib
import subprocess
import cryptography



class DataCreation:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.create_table()

        def create_directories(self):
            pass

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
        self.conn.commit()

    def add_user(self, username, password):
        self.c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        self.conn.commit()

    def get_user(self, username):
        self.c.execute('SELECT * FROM users WHERE username = ?', (username,))
        return self.c.fetchone()

    def get_all_users(self):
        self.c.execute('SELECT * FROM users')
        return self.c.fetchall()

    def delete_user(self, username):
        self.c.execute('DELETE FROM users WHERE username = ?', (username,))
        self.conn.commit()

    def update_user(self, username, password):
        self.c.execute('UPDATE users SET password = ? WHERE username = ?', (password, username))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()



