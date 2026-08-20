rawText = 'raw_text.txt'
encryptedText = 'encrypted_text.txt'
decryptedText = 'decrypted_text.txt'
shift1 = int(input("Enter the shift value one for encryption: "))
shift2 = int(input("Enter the shift value two for encryption: "))

def encrypt_file(shift1, shift2, input_path, output_path):
    with open(input_path, 'r') as file:
        text = file.read()   
    encrypted_text = ''
    for i, char in enumerate(text):
        if char.isalpha():
            if char.islower():
                if (ord(char) - 97) <= 13:
                    encrypted_text += chr((ord(char) - 97 + (shift1 * shift2)) % 26 + 97)
                else:
                    encrypted_text += chr((ord(char) - 97 - (shift1 + shift2)) % 26 + 97)
            elif char.isupper():
                if (ord(char) - 65) <= 12:
                    encrypted_text += chr((ord(char) - 65 - shift1) % 26 + 65)
                else:
                    encrypted_text += chr((ord(char) - 65 + (shift2**2)) % 26 + 65)
            else:
                print(f"ERROR: ALPHABET CHARACTER '{char}' IS NOT UPPER OR LOWER CASE")
        elif char.isdigit():
            encrypted_text += str((int(char) + shift1-shift2)%10)
        else:
            encrypted_text += char
            continue

    
    with open(output_path, 'w') as file:
        file.write(encrypted_text)
def decrypt_file(shift1, shift2, input_path, output_path):
    with open(input_path, 'r') as file:
        text = file.read()   
    decrypted_text = ''
    for i, char in enumerate(text):
        if char.isalpha():
            if char.islower():
                if (ord(char) - 97) <= 13:
                    decrypted_text += chr((ord(char) - 97 - (shift1 * shift2)) % 26 + 97)
                else:
                    decrypted_text += chr((ord(char) - 97 + (shift1 + shift2)) % 26 + 97)
            elif char.isupper():
                if (ord(char) - 65) <= 12:
                    decrypted_text += chr((ord(char) - 65 + shift1) % 26 + 65)
                else:
                    decrypted_text += chr((ord(char) - 65 - (shift2**2)) % 26 + 65)
            else:
                print(f"ERROR: ALPHABET CHARACTER '{char}' IS NOT UPPER OR LOWER CASE")
        elif char.isdigit():
            decrypted_text += str((int(char) - shift1 + shift2)%10)
        else:
            decrypted_text += char
            continue

    
    with open(output_path, 'w') as file:
        file.write(decrypted_text)
def verify_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
        if content1 == content2:
            print("The files are identical.")
        elif content1 != content2:
            errors = 0
            for i, char in enumerate(content1):
                if i >= len(content2) or char != content2[i]:
                    errors += 1
            print(f"The files are not identical. Number of errors found: {errors}")

encrypt_file(shift1, shift2, rawText, encryptedText)
decrypt_file(shift1, shift2, encryptedText, decryptedText)
verify_files(rawText, decryptedText)