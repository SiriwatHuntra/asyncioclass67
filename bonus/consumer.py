# https://aiokafka.readthedocs.io/en/stable/

from aiokafka import AIOKafkaConsumer
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

async def consume():

    consumer = AIOKafkaConsumer(
        'my_topic', 'my_other_topic',
        bootstrap_servers='localhost:9094',
        group_id="my-group")
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

async def main():
    await new_topic()
    await consume()

asyncio.run(main())