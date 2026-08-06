import sqlite3


def create_table():

    conn = sqlite3.connect("students.db")

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gender TEXT,
        reading INTEGER,
        writing INTEGER,
        prediction REAL

    )
    """)


    conn.commit()

    conn.close()



def save_prediction(
        gender,
        reading,
        writing,
        prediction
):

    conn = sqlite3.connect("students.db")

    cursor = conn.cursor()


    cursor.execute(
    """
    INSERT INTO predictions
    (
        gender,
        reading,
        writing,
        prediction
    )

    VALUES (?,?,?,?)

    """,
    (
        gender,
        reading,
        writing,
        prediction
    )
    )


    conn.commit()

    conn.close()



# create table when file runs

create_table()