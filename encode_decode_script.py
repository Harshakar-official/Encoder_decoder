import base64
import urllib.parse
import os
import codecs
import time
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# Cool ASCII Art Header
def print_banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "    🚀 Advanced Text Encoder & Decoder  🚀")
    print(Fore.CYAN + "=" * 50 + "\n")

# Encoding Functions
def b64_encode(text):
    return base64.b64encode(text.encode()).decode()

def b64_decode(text):
    return base64.b64decode(text).decode()

def utf16_encode(text):
    return text.encode("utf-16").decode("latin1")

def utf16_decode(text):
    return text.encode("latin1").decode("utf-16")

def url_encode(text):
    return urllib.parse.quote(text)

def url_decode(text):
    return urllib.parse.unquote(text)

def hex_encode(text):
    return text.encode().hex()

def hex_decode(text):
    try:
        return bytes.fromhex(text).decode()
    except ValueError:
        return Fore.RED + "❌ Invalid Hex input" + Style.RESET_ALL

def rot13_encode(text):
    return codecs.encode(text, 'rot_13')

def rot13_decode(text):
    return codecs.encode(text, 'rot_13')  # Encoding & Decoding are identical in ROT13


# Available operations dictionary
operations = {
    "1": ("Base64 Encode", b64_encode),
    "2": ("Base64 Decode", b64_decode),
    "3": ("UTF-16 Encode", utf16_encode),
    "4": ("UTF-16 Decode", utf16_decode),
    "5": ("URL Encode", url_encode),
    "6": ("URL Decode", url_decode),
    "7": ("Hex Encode", hex_encode),
    "8": ("Hex Decode", hex_decode),
    "9": ("ROT13 Encode", rot13_encode),
    "10": ("ROT13 Decode", rot13_encode)
}

# Function to process file
def process_file(file, mode):
    if mode not in operations:
        print(Fore.RED + "❌ Invalid selection. Please choose a valid number!" + Style.RESET_ALL)
        return

    operation_name, function = operations[mode]

    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        
        print(Fore.BLUE + f"\n🔄 Processing {operation_name}...\n")
        time.sleep(1)  # Fake loading effect
        
        result = function(content)

        output_file = f"{os.path.splitext(file)[0]}_{operation_name.replace(' ', '_')}.txt"
        with open(output_file, "w", encoding="utf-8") as out:
            out.write(result)

        print(Fore.GREEN + f"\n✅ Successfully processed! Output saved to: {output_file}\n")
    except Exception as e:
        print(Fore.RED + f"\n❌ Error processing file: {e}\n")

# Main Function
if __name__ == "__main__":
    try:
        while True:
            print_banner()
            file = input(Fore.CYAN + "📂 Enter file path: " + Style.RESET_ALL)

            print("\n" + Fore.YELLOW + "🎯 Choose an operation:" + Style.RESET_ALL)
            for key, (name, _) in operations.items():
                print(Fore.LIGHTCYAN_EX + f"[{key}] {name}" + Style.RESET_ALL)

            mode = input(Fore.CYAN + "\n➡ Enter your choice (1-10): " + Style.RESET_ALL)
            process_file(file, mode)

            another = input(Fore.MAGENTA + "🔄 Do you want to process another file? (y/n): " + Style.RESET_ALL).lower()
            if another != 'y':
                print(Fore.GREEN + "\n👋 Exiting... Have a great day!\n")
                break

    except KeyboardInterrupt:
        print(Fore.RED + "\n\n🔴 Process interrupted. Goodbye!\n")
