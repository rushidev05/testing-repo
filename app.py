import asyncio
from engine import AnalyticsEngine
from storage import InMemoryDB


class Application:

    def __init__(self, data):
        self.db = InMemoryDB()
        self.engine = AnalyticsEngine()
        self.data = data

    async def bootstrap(self):
        for item in self.data:
            self.db.insert(item)

        processed = self.engine.process(self.db.fetch_all())
        return processed

    async def top_user(self):
        results = await self.bootstrap()
        return sorted(results, key=lambda x: x["score"])[0]