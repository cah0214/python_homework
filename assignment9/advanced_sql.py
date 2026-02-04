import sqlite3
from pathlib import Path

def main() -> None:
    # Path to database
    db_path = Path(__file__).parent.parent / "db" / "lesson.db"
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = 1")
    
    try:
        cur = conn.cursor()

        # ------------------------
        # TASK 1: Complex JOINs with Aggregation
        # ------------------------
        sql_task1 = """
        SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li ON li.order_id = o.order_id
        JOIN products p ON p.product_id = li.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5;
        """
        cur.execute(sql_task1)
        rows = cur.fetchall()
        print("TASK 1 RESULTS:")
        for order_id, total_price in rows:
            print(f"order_id={order_id} total_price=${total_price:.2f}")

        # ------------------------
        # TASK 2: Understanding Subqueries
        # ------------------------
        print("\nTASK 2 RESULTS:")
        sql_task2 = """
        SELECT c.customer_name,
               AVG(sub.total_price) AS average_total_price
        FROM customers c
        LEFT JOIN (
            SELECT o.customer_id AS customer_id_b,
                   SUM(p.price * li.quantity) AS total_price
            FROM orders o
            JOIN line_items li ON li.order_id = o.order_id
            JOIN products p ON p.product_id = li.product_id
            GROUP BY o.order_id
        ) sub
        ON c.customer_id = sub.customer_id_b
        GROUP BY c.customer_id
        ORDER BY c.customer_id
        LIMIT 5;
        """
        cur.execute(sql_task2)
        rows = cur.fetchall()
        for customer_name, avg_total in rows:
            if avg_total is not None:
                print(f"{customer_name}: ${avg_total:.2f}")
            else:
                print(f"{customer_name}: $0.00")

        # ------------------------
        # TASK 3: Insert Transaction Based on Data
        # ------------------------
        print("\nTASK 3 LOOKUPS AND INSERTS:")

        # Get customer_id
        cur.execute("SELECT customer_id FROM customers WHERE customer_name = ?", ("Perez and Sons",))
        customer_id = cur.fetchone()[0]

        # Get employee_id
        cur.execute("SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?", ("Miranda", "Harris"))
        employee_id = cur.fetchone()[0]

        # Get 5 least expensive product_ids
        cur.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
        product_ids = [row[0] for row in cur.fetchall()]

        print("customer_id:", customer_id)
        print("employee_id:", employee_id)
        print("product_ids:", product_ids)

        # Begin transaction for order and line_items
        try:
            conn.execute("BEGIN;")

            # Insert order
            cur.execute("""
                INSERT INTO orders (customer_id, employee_id, order_date)
                VALUES (?, ?, CURRENT_DATE)
                RETURNING order_id;
            """, (customer_id, employee_id))
            order_id = cur.fetchone()[0]
            print("New order_id:", order_id)

            # Insert 5 line_items
            for pid in product_ids:
                cur.execute("""
                    INSERT INTO line_items (order_id, product_id, quantity)
                    VALUES (?, ?, ?)
                """, (order_id, pid, 10))

            # Commit transaction
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("Task 3 transaction failed:", e)

        # Verify inserted line_items
        cur.execute("""
            SELECT li.line_item_id, li.quantity, p.product_name
            FROM line_items li
            JOIN products p ON li.product_id = p.product_id
            WHERE li.order_id = ?
        """, (order_id,))
        rows = cur.fetchall()
        print("\nInserted line_items for the new order:")
        for line_item_id, qty, product_name in rows:
            print(f"line_item_id={line_item_id} quantity={qty} product={product_name}")

        # ------------------------
        # TASK 4: Aggregation with HAVING
        # ------------------------
        print("\nTASK 4 RESULTS:")
        sql_task4 = """
        SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON o.employee_id = e.employee_id
        GROUP BY e.employee_id, e.first_name, e.last_name
        HAVING COUNT(o.order_id) > 5
        ORDER BY order_count DESC;
        """
        cur.execute(sql_task4)
        rows = cur.fetchall()
        for employee_id, first_name, last_name, order_count in rows:
            print(f"employee_id={employee_id} name={first_name} {last_name} order_count={order_count}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
# End of advanced_sql.py
