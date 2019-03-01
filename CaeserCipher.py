
try:
    message_input = input("Enter a message: ").upper()
except ValueError:
    print("Invalid Input - enter a String")

try:
    key_input = int(input("Enter a key from 1-25: "))
except NameError:
    print("Invalid Input - enter an int")

print(message_input)


def caeser_cipher(message, key):
    encrypted = ""
    starting_alpha = ord('A')
    for character in message:
        if character.isalpha():
            num = ord(character) - starting_alpha
            num_mod = (num + key) % 26
            encrypted += chr(num_mod + starting_alpha)
        else:
            encrypted += character
    return encrypted


encrypted_message = caeser_cipher(message_input, key_input)
print(encrypted_message)


def caeser_decryption(message, key):
    decrypted = ""
    starting_alpha = ord('A')
    for character in message:
        if character.isalpha():
            num = ord(character) - starting_alpha
            num_mod = (num - key) % 26
            decrypted += chr(num_mod + starting_alpha)
        else:
            decrypted += character
    return decrypted


decrypted_message = caeser_decryption(encrypted_message, key_input)
print(decrypted_message)



