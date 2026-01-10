import sqlite3
from pathlib import Path

def main():
    db_path = Path(__file__).parent.parent / "db" / "magazines.db"
    try:
        conn = sqlite3.connect(db_path)
        print(f"Connected to database at {db_path}")
    except sqlite3.Error as e:
        print("Database connection failed.")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()
