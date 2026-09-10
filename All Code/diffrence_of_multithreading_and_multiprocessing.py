# # Multithreading vs Multiprocessing in Python
# # Core Difference
# # FeatureMultithreadingMultiprocessingUnitThreads (within one process)Separate processesMemoryShared memorySeparate memoryGILLimited by GILBypasses GILBest forI/O-bound tasksCPU-bound tasksOverheadLowHighCommunicationEasy (shared state)Complex (queues, pipes)Crash isolationOne thread can crash allProcesses are isolated

# # The GIL Problem
# # Python has a Global Interpreter Lock (GIL) — only one thread runs Python code at a time, even on multi-core CPUs. This makes threads ineffective for CPU-heavy work.

# # Multithreading — Best for I/O-bound tasks
# # pythonimport threading
# import requests

# def fetch(url):
#     r = requests.get(url)
#     print(f"{url} → {r.status_code}")

# urls = ["https://google.com", "https://github.com", "https://python.org"]

# threads = [threading.Thread(target=fetch, args=(u,)) for u in urls]
# for t in threads: t.start()
# for t in threads: t.join()
# Good for: API calls, file I/O, database queries, web scraping

# Multiprocessing — Best for CPU-bound tasks
# pythonfrom multiprocessing import Pool

# def square(n):
#     return n * n

# with Pool(processes=4) as pool:
#     results = pool.map(square, range(10))
#     print(results)  # [0, 1, 4, 9, 16, ...]
# ```
# Good for: **Image processing, data crunching, ML training, simulations**

# ---

# ### Quick Decision Guide
# ```
# Is your task CPU-heavy?
#     YES → Multiprocessing
#     NO  → Is it waiting on I/O (network, disk)?
#               YES → Multithreading (or asyncio)
#               NO  → Neither needed

# Bonus: asyncio — a third option
# For high-concurrency I/O (thousands of requests), asyncio is often better than threads:
# pythonimport asyncio
# import aiohttp

# async def fetch(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as r:
#             print(f"{url} → {r.status}")

# asyncio.run(fetch("https://google.com"))
# Rule of thumb: I/O-bound + many connections → asyncio, I/O-bound + simple → threading, CPU-bound → multiprocessing.