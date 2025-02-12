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
        self.cursor.execute('INSERT INTO sentence (words, sentence) VALUES (?, ?)', (words, sentence))
        self.conn.commit()

    def get_data(self):
        """
        查看所有用户信息
        """
        self.cursor.execute('SELECT * FROM sentence')
        return self.cursor.fetchall()

    


if __name__ == "__main__":
    db = Database("./sentence.db")
#     db.create_data(
#         "degradation&&grip&&soar&&pattern&&toll&&exotic&&soften&&refine&&ballet&&budget&&generalisation",
#         """The **ballet** troupe, operating on a shoestring **budget**, found themselves in a tricky situation. There was a **degradation** in the enthusiasm of the audience, perhaps due to the repetitive **pattern** of their shows. To address this, they decided to toss out the old **generalisation** that simplicity was best and embrace something **exotic**. 

# They brought in a choreographer to **refine** the routines, adding in new and exciting movements. The dancers worked hard to improve their **grip** on these complex steps. As a result, the tickets sales started to **soar**. But this transformation didn't come without a **toll**; the stress on the dancers was high, and the management had to **soften** the training regime a bit to keep everyone's spirits up. 

# 中文释义：这个靠微薄预算运营的**芭蕾舞**团陷入了棘手的境地。观众的热情有所**减退**，可能是因为他们演出的**模式**过于重复。为了解决这个问题，他们决定摒弃 “简约至上” 这种旧有的**普遍观念**，去接纳一些充满**异域风情**的元素。

# 他们请来一位编舞师对舞蹈动作进行**优化**，加入了新颖又刺激的舞步。舞者们努力提升对这些复杂舞步的**掌控**能力。结果，门票销量开始**飙升**。但这种转变并非毫无**代价**；舞者们承受的压力很大，管理层不得不稍微**放宽**训练制度，以此来鼓舞大家的士气 。  """
#     )
    print(db.get_data())