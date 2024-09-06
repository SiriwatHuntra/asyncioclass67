import time
import asyncio
from asyncio import Queue
from random import randrange

# we first implement the Customer and Product classes, 
# representing customers and products that need to be checked out. 
# The Product class has a checkout_time attribute, 
# which represents the time required for checking out the product.
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.produsts = products

# we implement a checkout_customer method that acts as a consumer.
# As long as there is data in the queue, this method will continue to loop. 
# During each iteration, it uses a get method to retrieve a Customer instance. 
# 
# If there is no data in the queue, it will wait. 
# 
# After retrieving a piece of data (in this case, a Customer instance), 
# it iterates through the products attribute and uses asyncio.sleep to simulate the checkout process.
# 
# After finishing processing the data, 
# we use queue.task_done() to tell the queue that the data has been successfully processed.
async def checkout_customer(queue: Queue, cashier_number: int):
    total_time = 0.0
    customer_count = 0
    while not queue.empty():
        customer: Customer = await queue.get()
        customer_start_time = time.perf_counter()
        print(f"The Cashier-{cashier_number} "
              f"Will checkout Customer_{customer.customer_id} ")
        for product in customer.produsts:
            print (f"The Cashier_{cashier_number} "
                   f"Will checkout Customer_{customer.customer_id}'s  "
                   f"Product_{product.product_name} "
                   f"in {product.checkout_time} secs ")
            await asyncio.sleep(product.checkout_time)
        print(f'The Cashier_{cashier_number} '
              f'Finish chackout Customer_{customer.customer_id} '
              f"in {round(time.perf_counter() - customer_start_time, ndigits = 2)} secs ")

        queue.task_done()
        customer_count += 1
        total_time += time.perf_counter() - customer_start_time
    return total_time, customer_count

# we implement the generate_customer method as a factory method for producing customers.
#
# We first define a product series and the required checkout time for each product. 
# Then, we place 0 to 4 products in each customer’s shopping cart.
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

# we implement the customer_generation method as a producer. 
# This method generates several customer instances regularly 
# and puts them in the queue. If the queue is full, the put method will wait.
async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id)
                     for the_id in range(customer_count, customer_count + customers)]

        for customer in customers:
            print("waiting to put customer in line...")
            await queue.put(customer)
            print('Customer put in line...')
        customer_count = customer_count + len(customers)
        await asyncio.sleep(.001)
        return customer_count

# Finally, we use the main method to initialize the queue, 
# producer, and consumer, and start all concurrent tasks.
async def main():
    customer_queue = Queue(3)
    customers_start_time = time.perf_counter()
    customer_producer = asyncio.create_task(customer_generation(customer_queue, 10))
    cashier  = [checkout_customer(customer_queue, the_id) for the_id in range(5)]
    result = await asyncio.gather(customer_producer, *cashier)

    for i, (total_time, customer_count) in enumerate(result[1:]):
        print(f"Cashier {i} checked out {customer_count} customers in {total_time:.2f} seconds")

    print(f"the super market process finished "
          f"{customer_producer.result()} customers "
          f"in {round(time.perf_counter() - customers_start_time, ndigits = 2)} secs")

if __name__ == "__main__":
    asyncio.run(main())

