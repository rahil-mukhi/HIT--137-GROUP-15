# Opens the raw text file "raw_text.txt" in the read mode and reads the text file
text = open("raw_text.txt", "r")
data = text.read()  # Read the content of the file
print("Original Text :", data)  # Prints the original text to verify

# Takes input from the user for encryption parameters n and m
n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))


# Function for the encryption of input text
def encrypt(data, n, m):
    encrypted_text = ""  # string to store the encrypted text
    for char in data:
        if char.isalpha():  # Only alphabetic characters are processed
            if char.islower():
                if ord("a") <= ord(char) <= ord("m"):  # First part of the alphabet (a-m)
                    encrypted_char = chr((ord(char) + (n * m) - ord("a")) % 13 + ord("a"))
                else:  # Second part of the alphabet (n-z)
                    encrypted_char = chr((ord(char) - (n + m) - ord("n")) % 13 + ord("n"))
            else:
                if ord("A") <= ord(char) <= ord("M"):

                    encrypted_char = chr((ord(char) - n - ord("A")) % 13 + ord("A"))
                else:
                    encrypted_char = chr((ord(char) + (m ** 2) - ord("N")) % 13 + ord("N"))
        else:  # Non-alphabetic characters remain unchanged
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text  # Returns the final encrypted text


# Function to decrypt the encrypted text
def decrypt(encrypted_data, n, m):
    decrypted_text = ""  # String to store the decrypted text
    for i in range(len(encrypted_data)):
        char = encrypted_data[i]
        if char.isalpha():  # Only alphabetic characters are processed
            if char.islower():
                if ord("a") <= ord(char) <= ord("m"):
                    decrypted_char = chr((ord(char) - (n * m) - ord("a")) % 13 + ord("a"))
                else:
                    decrypted_char = chr((ord(char) + (n + m) - ord("n")) % 13 + ord("n"))
            else:
                if ord("A") <= ord(char) <= ord("M"):  # First half of the alphabet (A-M)
                    decrypted_char = chr((ord(char) + n - ord("A")) % 13 + ord("A"))
                else:
                    decrypted_char = chr((ord(char) - (m ** 2) - ord("N")) % 13 + ord("N"))
        else:  # Non-alphabetic characters remain unchanged
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text  # Final decrypted text is returned


# Function to check the decrypted text matches the original text
def check_correctness(data, decrypted_data):
    if data == decrypted_data:
        print("Success! The decrypted text matches the original text.")
    else:
        print("Failed! The decrypted text does not match the original text.")


# Encrypting the data using the encrypt function
encrypted_data = encrypt(data, n, m)
print("Encrypted Text :", encrypted_data)

# The encrypted text is written to a file
with open('encrypted_text.txt', 'w') as f:
    f.write(encrypted_data)

# Decrypting the encrypted text using the decrypt function
decrypted_data = decrypt(encrypted_data, n, m)
print("Decrypted Text :", decrypted_data)

# The decrypted text is written to a file
with open('decrypted_text.txt', 'w') as f:
    f.write(decrypted_data)

# Checking if the decryption process was successful
check_correctness(data, decrypted_data)
