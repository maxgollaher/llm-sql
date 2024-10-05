import mysql.connector
import config


class DB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DB, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'connection'):
            self.connection = mysql.connector.connect(
                host="localhost",
                user=config.MYSQL_USER,
                password=config.MYSQL_PASSWORD,
                database='llm-sql'
            )
            self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def execute(self, query=None, path=None):
        results = []
        if path:
            with open(path, 'r') as file:
                query = file.read()
        commands = query.split(';')
        for command in commands:
            command = command.strip()
            if not command:
                continue
            try:
                self.cursor.execute(command)
                if 'SELECT' in command:
                    results.append(self.cursor.fetchall())
                else:
                    self.connection.commit()
            except Exception as ex:
                results.append(f"Error: {ex}")
                self.connection.rollback()
        return results

    def create_tables(self):
        self.execute(path="sql/create-database.sql")
        self.execute(path="sql/populate-tables.sql")
        self.connection.commit()


if __name__ == '__main__':
    db = DB()
    db.create_tables()

    tables = db.execute("SELECT * from User;"
                        "SELECT * from Item;"
                        "SELECT * from Transaction;")
    for table in tables:
        [print(row) for row in table]
        print()
