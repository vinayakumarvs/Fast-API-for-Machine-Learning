import asyncio
from timeit import default_timer as timer

async def run_task(name, duration):
    print(f"Task {name} starting, will take {duration} seconds.")
    await asyncio.sleep(duration)
    print(f"Task {name} completed.")

async def main():
    start = timer()
    await asyncio.gather(
        run_task("A", 2),
        run_task("B", 3),
        run_task("C", 5)
    )
    print(f"All tasks completed in {timer() - start} seconds.")

if __name__ == "__main__":
    asyncio.run(main())