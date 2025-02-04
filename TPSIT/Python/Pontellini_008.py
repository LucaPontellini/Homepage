import threading

def fibonacci(n, risultato):
    if n == 0 or n == 1:
        risultato[n] = 1
    else:
        risultato[n] = risultato[n-1] + risultato[n-2]

def fibonacci_threaded(n):
    risultato = [0] * (n + 1)
    threads = []

    def thread_function(start, step):
        for i in range(start, n + 1, step):
            if i == 0 or i == 1:
                risultato[i] = 1
            else:
                risultato[i] = risultato[i-1] + risultato[i-2]

    thread_even = threading.Thread(target=thread_function, args=(0, 2))
    thread_odd = threading.Thread(target=thread_function, args=(1, 2))

    threads.append(thread_even)
    threads.append(thread_odd)

    thread_even.start()
    thread_odd.start()

    for thread in threads:
        thread.join()

    return risultato

def main():
    n = int(input("Inserisci il valore di n: "))
    sequenza_fib = fibonacci_threaded(n)
    print(f"Sequenza di Fibonacci fino a {n}: {sequenza_fib}")

    fib_string = ''.join(map(str, sequenza_fib))
    print(f"Sequenza di Fibonacci come stringa: {fib_string}")

if __name__ == "__main__":
    main()