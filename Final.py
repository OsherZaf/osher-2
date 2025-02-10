import platform
import os
import subprocess
import time
import psutil

# Exercise 1: Display system information
def display_system_info():
    # System name and version
    system_name = platform.system()  # Windows or Linux
    system_version = platform.version()
    architecture = platform.architecture()[0]  # 32-bit or 64-bit

    print(f"System Information:")
    print(f"Operating System: {system_name}")
    print(f"Version: {system_version}")
    print(f"Architecture: {architecture}")
    
    if system_name == "Linux":
        # For Linux, get CPU details
        cpu_info = subprocess.getoutput("lscpu")
        print(f"CPU Information:\n{cpu_info}")
    elif system_name == "Windows":
        # For Windows, get CPU details
        cpu_info = subprocess.getoutput("wmic cpu get caption")
        print(f"CPU Information:\n{cpu_info}")
    else:
        print("Unknown system")

# Exercise 2: Check file permissions
def check_file_permissions():
    file_path = input("Enter the file path: ")

    # Check if the file exists
    if not os.path.exists(file_path):
        print("The file does not exist.")
        return

    # Check if the file is readable
    is_readable = os.access(file_path, os.R_OK)
    # Check if the file is writable
    is_writable = os.access(file_path, os.W_OK)
    # Check if the file is executable
    is_executable = os.access(file_path, os.X_OK)

    print(f"Permissions for {file_path}:")
    print(f"Readable: {'Yes' if is_readable else 'No'}")
    print(f"Writable: {'Yes' if is_writable else 'No'}")
    print(f"Executable: {'Yes' if is_executable else 'No'}")

# Exercise 3: Calculate directory size
def calculate_directory_size(): 
    directory_path = input("Enter the directory path: ")

    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print("The directory does not exist.")
        return
    
    total_size = 0
    # Traverse through all files and directories in the given directory
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Add the file size to the total size
            total_size += os.path.getsize(file_path)

    # Convert the size from bytes to MB
    total_size_mb = total_size / (1024 * 1024)
    print(f"Total size of directory {directory_path}: {total_size_mb:.2f} MB")

# Exercise 4: Edit environment variable
def edit_environment_variable():
    print("Choose an option:")
    print("1. Add a new environment variable")
    print("2. Update an existing environment variable")
    print("3. Delete an environment variable")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        # Add a new environment variable
        var_name = input("Enter the name of the variable: ")
        var_value = input("Enter the value of the variable: ")
        os.environ[var_name] = var_value
        print(f"Environment variable {var_name} added successfully!")
        print(f"Value: {os.environ[var_name]}")        
    
    elif choice == "2":
        # Update an existing environment variable
        var_name = input("Enter the name of the variable to update: ")
        if var_name in os.environ:
            var_value = input("Enter the new value of the variable: ")
            os.environ[var_name] = var_value
            print(f"Environment variable {var_name} updated successfully!")
        else:
            print(f"The environment variable {var_name} does not exist.")
    
    elif choice == "3":
        # Delete an environment variable
        var_name = input("Enter the name of the variable to delete: ")
        if var_name in os.environ:
            del os.environ[var_name]
            print(f"Environment variable {var_name} deleted successfully!")
        else:
            print(f"The environment variable {var_name} does not exist.")
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# Exercise 5: Count files and directories
def count_files_and_directories():
    """This function checks how many files or directories are in a given directory"""
    dir_path = input("Enter the directory path: ")

    # Check if the provided path is a valid directory
    if not os.path.isdir(dir_path):
        print(f"The path {dir_path} is not a valid directory.")
        return

    total_files = 0
    total_directories = 0

    # Scan the current directory only
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):
            total_files += 1
        elif os.path.isdir(item_path):
            total_directories += 1

    print(f"Total number of files: {total_files}")
    print(f"Total number of subdirectories: {total_directories}")

# Exercise 6: Ping hosts
def ping_hosts():
    hosts = input("Enter one or more hostnames (comma-separated): ").split(',')

    for host in hosts:
        host = host.strip()  # Remove extra spaces
        param = "-n" if platform.system().lower() == "windows" else "-c"  # Adjust for the OS
        command = ["ping", param, "1", host]  # Ping command

        try:
            output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if output.returncode == 0:
                print(f"{host} is reachable.")
            else:
                print(f"{host} is NOT reachable.")
        except Exception as e:
            print(f"Error pinging {host}: {e}")

# Exercise 7: Exit program
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

# Exercise 8: Display system uptime
def display_system_uptime():
    uptime_seconds = time.time() - psutil.boot_time()  # Uptime in seconds
    uptime_hours = uptime_seconds // 3600  # Convert to hours
    uptime_minutes = (uptime_seconds % 3600) // 60  # Convert to minutes
    print(f"System uptime: {int(uptime_hours)} hours, {int(uptime_minutes)} minutes")

# Running all functions
display_system_info()
check_file_permissions()
calculate_directory_size()
edit_environment_variable()
count_files_and_directories()
ping_hosts()
exit_program()
display_system_uptime()
