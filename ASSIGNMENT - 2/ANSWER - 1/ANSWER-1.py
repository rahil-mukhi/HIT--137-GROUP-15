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



      