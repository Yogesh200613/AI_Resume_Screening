import sqlite3


def create_database():

    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        filename TEXT,
        score INTEGER,
        jd_match INTEGER,
        recommendation TEXT

    )
    """)

    conn.commit()
    conn.close()


def save_resume(user_id, filename, score, jd_match, recommendation):

    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO resumes
    (user_id, filename, score, jd_match, recommendation)

    VALUES (?,?,?,?,?)
    """, (user_id, filename, score, jd_match, recommendation))

    conn.commit()
    conn.close()


def create_user_table():

    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        username TEXT,
        password TEXT

    )
    """)

    conn.commit()
    conn.close()