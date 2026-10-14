import os
import sys

def create_workspace(folder_name):
    """Creates a dynamic workspace folder."""
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"[Success] Workspace '{folder_name}' created or already exists.")
    except OSError as e:
        print(f"[Error] Failed to create workspace: {e}")

def list_extensions(directory, extension):
    """Inspects directory structure and lists files with a targeted extension."""
    if not os.path.exists(directory):
        print(f"[Error] Directory '{directory}' does not exist.")
        return

    print(f"\nSearching for '{extension}' files in '{directory}' and its subdirectories...")
    found_files = False
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))
                found_files = True
                
    if not found_files:
        print(f"No files ending with '{extension}' found.")

def write_log(log_path, message):
    """Creates or appends to a text log using a context manager."""
    try:
        with open(log_path, 'a') as file:
            file.write(message + '\n')
        print(f"[Success] Message logged safely to '{log_path}'.")
    except IOError as e:
        print(f"[Error] Could not write to file: {e}")

def read_log(log_path):
    """Safe-reads a target text log using a context manager."""
    try:
        with open(log_path, 'r') as file:
            content = file.read()
            print(f"\n--- Reading {log_path} ---")
            print(content if content else "[File is empty]")
            print("-" * 30)
    except FileNotFoundError:
        print(f"[Error] The file '{log_path}' does not exist.")
    except IOError as e:
        print(f"[Error] Could not read file: {e}")

def display_help():
    """Displays usage instructions."""
    print("Usage: python file_manager.py [command] [arguments]")
    print("\nCommands:")
    print("  create <folder_path>                  - Create a dynamic workspace folder")
    print("  list <directory_path> <extension>     - List files with a specific extension (.txt, .py)")
    print("  writelog <file_path> \"<message>\"      - Write/append a message to a text log")
    print("  readlog <file_path>                   - Safely read a text log")

def main():
    if len(sys.argv) < 2:
        display_help()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "create" and len(sys.argv) == 3:
        create_workspace(sys.argv[2])
        
    elif command == "list" and len(sys.argv) == 4:
        list_extensions(sys.argv[2], sys.argv[3])
        
    elif command == "writelog" and len(sys.argv) == 4:
        write_log(sys.argv[2], sys.argv[3])
        
    elif command == "readlog" and len(sys.argv) == 3:
        read_log(sys.argv[2])
        
    else:
        print("[Error] Invalid command or missing arguments.")
        display_help()

if __name__ == "__main__":
    main()