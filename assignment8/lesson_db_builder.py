import sqlite3
from pathlib import Path

def main():
    db_path = Path(__file__).parent.parent / "db" / "lesson.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # SQL goes here

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
