import sqlite3

def main():
    conn = sqlite3.connect("school_a.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    # Database tables will be created here

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
