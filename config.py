import os

DEFAULT_POSTGRESQL_PATH = r"D:\Program Files\PostgreSQL\17\bin"

def POSTGRESQL_PATH_FINDER():
    # Prompt user for custom path or use default
    user_input = input(f"Enter the PostgreSQL bin directory or press Enter to use the default ({DEFAULT_POSTGRESQL_PATH}): ")

    # Use default path if user input is empty
    postgresql_path = user_input.strip() if user_input else DEFAULT_POSTGRESQL_PATH

    # Check if the path is already in the system PATH, if not, add it
    if postgresql_path not in os.environ['PATH']:
        os.environ['PATH'] += f";{postgresql_path}"

    print(f"PostgreSQL bin directory is set to: {postgresql_path}")
