import sqlite3
from pathlib import Path
from tkinter import INSERT


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
    conn.execute("PRAGMA foreign_keys = 1")


    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        for order_id, total_price in rows:
            print(f"order_id={order_id} total_price=${total_price:.2f}")

    
        # TASK 2: Understanding Subqueries
        print("\nTASK 2 RESULTS:")
        sql_task2 = """
    SELECT c.customer_name,
       AVG(ot.total_price) AS average_total_price
    FROM customers c
    LEFT JOIN (
    SELECT o.customer_id AS customer_id_b,
         SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON li.order_id = o.order_id
    JOIN products p ON p.product_id = li.product_id
    GROUP BY o.order_id
   ) ot ON c.customer_id = ot.customer_id_b
   GROUP BY c.customer_id
   ORDER BY c.customer_id
   LIMIT 5;
   """

        cur.execute(sql_task2)
        rows = cur.fetchall()

        for customer_name, avg_total in rows:
            print(customer_name, avg_total)
            # TASK 3: Insert Transaction Based on Data
        print("\nTASK 3 LOOKUPS:")

        sql_customer = """
        SELECT customer_id
        FROM customers
        WHERE customer_name = 'Perez and Sons';
        """
        cur.execute(sql_customer)
        customer_id = cur.fetchone()[0]

        sql_employee = """
        SELECT employee_id
        FROM employees
        WHERE first_name = 'Miranda' AND last_name = 'Harris';
        """
        cur.execute(sql_employee)
        employee_id = cur.fetchone()[0]

        sql_products = """
        SELECT product_id
        FROM products
        ORDER BY price ASC
        LIMIT 5;
        """
        cur.execute(sql_products)
        product_rows = cur.fetchall()
        product_ids = [row[0] for row in product_rows]

        print("customer_id:", customer_id)
        print("employee_id:", employee_id)
        print("product_ids:", product_ids)

        # Begin transaction
        conn.execute("BEGIN;")
        cur.execute("""
        INSERT INTO orders (customer_id, employee_id, date)
        VALUES (?, ?, ?)
        RETURNING order_id;
        """, (customer_id, employee_id, "2023-01-01"))
        order_id = cur.fetchone()[0]
        print("New order_id:", order_id)

        # Task 4: Aggregation with HAVING 

        print("\nTASK 4 RESULTS:")
        sql_task4 = """
        SELECT
           e.employee_id,
           e.first_name,
              e.last_name,
              COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON o.employee_id = e.employee_id
        GROUP BY e.employee_id, e.first_name, e.last_name
        HAVING COUNT(o.order_id) > 5
        """
        cur.execute(sql_task4)
        rows = cur.fetchall()
        for employee_id, first_name, last_name, order_count in rows:
            print(f"employee_id={employee_id} name={first_name} {last_name} order_count={order_count}")
            



    
    finally:
        conn.close()


if __name__ == "__main__":
    main()

