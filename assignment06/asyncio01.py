import asyncio

class AsyncDatabaseConection:
    def __init__(self, db_name):
        self.db_name = db_name
    
    async def __aenter__(self):
        print(f'Connecting to the database {self.db_name}...')
        await asyncio.sleep(1) #simulate connection process
        print(f"Connect to the database {self.db_name}.")
    
    async def __aexit_(self, exec_type, exc, tb):
        print(f"Closing the database connection to {self.db_name}.")
        await asyncio.sleep(1) #simulate teardown process
        print(f"Closed the database connection to {self.db_name}.")
        if exc:
            print(f"An exception occurred: {exc}")

    async def fetsh_data(self):
        await asyncio.sleep(1) #simulate asycn data fetch
        return {"data" : "sample data"}
    
async def main():
    async with AsyncDatabaseConection("test_db") as db:
        data = await db.fetch_data()
        print(f'Fetch data: {data}')

asyncio.run(main())