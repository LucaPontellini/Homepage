import time
import random
from threading import Thread, Lock, Condition

class Buffer:
    def __init__(self, size):
        self.buffer = []
        self.size = size
        self.mutex = Lock()
        self.not_full = Condition(self.mutex)
        self.not_empty = Condition(self.mutex)

    def add(self, item):
        with self.not_full:
            while len(self.buffer) >= self.size:
                self.not_full.wait()
            self.buffer.append(item)
            print(f"Prodotto: {item} | Buffer: {self.buffer}")
            self.not_empty.notify()

    def remove(self):
        with self.not_empty:
            while not self.buffer:
                self.not_empty.wait()
            item = self.buffer.pop(0)
            print(f"Consumato: {item} | Buffer: {self.buffer}")
            self.not_full.notify()
            return item

class Producer(Thread):
    def run(self):
        while True:
            item = random.randint(0, 10)
            buffer.add(item)
            time.sleep(random.uniform(0.5, 1.5))

class Consumer(Thread):
    def run(self):
        while True:
            item = buffer.remove()
            time.sleep(random.uniform(1, 2))

buffer_size = 5
buffer = Buffer(buffer_size)

producer = Producer()
consumer = Consumer()
producer.start()
consumer.start()