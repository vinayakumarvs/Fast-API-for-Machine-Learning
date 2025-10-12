import time
from timeit import default_timer as timer

def run_task(name, duration):
    print(f"Task {name} starting, will take {duration} seconds.")
    time.sleep(duration)
    print(f"Task {name} completed.")

start = timer()
run_task("A", 2)
run_task("B", 3)
run_task("C", 5)
print(f"All tasks completed in {timer() - start} seconds.")