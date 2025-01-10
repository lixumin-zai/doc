import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS sentence (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            words TEXT,
            sentence TECT
        )
        ''')
        self.conn.commit()

    