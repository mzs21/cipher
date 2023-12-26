text = input('Enter Encrypted text: ')  # Ex.: 'mrttaqrhknsw ih puggrur'
custom_key = input('\nKey value: ')  # Sets the key for encryption/decryption. Ex.: 'python'


def vigenere(message, key, direction=1):  # message:  The text to be encrypted or decrypted, key: The key to be used for the cipher, direction (optional): 1 for encryption, -1 for decryption (default is 1)

    key_index = 0  # Initializes a counter to track the current position within the key. 
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Stores a string containing the alphabet for reference.
    
    final_message = ''  # Initializes an empty string to store the result (encrypted or decrypted text).

    for char in message.lower(): # Iterates through each character in the message, converting them to lowercase for consistency.

        # Append any non-letter character to the message
        if not char.isalpha():      # If the character is not a letter, it's simply added 
            final_message += char   # to the final_message without any modification.
        else:
            # Find the right key character to encode/decode

            key_char = key[key_index % len(key)] #  Retrieves the current key character by cycling through the key using the key_index.

            key_index += 1

            # Define the offset and the encrypted/decrypted letter

            offset = alphabet.index(key_char) # Determines the offset for encryption/decryption based on the position of the key character in the alphabet.

            index = alphabet.find(char) # Finds the position of the current character in the alphabet.

            new_index = (index + offset*direction) % len(alphabet) # Calculates the new position for the encrypted/decrypted character based on the offset and direction.

            final_message += alphabet[new_index] # Calculates the new position for the encrypted/decrypted character based on the offset and direction.

    return final_message


def encrypt(message, key): # A simple wrapper function that calls vigenere for encryption.
    return vigenere(message, key)
    

def decrypt(message, key): # A wrapper function that calls vigenere for decryption by setting the direction to -1.
    return vigenere(message, key, -1)


print(f'\nEncrypted text: {text}\n')

print(f'Key: {custom_key}\n')

decryption = decrypt(text, custom_key)

print(f'Decrypted text: {decryption}')