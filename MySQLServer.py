#!/usr/bin/python3
"""
MySQLServer.py
Creates the database alx_book_store if it does not already exist.

Constraints:
- Must not use SELECT or SHOW statements.
- Must print success message when created successfully.
- Must print error message on connection failures.
- Must handle open/close properly.
"""

import os
import sys

import mysql.connector
from mysql.connector import Error


def main() -> None:
    host = os.getenv("MYSQL_HOST", "localhost")
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "")
    port = int(os.getenv("MYSQL_PORT", "3306"))

    conn = None
    cursor = None

    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
        )
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        # If we got here without exception, consider it successful.
        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}", file=sys.stderr)

    finally:
        try:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()
