import sqlite3

class SQLiteDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('Vocabulary-learn/profile/vocabulary.sqlite3')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def fetch_all(self, query: str, params: tuple = ()) -> list:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self) -> None:
        self.connection.close()

if __name__ == "__main__":
    db = SQLiteDatabase()
    # Example usage
    db.cursor.execute("""CREATE TABLE IF NOT EXISTS unit(
        unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
        unit_name TEXT NOT NULL,
        description TEXT NOT NULL
    )""")
    db.cursor.execute("""CREATE TABLE IF NOT EXISTS vocabulary(
        vocabulary TEXT NOT NULL,
        unit_id INTEGER NOT NULL,
        description TEXT NOT NULL
    )""")
    db.close()