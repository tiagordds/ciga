import sqlite3


def save_to_db(text):
    conn = sqlite3.connect("ciga.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS latest_edital (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            text TEXT
        )
    """)

    cursor.execute(
        """
        INSERT INTO latest_edital (id, text) VALUES (1, ?)
        ON CONFLICT(id) DO UPDATE SET text = excluded.text
    """,
        (text,),
    )

    conn.commit()
    conn.close()


def get_saved_text():
    conn = sqlite3.connect("ciga.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS latest_edital (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            text TEXT
        )
    """)

    cursor.execute("SELECT text FROM latest_edital WHERE id = 1")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None


def is_same_as_saved(new_text):
    saved_text = get_saved_text()
    return new_text == saved_text
