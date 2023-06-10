import sqlite3 as sq

with sq.connect('rps.db') as con:
    cus = con.cursor()
    cus.execute('''CREATE TABLE IF NOT EXISTS player (
    nickname TEXT,
    scores INTEGER
    )''')


def get_score(player: str):
    with sq.connect('rps.db') as con_1:
        cus_1 = con_1.cursor()
        return cus_1.execute('''SELECT scores FROM player WHERE nickname = ?''', (player,)).fetchone()


def plus_score(player: str):
    with sq.connect('rps.db') as con_2:
        cus_2 = con_2.cursor()
        cus_2.execute('''UPDATE player SET scores = scores + 2 WHERE nickname = ?''', (player,))


def minus_score(player: str):
    with sq.connect('rps.db') as con_3:
        cus_3 = con_3.cursor()
        cus_3.execute('''UPDATE player SET scores = scores - 1 WHERE nickname = ?''', (player,))


def check_user(player: str):
    with sq.connect('rps.db') as con_4:
        cus_4 = con_4.cursor()

        return cus_4.execute('''SELECT nickname FROM player WHERE nickname = ?''', (player,)).fetchone() is not None


def add_user(nick: str):
    with sq.connect('rps.db') as con_5:
        cus_5 = con_5.cursor()
        cus_5.execute('''INSERT INTO player(nickname, scores) VALUES (?, 0)''', (nick,))
