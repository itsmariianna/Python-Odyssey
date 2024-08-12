# Create a decorator that adds retry logic to a function. The decorator should retry the function a specified number of times if it raises an exception. Apply this decorator to a function that reads data from a file.

import time 

def retry(delay):
  def limit_funtion(limit):
    def decorator(fn):
      def wrapper(*args, **kwargs):
        for i in range(limit):
          try:
            return fn(*args, **kwargs)
          except Exception as e:
            print(f"Function can't be executed {i + 1} time, trying execute after {delay}")
            time.sleep(delay)
        raise ValueError("Function can't  be executed anymore")
      return wrapper
    return decorator
  return limit_funtion

arg = int(input("Enter retry limit: "))


@retry(1)
def read_file(file_path):
  fs = open(file_path)
  return fs.read()

try:
  read_file('fil.txt')
except ValueError as e:
  print(e)