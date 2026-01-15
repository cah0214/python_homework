import sqlite3
from pathlib import Path


def main() -> None:
    # TASK 1: Complex JOINs with Aggregation
    sql = """
    SELECT
      o.order_id,
      SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON li.order_id = o.order_id
    JOIN products p ON p.product_id = li.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;
    """

    db_path = Path(__file__).parent.parent / "db" / "lesson.db"
    conn = sqlite3.connect(db_path)

    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        for order_id, total_price in rows:
            print(f"order_id={order_id} total_price=${total_price:.2f}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
