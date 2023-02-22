logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""
print(logo)

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                 ' ', ',', ':', ';', '.', '?', '!','_','@',"\""]

def encrypt(text, shift):
    text_length = len(text)
    encrypted_text = ''

    alphabet_list_length = len(alphabet_list)
    alphabet_list_index_shift = 0

    for i in range(text_length):
        alphabet_list_index_shift = alphabet_list.index(text[i]) + int(shift)

        if alphabet_list_index_shift >= int(alphabet_list_index_shift/alphabet_list_length) * alphabet_list_length:
            alphabet_list_index_shift -= int(alphabet_list_index_shift/alphabet_list_length) * alphabet_list_length

        if alphabet_list_index_shift <= int(alphabet_list_index_shift/alphabet_list_length) * alphabet_list_length:
            alphabet_list_index_shift += int(alphabet_list_index_shift/alphabet_list_length) * alphabet_list_length    

        encrypted_text += alphabet_list[alphabet_list_index_shift]

    return encrypted_text

def decrypt(text, shift):
    text_length = len(text)
    decrypted_text = ''

    alphabet_list_length = len(alphabet_list)
    alphabet_list_index_shift = 0

    for i in range(text_length):
        alphabet_list_index_shift = alphabet_list.index(text[i]) - int(shift)

        if alphabet_list_index_shift >= int(alphabet_list_index_shift/alphabet_list_length) * alphabet_list_length:
            alphabet_list_index_shift -= int(alphabet_list_index_shift/alphabet_list_length) * alphabet_list_length

        if alphabet_list_index_shift <= int(alphabet_list_index_shift/alphabet_list_length) * alphabet_list_length:
            alphabet_list_index_shift += int(alphabet_list_index_shift/alphabet_list_length) * alphabet_list_length    

        decrypted_text += alphabet_list[alphabet_list_index_shift]

    return decrypted_text

def encrypt_encrypt():
    direction = input("\nType 'encode' to encrypt and 'decode' to decrypt: ")
    if direction != "encode" or direction != "decode":
        print("Wrong input, type either 'encode' or 'decode' please!, Try again!")

    if direction == "encode":
        text = input("Type your message for encryption: ")
        shift = input("Type the shift number: ")
        encrypted_text = encrypt(text, shift)
        print(f"\nEncrypted text of \"{text}\" with ({shift}) shift(s) is: ", encrypted_text)
    elif direction == "decode":
        text = input("Type your message for decryption: ")
        shift = input("Type the shift number: ")
        decrypted_text = decrypt(text, shift)
        print(f"\nDecrypted text of \"{text}\" with ({shift}) shift(s) is: ", decrypted_text)

while(True):
    encrypt_encrypt()



