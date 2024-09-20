# https://aiokafka.readthedocs.io/en/stable/

from aiokafka.admin import AIOKafkaAdminClient, NewTopic
import asyncio

async def new_topic():
    admin = AIOKafkaAdminClient(bootstrap_servers='localhost:9092')
    await admin.start()
    try:
       ex_topic = await admin.list_topics()
       if 'my_topic' not in ex_topic:
           topic = NewTopic(name='my_topic', num_partitions=3, replication_factor=3)
           await admin.create_topics([topic])
           print(f"create topic with partition = {3} replication = {3} ")
    finally:
        await admin.close()


asyncio.run(new_topic())
