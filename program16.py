import os
import traceback

class FileProcessingError(Exception):
    """Base custom exception for file processing errors."""
    pass


class InvalidFileFormatError(FileProcessingError):
    """Raised when the parsed file does not meet the expected structural format."""
    def __init__(self, message, line_number=None):
        super().__init__(message)
        self.line_number = line_number


def parse_data_file(filepath: str):
    """
    Safely opens, parses, and cleans up a data file using a full 
    try-except-else-finally block and custom exceptions.
    
    Input:
        filepath (str): The path to the file to be processed.
    Output:
        None: Prints parsed data or logs traceback on failure.
    """
    file_obj = None
    parsed_records = []

    print(f"\n--- Starting processing for: '{filepath}' ---")
    try:
        file_obj = open(filepath, 'r', encoding='utf-8')
        
        for line_num, line in enumerate(file_obj, start=1):
            line = line.strip()
            if not line:
                continue
                
            if '=' not in line:
                raise InvalidFileFormatError(
                    f"Missing '=' delimiter in record: '{line}'", 
                    line_number=line_num
                )
            
            key, value = line.split('=', 1)
            parsed_records.append((key.strip(), value.strip()))

    except FileNotFoundError:
        print(f"[Error] The file '{filepath}' could not be found on the system.")
        
    except InvalidFileFormatError as ife:
        print(f"[Format Error] Line {ife.line_number}: {ife}")
        print("Detailed Traceback:")
        traceback.print_exc() # Logs the full traceback to the console
        
    except Exception as e:
        print(f"[Unexpected Error] A critical runtime error occurred: {e}")
        traceback.print_exc()

    else:
        print("[Success] File parsed successfully with no errors.")
        print(f"Extracted {len(parsed_records)} records:")
        for record in parsed_records:
            print(f"  -> {record[0]}: {record[1]}")

    finally:
        if file_obj and not file_obj.closed:
            file_obj.close()
            print(f"[Cleanup] File resource '{filepath}' safely closed.")
        else:
            print(f"[Cleanup] No open file resources to close for '{filepath}'.")


def create_test_files():
    """Helper function to generate valid and invalid test files."""
    with open('valid_data.txt', 'w') as f:
        f.write("username = admin\ntheme = dark\nversion = 1.0\n")
        
    with open('invalid_data.txt', 'w') as f:
        f.write("username = guest\nmissing_delimiter_line\nversion = 2.0\n")


if __name__ == "__main__":
    create_test_files()
    parse_data_file("non_existent_file.txt")
    parse_data_file("valid_data.txt")
    parse_data_file("invalid_data.txt")

    if os.path.exists('valid_data.txt'): os.remove('valid_data.txt')
    if os.path.exists('invalid_data.txt'): os.remove('invalid_data.txt')