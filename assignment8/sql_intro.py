import sqlite3
from pathlib import Path


def get_or_create_publisher(conn, name):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            return row[0]
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error in get_or_create_publisher: {e}")
        return None
def get_or_create_magazine(conn, name, publisher_id):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row:
            return row[0]
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error in get_or_create_magazine: {e}")
        return None
def get_or_create_subscriber(conn, name, address):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", (name, address))
        row = cursor.fetchone()
        if row:
            return row[0]
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error in get_or_create_subscriber: {e}")
        return None
def get_or_create_subscription(conn, subscriber_id, magazine_id, expiration_date):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT 1 FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
            (subscriber_id, magazine_id)
        )
        if cursor.fetchone():
            return False
        cursor.execute(
            "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
            (subscriber_id, magazine_id, expiration_date)
        )
        return True
    except sqlite3.Error as e:
        print(f"Error in get_or_create_subscription: {e}")
        return False
       
    
def main():
    db_path = Path(__file__).parent.parent / "db" / "magazines.db"
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS publishers (publisher_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE)")
        cursor.execute("CREATE TABLE IF NOT EXISTS magazines (magazine_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE, " \
                       "publisher_id INTEGER NOT NULL, FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id))")    
        cursor.execute("CREATE TABLE IF NOT EXISTS subscribers (subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, " \
                       "address TEXT NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS subscriptions (subscriber_id INTEGER NOT NULL, magazine_id INTEGER NOT NULL, expiration_date TEXT NOT NULL, " \
                       "PRIMARY KEY (subscriber_id, magazine_id), " \
                       "FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id), " \
                       "FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id))")
        conn.commit()
        pub1_id = get_or_create_publisher(conn, "Acme Publishing")
        pub2_id = get_or_create_publisher(conn, "North Star Media")
        pub3_id = get_or_create_publisher(conn, "Riverbend Press")
        print(pub1_id, pub2_id, pub3_id)
        conn.commit()

        mag1_id = get_or_create_magazine(conn, "Acme Monthly", pub1_id)
        mag2_id = get_or_create_magazine(conn, "North Star Weekly", pub2_id)
        mag3_id = get_or_create_magazine(conn, "Riverbend Quarterly", pub3_id)  
        print(mag1_id, mag2_id, mag3_id)
        conn.commit()

        sub1_id = get_or_create_subscriber(conn, "John Doe", "123 Elm St")
        sub2_id = get_or_create_subscriber(conn, "Jane Smith", "456 Oak Ave")
        sub3_id = get_or_create_subscriber(conn, "Alice Johnson", "789 Pine Rd")
        print(sub1_id, sub2_id, sub3_id)
        conn.commit()


        created1 = get_or_create_subscription(conn, sub1_id, mag1_id, "2024-12-31")
        created2 = get_or_create_subscription(conn, sub1_id, mag2_id, "2024-11-30")
        created3 = get_or_create_subscription(conn, sub2_id, mag3_id, "2025-01-15")
        print(created1, created2, created3)
        conn.commit()

        cursor.execute("SELECT * FROM subscribers")
        subscribers = cursor.fetchall()
        for subscriber in subscribers:
            print(subscriber)

        cursor.execute("SELECT * FROM magazines ORDER BY name")
        magazines = cursor.fetchall()
        for magazine in magazines:
            print(magazine)

        cursor.execute(
        "SELECT magazines.name "
        "FROM magazines "
        "JOIN publishers ON magazines.publisher_id = publishers.publisher_id "
        "WHERE publishers.name = ?",
        ("Acme Publishing",)
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)




        #SQL Goes here
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS publishers (publisher_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE)")
        cursor.execute("CREATE TABLE IF NOT EXISTS magazines (magazine_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE, " \
        "publisher_id INTEGER NOT NULL, FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id))")
        cursor.execute("CREATE TABLE IF NOT EXISTS subscribers (subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, " \
        "address TEXT NOT NULL)")

        cursor.execute("CREATE TABLE IF NOT EXISTS subscriptions (subscriber_id INTEGER NOT NULL, magazine_id INTEGER NOT NULL, expiration_date TEXT NOT NULL, " \
        "PRIMARY KEY (subscriber_id, magazine_id), " \
        "FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id), " \
        "FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id))")

        print(f"Connected to database at {db_path}")
    except sqlite3.Error as e:
        print("Database connection failed.")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()
