# https://aiokafka.readthedocs.io/en/stable/

from aiokafka import AIOKafkaConsumer
import asyncio

async def consume():
    consumer = AIOKafkaConsumer(
        'my_topic', 'my_other_topic',
        bootstrap_servers=' 192.168.137.225:9095'
    )
    await consumer.start()
    try:
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        await consumer.stop()

asyncio.run(consume())