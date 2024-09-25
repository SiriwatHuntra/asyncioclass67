from aiokafka.admin import AIOKafkaAdminClient, NewPartitions
import asyncio

async def add_partitions():
    admin = AIOKafkaAdminClient(bootstrap_servers='localhost:9092')
    await admin.start()
    try:
        # Check if the topic exists
        ex_topic = await admin.list_topics()
        if 'my_topic' in ex_topic:
            # Specify the new number of partitions
            new_partition_count = 3  # Example: Increase partitions to 3
            new_partitions = NewPartitions(total_count=new_partition_count)
            await admin.create_partitions({'my_topic': new_partitions})
            print(f"Partitions of 'my_topic' increased to {new_partition_count}")
        else:
            print("'my_topic' does not exist. Create it first.")
    finally:
        await admin.close()

asyncio.run(add_partitions())