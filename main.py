import os
from Crypto.Cipher import Blowfish
from art import *

# KEY_SIZE = 16  # 128 bits

def pad(data):
    """
    Pad the input data to make its length a multiple of 8 bytes.

    Parameters:
    data (bytes): The input data to be padded.

    Returns:
    bytes: The padded data.
    """
    pad_len = 8 - (len(data) % 8)
    return data + bytes([pad_len] * pad_len)


def unpad(data):
    """
    Remove the padding from the input data.

    Parameters:
    data (bytes): The input data to be unpadded.

    Returns:
    bytes: The unpadded data.
    """
    pad_len = data[-1]
    return data[:-pad_len]


def encrypt(plaintext, key, iv=None):
    if len(key) % 8 != 0:
        raise ValueError("Key size must be a multiple of 8 bytes")

    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv=iv)
    plaintext_padded = pad(plaintext)
    ciphertext = cipher.encrypt(plaintext_padded)
    return ciphertext


def decrypt(ciphertext, key, iv=None):
    if len(key) % 8 != 0:
        raise ValueError("Key size must be a multiple of 8 bytes")

    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv=iv)
    plaintext_padded = cipher.decrypt(ciphertext)
    plaintext = unpad(plaintext_padded)
    return plaintext

def get_key_size():
    while True:
        try:
            print("Choose key size:")
            print("[1] 128 bits")
            print("[2] 192 bits")
            print("[3] 256 bits")
            choice = int(
                input("Enter the number corresponding to your choice: "))

            if choice == 1:
                return 16  # 128 bits
            elif choice == 2:
                return 24  # 192 bits
            elif choice == 3:
                return 32  # 256 bits
            else:
                print("Invalid choice. Please enter a valid option.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")


def main():
    """
    Demonstrate the usage of the encryption and decryption functions.

    This function continuously prompts the user for a plaintext input to be encrypted.
    It generates a random key and initialization vector (IV) for each encryption/decryption cycle.
    The plaintext is encrypted, then decrypted, and both the original and decrypted plaintexts, as well as the ciphertext, are printed.
    The function handles ValueError exceptions (for invalid key sizes) and other unexpected exceptions.

    Raises:
    ValueError: If the key size is not valid.
    Exception: If an unexpected error occurs during encryption or decryption.
    """
    blowfish = '''
              |    .
          .   |L  /|   .          _
      _ . |\ _| \--+._/| .       (_)
     / ||\| Y J  )   / |/| ./
    J  |)'( |        ` F`.'/        _
  -<|  F         __     .-<        (_)
    | /       .-'. `.  /-. L___
    J \      <    \  | | O\|.-'  _
  _J \  .-    \/ O | | \  |F    (_)
 '-F  -<_.     \   .-'  `-' L__
__J  _   _.     >-'  )._.   |-'
`-|.'   /_.           \_|   F
  /.-   .                _.<
 /'    /.'             .'  `\\
  /L  /'   |/      _.-'-\\
 /'J       ___.---'\\|
   |\\  .--' V  | `. `
   |\\/`. `-.     `._)
      / .-.\\
      \\ (  `\\
       `.\n'''

    print("-" * 50)
    print(blowfish)
    print(text2art("Blowfish", font="small"))
    print("-" * 50 + "\n")
    print("CTG Assignment CSF02 2023\n")
    print(
        "This script simulates the encryption and decryption of a \nplaintext using Blowfish in the Cipher Block Chaining mode.\n"
        "It pads and unpads the plaintext to a multiple of 8 bytes,\nand uses a random initialization vector (IV) for each \nencryption/decryption cycle."
        "The plaintext, ciphertext, \nand decrypted plaintext are printed for each cycle.\n"
    )
    print("-" * 50 + "\n")

    while True:
        try:
            key_size = get_key_size()  # Use the user-selected key size
            key = os.urandom(key_size)
            iv = os.urandom(8)

            plaintext_input = input("Enter the plaintext: ")
            if not plaintext_input:
                print("Please enter a non-empty plaintext.")
                continue  # Continue to the next iteration of the loop

            plaintext = plaintext_input.encode('utf-8')

            ciphertext = encrypt(plaintext, key, iv)
            decrypted_text = decrypt(ciphertext, key, iv)

            # print("\nPlaintext:", str(plaintext)[2:-1])
            # print("Ciphertext:", str(ciphertext)[2:-1])
            # print("Decrypted Text:", decrypted_text.decode('utf-8'))
            
            print("\nPlaintext:", repr(plaintext)[2:-1])
            print("Ciphertext:", repr(ciphertext)[2:-1])
            print("Decrypted Text:", repr(decrypted_text)[2:-1])
            print("\nEncryption and decryption successful.")

            break

        except ValueError as ve:
            print("ValueError:", str(ve))
        except Exception as e:
            print("An unexpected error occurred:", str(e))


if __name__ == "__main__":
    main()
