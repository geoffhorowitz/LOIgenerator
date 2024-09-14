import os
import sqlite3
import json

# Database initialization (you can run this once to set up the table)
def init_db(db_path, table_name='user_data'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {user_data} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            data TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Save user responses to the SQLite database
def save_to_db(db_path: str, user_id: str, data: dict):
    # Check if the database file exists
    if not os.path.exists(db_path):
        print("Database doesn't exist. Initializing the database...")
        init_db(db_path)  # Call the function to create the database and tables

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f'''
        INSERT INTO user_data (user_id, data)
        VALUES (?, ?)
    ''', (user_id, json.dumps(data)))  # Store data as a JSON string
    conn.commit()
    conn.close()



def read_sqlite_database(db_file, table_name=None):
    """Reads a SQLite database and returns a list of rows.

    Args:
        db_file (str): The path to the SQLite database file.
        table_name(str): sql table name.

    Returns:
        list: A list of rows containing data from the database.
    """

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Replace with your desired SQL query
        query = "SELECT * FROM your_table_name"

        if table_name:
            # If a table name is provided, read only that table
            cursor.execute(f"SELECT * FROM {table_name};")
            table_data = cursor.fetchall()
            results = table_data
        else:
            # Get a list of all table names
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

            results = []
            for table_name, in tables:
                cursor.execute(f"SELECT * FROM {table_name};")
                table_data = cursor.fetchall()
                results.append({table_name: table_data})

        return results

    except sqlite3.Error as e:
        print("Error connecting to the database:", e)
        return []

    finally:
        conn.close()

if __name__ == "__main__":
    # Example usage
    db_path = "./database/loi_app.db"
    table_name = 'user_data'
    results = read_sqlite_database(db_path, table_name)

    # Print the results
    for row in results:
        print(row)