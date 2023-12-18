import os
from Crypto.Cipher import Blowfish
from art import *

KEY_SIZE = 16  # 128 bits


def pad(data):
    """
    Pad the input data to make its length a multiple of 8 bytes.

    This function calculates the number of bytes needed to make the length of the data a multiple of 8.
    It then creates a new bytes object of that length, filled with the padding length value, and appends it to the end of the data.

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

    This function reads the last byte of the data to determine the padding length.
    It then returns a new bytes object with the padding removed from the end.

    Parameters:
    data (bytes): The input data to be unpadded.

    Returns:
    bytes: The unpadded data.
    """
    pad_len = data[-1]
    return data[:-pad_len]


def encrypt(plaintext, key, iv=None):
    """
    Encrypt the plaintext using Blowfish in CBC mode.

    This function creates a new Blowfish cipher object with the given key and initialization vector (IV).
    It then pads the plaintext to a multiple of 8 bytes, and encrypts it using the cipher.
    The encrypted ciphertext is then returned.

    Parameters:
    plaintext (bytes): The input data to be encrypted.
    key (bytes): The secret key to use in the symmetric cipher. It must be 16, 24, or 32 bytes long.
    iv (bytes, optional): The initialization vector to use for the cipher. If None, a random IV will be created.

    Returns:
    bytes: The encrypted ciphertext.

    Raises:
    ValueError: If the key size is not valid.
    """
    if len(key) != KEY_SIZE:
        raise ValueError("Key size must be {} bytes".format(KEY_SIZE))

    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv=iv)
    plaintext_padded = pad(plaintext)
    ciphertext = cipher.encrypt(plaintext_padded)
    return ciphertext


def decrypt(ciphertext, key, iv=None):
    """
    Decrypt the ciphertext using Blowfish in CBC mode.

    This function creates a new Blowfish cipher object with the given key and initialization vector (IV).
    It then decrypts the ciphertext using the cipher, and unpads the resulting plaintext.
    The decrypted plaintext is then returned.

    Parameters:
    ciphertext (bytes): The input data to be decrypted.
    key (bytes): The secret key to use in the symmetric cipher. It must be 16, 24, or 32 bytes long.
    iv (bytes, optional): The initialization vector to use for the cipher. If None, a random IV will be created.

    Returns:
    bytes: The decrypted plaintext.

    Raises:
    ValueError: If the key size is not valid.
    """
    if len(key) != KEY_SIZE:
        raise ValueError("Key size must be {} bytes".format(KEY_SIZE))

    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv=iv)
    plaintext_padded = cipher.decrypt(ciphertext)
    plaintext = unpad(plaintext_padded)
    return plaintext


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

    print("-" * 50 )
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
            key = os.urandom(KEY_SIZE)
            iv = os.urandom(8)

            plaintext_input = input("Enter the plaintext: ")
            if not plaintext_input:
                print("Please enter a non-empty plaintext.")
                continue  # Continue to the next iteration of the loop

            plaintext = plaintext_input.encode('utf-8')

            ciphertext = encrypt(plaintext, key, iv)
            decrypted_text = decrypt(ciphertext, key, iv)

            print("\nPlaintext:", str(plaintext)[2:-1])
            print("Ciphertext:", str(ciphertext)[2:-1])
            print("Decrypted Text:", decrypted_text.decode('utf-8'))
            print("\nEncryption and decryption successful.")

            break

        except ValueError as ve:
            print("ValueError:", str(ve))
        except Exception as e:
            print("An unexpected error occurred:", str(e))


if __name__ == "__main__":
    main()
