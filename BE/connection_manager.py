import sqlite3

class SQLiteConnectionManager:
    def __init__(self):
        # Connect to an in-memory SQLite database
        self.conn = sqlite3.connect(':memory:')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                candidate TEXT,
                date TEXT,
                notes TEXT
            )
        ''')
        self.conn.commit()

    def get_connection(self):
        return self.conn

    def close(self):
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    db_manager = SQLiteConnectionManager()
    conn = db_manager.get_connection()
    cursor = conn.cursor()

    # Insert a sample interview
    cursor.execute(
        "INSERT INTO interviews (candidate, date, notes) VALUES (?, ?, ?)",
        ("Alice Johnson", "2025-08-03", "Strong communication skills. Needs to improve technical depth.")
    )
    conn.commit()

    # Fetch and print all interviews
    cursor.execute("SELECT * FROM interviews")
    interviews = cursor.fetchall()
    print(interviews)  # Should print a list with one tuple

    db_manager.close()