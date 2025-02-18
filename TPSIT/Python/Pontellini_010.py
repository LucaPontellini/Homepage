import random
import threading
import time
import os

class Buffer:
    def __init__(self):
        self.areaCondivisa = 0
        self.produttore_lock = threading.Lock()
        self.consumatore_lock = threading.Lock()
        self.consumatore_lock.acquire()

    def get_dato(self, name):
        self.consumatore_lock.acquire()
        dato = self.areaCondivisa
        print(f'{name} ha consumato il dato: {dato}')
        self.produttore_lock.release()
        return dato
        
    def set_dato(self, dato, name):
        self.produttore_lock.acquire()
        self.areaCondivisa = dato
        print(f'{name} ha prodotto il dato: {dato}')
        self.consumatore_lock.release()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def produttore(buffer, name):
    while True:
        dato = random.randint(1, 100)
        buffer.set_dato(dato, name)
        time.sleep(5)
        clear_terminal()

def consumatore(buffer, name):
    while True:
        buffer.get_dato(name)
        time.sleep(5)
        clear_terminal()

if __name__ == "__main__":
    buffer = Buffer()
    
    produttore_thread = threading.Thread(target=produttore, args=(buffer, 'Produttore'))
    consumatore_thread = threading.Thread(target=consumatore, args=(buffer, 'Consumatore'))
    
    produttore_thread.start()
    consumatore_thread.start()
    
    produttore_thread.join()
    consumatore_thread.join()