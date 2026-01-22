import sqlite3 
import pandas as pd
from pathlib import Path

def main():
    db_path = Path(__file__).parent.parent / "db" / "lesson.db"
    conn = sqlite3.connect(db_path)
    SQL = """
    SELECT
        line_item.lineitem_id,
        line_item.order_id,
        line_item.product_id,
        line_item.quantity,
        product.name AS product_name,
        product.price AS product_price
    FROM lineitem
    JOIN product 
    ON line_item.product_id = product.product_id
    """

    df = pd.read_sql_query(SQL, conn)
    print(df.head())
    conn.close()


if __name__ == "__main__":
    main()
