import os
name = os.getenv("MY_NAME", "World")
# World is the default value to return if MY_NAME is not provided. By default it is None

print(f"Hello {name} from Python")