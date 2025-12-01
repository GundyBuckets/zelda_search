class DatabaseManager:
    def __init__(self):
        self.database_path = "/database.db"
        self.connection = None

    def connect(self):
        # Logic to connect to the database
        print(f"Connecting to database at {self.database_path}")
        # Example: self.connection = some_database_library.connect(self.database_url)
        self.connection = 

    def disconnect(self):
        # Logic to disconnect from the database
        if self.connection:
            print("Disconnecting from the database")
            # Example: self.connection.close()
            self.connection = None

    def execute_query(self, query):
        # Logic to execute a query
        if not self.connection:
            raise Exception("Database not connected")
        print(f"Executing query: {query}")
        # Example: return self.connection.execute(query)

    def fetch_results(self, query):
        # Logic to fetch results from a query
        if not self.connection:
            raise Exception("Database not connected")
        print(f"Fetching results for query: {query}")
        # Example: return self.connection.execute(query).fetchall()