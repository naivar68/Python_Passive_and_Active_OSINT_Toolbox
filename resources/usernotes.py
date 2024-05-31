from database_setup import DatabaseSetup
from researcher import User

class UserNotes:
    def __init__(self, username, password):
        self.db_setup = DatabaseSetup()
        self.username = username
        self.password = password

    def authenticate(self):
        return User.login(self.username, self.password)

    def add_note(self, title, content):
        if not self.authenticate():
            return "Invalid credentials"
        self.db_setup.c.execute("INSERT INTO UserNotes (NoteTitle, NoteContent) VALUES (?, ?)", (title, content))
        self.db_setup.conn.commit()

    def modify_note(self, title, new_title, new_content):
        if not self.authenticate():
            return "Invalid credentials"
        self.db_setup.c.execute("UPDATE UserNotes SET NoteTitle = ?, NoteContent = ? WHERE NoteTitle = ?", (new_title, new_content, title))
        self.db_setup.conn.commit()

    def delete_note(self, title):
        if not self.authenticate():
            return "Invalid credentials"
        self.db_setup.c.execute("DELETE FROM UserNotes WHERE NoteTitle = ?", (title,))
        self.db_setup.conn.commit()

    def get_notes(self):
        if not self.authenticate():
            return "Invalid credentials"
        self.db_setup.c.execute("SELECT * FROM UserNotes")
        notes = self.db_setup.c.fetchall()
        self.db_setup.conn.close()
        return notes