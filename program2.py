import sys

def process_cipher(text, shift, mode):
    """Encodes or decodes text using the Caesar cipher technique."""
    result = ""
    
    if mode == 'decode':
        shift = -shift

    for char in text:
        if char.isalpha():
            start_ascii = ord('A') if char.isupper() else ord('a')
            shifted_ascii = (ord(char) - start_ascii + shift) % 26 + start_ascii
            result += chr(shifted_ascii)
        else:
            result += char
            
    return result

def main():
    if len(sys.argv) == 4:
        mode = sys.argv[1].lower()
        text = sys.argv[2]
        shift_input = sys.argv[3]
    else:
        print("--- Interactive Caesar Cipher ---")
        mode = input("Choose mode ('encode' or 'decode'): ").strip().lower()
        text = input("Enter the message: ")
        shift_input = input("Enter the shift key (integer): ").strip()

    if mode not in ['encode', 'decode']:
        print("Error: Mode must be either 'encode' or 'decode'.")
        sys.exit(1)
        
    if not shift_input.lstrip('-').isdigit():
        print("Error: The shift key must be a valid whole number.")
        sys.exit(1)

    shift = int(shift_input)
    output_message = process_cipher(text, shift, mode)
    
    print("\n--- Result ---")
    print(output_message)

if __name__ == "__main__":
    main()