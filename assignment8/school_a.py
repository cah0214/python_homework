import sqlite3

def get_or_create_publisher(conn, name):
    cursor = conn.cursor()
    cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (name,))
    row = cursor.fetchone()
    if row:
        return row[0]
    cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    return cursor.lastrowid

def get_or_create_magazine(conn, name, publisher_id):
    cursor = conn.cursor()
    cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (name,))
    row = cursor.fetchone()
    if row:
        return row[0]
    cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
    return cursor.lastrowid

def get_or_create_subscriber(conn, name, address):
    cursor = conn.cursor()
    cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", (name, address))
    row = cursor.fetchone()
    if row:
        return row[0]
    cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    return cursor.lastrowid

def get_or_create_subscription(conn, subscriber_id, magazine_id):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
        (subscriber_id, magazine_id)
    )
    if cursor.fetchone():
        return False
    cursor.execute(
        "INSERT INTO subscriptions (subscriber_id, magazine_id) VALUES (?, ?)",
        (subscriber_id, magazine_id)
    )
    return True

def main():
    conn = sqlite3.connect("school_a.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            PRIMARY KEY (subscriber_id, magazine_id),
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
        )
    """)

    pub1_id = get_or_create_publisher(conn, "Acme Publishing")
    pub2_id = get_or_create_publisher(conn, "North Star Media")
    pub3_id = get_or_create_publisher(conn, "Riverbend Press")
    print(pub1_id, pub2_id, pub3_id)

    mag1_id = get_or_create_magazine(conn, "Warehouse Weekly", pub1_id)
    mag2_id = get_or_create_magazine(conn, "Supply Chain Today", pub1_id)
    mag3_id = get_or_create_magazine(conn, "Tech Monthly", pub2_id)
    print(mag1_id, mag2_id, mag3_id)

    sub1_id = get_or_create_subscriber(conn, "Crystal Hoefener", "741 Barbados Dr Apt 3 Indianapolis, IN 46227")
    sub2_id = get_or_create_subscriber(conn, "Brayden Hoefener", "Indianapolis, IN")
    sub3_id = get_or_create_subscriber(conn, "Wyatt Hoefener", "Indianapolis, IN")
    print("Subscribers:", sub1_id, sub2_id, sub3_id)

    get_or_create_subscription(conn, sub1_id, mag1_id)
    get_or_create_subscription(conn, sub1_id, mag3_id)
    get_or_create_subscription(conn, sub2_id, mag2_id)
    get_or_create_subscription(conn, sub3_id, mag1_id)
    print("Subscriptions created (some may already exist).")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
