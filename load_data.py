# ------------------------------
# PROJECT 3: SQL DATA ANALYSIS
# ------------------------------


# ------------------------------
# IMPORT LIBRARIES
# ------------------------------
# Required libraries for database, data handling, and output formatting
print("STARTING SCRIPT")

import sqlite3
import pandas as pd
from tabulate import tabulate   # used to display query output as tables

print("IMPORTS DONE")


# ------------------------------
# CONNECT TO SQLITE DATABASE
# ------------------------------
# Creates/opens SQLite database file
conn = sqlite3.connect("project3.db")
cursor = conn.cursor()

print("DB CONNECTED")


# ------------------------------
# LOAD DATA FROM CSV
# ------------------------------
# Read dataset from CSV file into pandas DataFrame
df = pd.read_csv("cleaned_dataset.csv")

print("CSV LOADED")


# ------------------------------
# STORE DATA INTO SQLITE TABLE
# ------------------------------
# Convert DataFrame into SQL table named 'orders'
df.to_sql("orders", conn, if_exists="replace", index=False)

print("DATA WRITTEN TO DB")


# ------------------------------
# VERIFY DATA LOAD
# ------------------------------
# Check total number of records inserted
cursor.execute("SELECT COUNT(*) FROM orders")
print("TOTAL RECORDS:", cursor.fetchone()[0])

print("DATA LOAD COMPLETE")


# ------------------------------
# FUNCTION TO EXECUTE SQL QUERIES
# ------------------------------
# Executes query, fetches results, and displays in formatted table
def run(query, label=None):

    cursor.execute(query)
    result = cursor.fetchall()

    # If no data returned
    if not result:
        print("No data found")
        return

    # Print heading for output
    if label:
        print("\n" + label)

    # Extract column names dynamically
    headers = [column[0] for column in cursor.description]

    # Trim long text to avoid messy terminal output
    cleaned_result = [
        [str(col)[:25] if isinstance(col, str) else col for col in row]
        for row in result
    ]

    # Display result in table format
    print(tabulate(cleaned_result, headers=headers, tablefmt="fancy_grid", stralign="center"))

    print("-" * 40)


# ------------------------------
# MENU SYSTEM (USER INTERFACE)
# ------------------------------
# Allows user to select different SQL analysis options
while True:

    print("\n===== SQL DATA ANALYSIS MENU =====")
    print("1. View first 10 records")
    print("2. Count total orders")
    print("3. Delivered orders")
    print("4. Sort by highest order value")
    print("5. Total revenue")
    print("6. Average order value")
    print("7. Orders by payment method")
    print("8. Revenue by product")
    print("9. Top selling products")
    print("10. Order status distribution")
    print("11. Revenue by referral source")
    print("12. Most used coupon codes")
    print("13. Average order value by product")
    print("14. Top 10 highest value orders")
    print("15. Payment methods (>5 orders)")
    print("0. Exit")

    choice = input("Enter your choice: ")


    # ------------------------------
    # BASIC DATA VIEW QUERIES
    # ------------------------------
    if choice == "1":
        run("""
        SELECT order_id, date, customer_id, product, total_price
        FROM orders
        LIMIT 10
        """, "First 10 Records")

    elif choice == "2":
        # Total number of orders in dataset
        cursor.execute("SELECT COUNT(*) FROM orders")
        print("Total Orders:", cursor.fetchone()[0])


    elif choice == "3":
        # Filter only delivered orders
        run("""
        SELECT order_id, customer_id, product, total_price, order_status
        FROM orders
        WHERE order_status='Delivered'
        """, "Delivered Orders")


    # ------------------------------
    # BUSINESS ANALYTICS QUERIES
    # ------------------------------
    
    elif choice == "4":
     run("""
     SELECT order_id, date, customer_id, product, quantity, total_price
     FROM orders
     ORDER BY total_price DESC
     """, "Sorted Orders")

    elif choice == "5":
        # Total revenue generated
        cursor.execute("SELECT SUM(total_price) FROM orders")
        print("Total Revenue:", cursor.fetchone()[0])

    elif choice == "6":
        # Average order value
        cursor.execute("SELECT AVG(total_price) FROM orders")
        print("Average Order Value:", cursor.fetchone()[0])


    # ------------------------------
    # CATEGORY ANALYSIS (GROUP BY)
    # ------------------------------
    elif choice == "7":
        run("SELECT payment_method, COUNT(*) FROM orders GROUP BY payment_method")

    elif choice == "8":
        # Revenue per product
        run("""
        SELECT product, SUM(total_price)
        FROM orders
        GROUP BY product
        ORDER BY SUM(total_price) DESC
        """)

    elif choice == "9":
        # Most sold products by quantity
        run("""
        SELECT product, SUM(quantity)
        FROM orders
        GROUP BY product
        ORDER BY SUM(quantity) DESC
        """)

    elif choice == "10":
        # Order status distribution
        run("SELECT order_status, COUNT(*) FROM orders GROUP BY order_status")


    elif choice == "11":
        # Revenue by referral source
        run("""
        SELECT referral_source, SUM(total_price)
        FROM orders
        GROUP BY referral_source
        """)


    # ------------------------------
    # ADVANCED ANALYSIS
    # ------------------------------
    elif choice == "12":
        # Most used coupon codes
        run("""
        SELECT coupon_code, COUNT(*)
        FROM orders
        WHERE coupon_code IS NOT NULL
        GROUP BY coupon_code
        """)

    elif choice == "13":
        # Average order value per product
        run("""
        SELECT product, AVG(total_price)
        FROM orders
        GROUP BY product
        """)

    elif choice == "14":
        # Top 10 highest value orders
        run("""
        SELECT order_id, customer_id, total_price
        FROM orders
        ORDER BY total_price DESC
        LIMIT 10
        """)

    elif choice == "15":
        # Payment methods used more than 5 times
        run("""
        SELECT payment_method, COUNT(*)
        FROM orders
        GROUP BY payment_method
        HAVING COUNT(*) > 5
        """)


    # ------------------------------
    # EXIT PROGRAM
    # ------------------------------
    elif choice == "0":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")


# ------------------------------
# CLOSE DATABASE CONNECTION
# ------------------------------
conn.close()