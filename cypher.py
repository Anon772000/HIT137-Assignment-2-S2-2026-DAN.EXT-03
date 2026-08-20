"""Write a program in a file named cipher.py that reads the text file raw_text.txt , 
encrypts its contents using the scheme described below, and writes the result to 
encrypted_text.txt . You must then write a function that decrypts that file, and a 
function that verifies the decryption was successful."""

import os

# Open the file in read mode using UTF-8 encoding
with open("raw_text.txt", "r", encoding="utf-8") as raw_text:
    text = raw_text.read()

# Function to display the welcome banner
def welcome_banner():
    width = 58
    print("=" * width)
    print("Encryption tool".center(width))
    print("Enter values below to begin encryption".center(width))
    print("=" * width)

# Function to handle non-negative integer input validation
def get_shift_input(prompt_text: str) -> int:
    while True:
        try:
            val = int(input(prompt_text))
            if val >= 0:
                return val  # Exit loop and return valid value
            print("That was not a non-negative integer! Please enter a number 0 or greater")
        except ValueError:
            print("That was not a non-negative integer! Please enter a number 0 or greater")

#Display welcome banner
welcome_banner()

# Get user inputs using the helper function
shift1 = get_shift_input("Enter shift1 value (non-negative integer): ")
shift2 = get_shift_input("Enter shift2 value (non-negative integer): ")

print()
print(f"Shift 1: {shift1}")
print(f"Shift 2: {shift2}")
print(text)
