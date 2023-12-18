# Blowfish Simulation
This repository contains a Python script that simulates the Blowfish algorithm in the Cipher Block Chaining (CBC) mode, as part of my group's cryptography assignment. 

The Blowfish algorithm is a type of symmetric-key block cipher. It operates on variable-length blocks (usually 32 to 448 bits) and is known for its simplicity and speed.

This script allows users to choose a key size and plaintext, and simulate the encryption and decryption of the plaintext using Blowfish in the CBC mode, allowing users to see the relationship between the key size and the ciphertext size, and the seamingly randomness of the ciphertext.

## Getting Started

1. Clone this repository:
```bash
git clone https://github.com/Kairos-T/blowfish-simulation
cd blowfish-simulation
```

2. (Optional): Create a Python virtual environment
```bash
sudo python3 -m venv venv
source venv/bin/activate
```

3. Install required dependencies
```bash
pip install -r requirements.txt
```

4. Run the script:
```bash
python3 main.py
```

## Simulation Results (Sample)

### Main Menu
```
--------------------------------------------------

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
 /'    /.'             .'  `\
  /L  /'   |/      _.-'-\
 /'J       ___.---'\|
   |\  .--' V  | `. `
   |\/`. `-.     `._)
      / .-.\
      \ (  `\
       `.

 ___  _                __  _      _    
| _ )| | ___ __ __ __ / _|(_) ___| |_  
| _ \| |/ _ \\ V  V /|  _|| |(_-<| ' \ 
|___/|_|\___/ \_/\_/ |_|  |_|/__/|_||_|
                                       

--------------------------------------------------

CTG Assignment CSF02 2023

This script simulates the encryption and decryption of a 
plaintext using Blowfish in the Cipher Block Chaining mode.
It pads and unpads the plaintext to a multiple of 8 bytes,
and uses a random initialization vector (IV) for each 
encryption/decryption cycle.The plaintext, ciphertext, 
and decrypted plaintext are printed for each cycle.

--------------------------------------------------
```

### Key Size Options
```
Choose key size:
[1] 128 bits
[2] 192 bits
[3] 256 bits
Enter the number corresponding to your choice: 
```

### Simulation

**Scenario 1: Same key size, same input text**
Using 128 bits key size:

```
Enter the plaintext: CTG Assignment

Plaintext: CTG Assignment
Ciphertext: \xa7-\xba\xcc'\x85w\xd1\x8c\x9f\x1cTdA\xd8\x9d
Decrypted Text: CTG Assignment

Encryption and decryption successful.

```

```
Enter the plaintext: CTG Assignment

Plaintext: CTG Assignment
Ciphertext: \x8e\x977\xe1W\xe3\xab\nE\xb8\xf0?\xf9u\x8f\x0b
Decrypted Text: CTG Assignment

Encryption and decryption successful.
```

**Scenario 2: Same key size, different lengths of input text**

Using 128 bits key size:

```
Enter the plaintext: 1

Plaintext: 1
Ciphertext: \xaa|\x18\x0c\x1d>\x18\xb9
Decrypted Text: 1

Encryption and decryption successful.
```

```
Enter the plaintext: 1234567890987654321

Plaintext: 1234567890987654321
Ciphertext: \xa7\x07\x1eD\xea^\xa1w2\x80\xeb,`\x07\x833?\x8f\x9c d5\xb1\xe3
Decrypted Text: 1234567890987654321

Encryption and decryption successful.
```

**Scenario 3: Different key sizes, same input text**

Using 128 bits key size:

```
Enter the number corresponding to your choice: 1
Enter the plaintext: 123

Plaintext: 123
Ciphertext: \x8e\x90`O\x84\xd3"\xcd
Decrypted Text: 123
```

Using 192 bits key size:

```
Enter the number corresponding to your choice: 2
Enter the plaintext: 123

Plaintext: 123
Ciphertext: Xu&\x92\xd4v\xb6/
Decrypted Text: 123
```

Using 256 bits key size:

```
Enter the number corresponding to your choice: 3
Enter the plaintext: 123

Plaintext: 123
Ciphertext: \x11`\xb3\n0\xc6Q4
Decrypted Text: 123
```