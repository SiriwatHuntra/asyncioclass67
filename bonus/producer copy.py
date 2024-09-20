# https://aiokafka.readthedocs.io/en/stable/

from aiokafka import AIOKafkaProducer
import asyncio

async def send_messages():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9093')
    await producer.start()
    try:
        for counter in range(10):
            message = f"Super message from producer1 {counter}".encode('utf-8')
            await producer.send_and_wait("my_topic", message)
            print(f"Sent: {message.decode('utf-8')}")
            counter += 1
            await asyncio.sleep(1)  # Wait for 3 seconds before sending the next message
    finally:
        await producer.stop()


asyncio.run(send_messages())