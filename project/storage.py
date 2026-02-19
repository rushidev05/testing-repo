class InMemoryDB:

    def __init__(self):
        self.data = {}

    def insert(self, record):
        self.data[record["id"]] = record

    def fetch_all(self):
        return self.data
