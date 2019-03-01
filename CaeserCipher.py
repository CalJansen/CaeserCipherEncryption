
try:
    message_input = input("Enter a message: ").upper()
except ValueError:
    print("Invalid Input - enter a String")

print(message_input)

try:
    key_input = int(input("Enter a key from 1-25: "))
except NameError:
    print("Invalid Input - enter an int")


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
    print(encrypted)


caeser_cipher(message_input, key_input)





