# task 4: Write a custom context manager class using __enter__ and __exit__ that logs when a block starts and ends.

class Logger:
    def __enter__(self):
        print("Block has started")
    
    def __exit__(self, type, value, traceback):
        print("Block has exited")

with Logger():
    print("This is inside the block")