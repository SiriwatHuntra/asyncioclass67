from aiokafka import AIOKafkaProducer
import asyncio

async def send_one():
    # Initialize the producer with the Kafka broker address
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9093'
    )
    # Start the producer to get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Send a message to the specified topic
        await producer.send_and_wait("my_topic", b"Super message")
    finally:
        # Stop the producer and wait for all pending messages to be delivered or expire
        await producer.stop()

# Run the asynchronous function
asyncio.run(send_one())
