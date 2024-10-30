import multiprocessing
import time
import random
from datetime import datetime

def print_time():
    # Wait for a random number of seconds
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    
    # Print the current time
    print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} after waiting {wait_time:.2f} seconds")

if __name__ == "__main__":
    processes = []
    
    # Create three separate processes
    for _ in range(3):
        p = multiprocessing.Process(target=print_time)
        processes.append(p)
        p.start()
    
    # Wait for all processes to finish
    for p in processes:
        p.join()
