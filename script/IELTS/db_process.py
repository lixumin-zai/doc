import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_sentence_table()

    def create_sentence_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS sentence (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            words TEXT,
            sentence TEXT
        )
        ''')
        self.conn.commit()

    def create_data(self, words, sentence):
        """
        创建用户
        """
        self.cursor.execute('SELECT * FROM users WHERE wechat_id = ? OR verification_code = ?', 
                        (wechat_id, verification_code))
        if self.cursor.fetchone() is not None:
            raise UserAlreadyExistsError("该用户已存在")

        self.cursor.execute('INSERT INTO users (wechat_id, verification_code) VALUES (?, ?)', (wechat_id, verification_code))
        self.conn.commit()

    def get_users(self):
        """
        查看所有用户信息
        """
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    


if __name__ == "__main__":
    db = Database("./sentence.db")
    words = ["collision", "grip"]