
# def encrypt_or_decrypt(word, encryption_dictionary):
#     '''WORD is the word to be encrypted or decrypted. ENCRYPTION_DICTIONARY is the ROT-13 dictionary used for encryption-decryption.'''
#     working_list = []
#     for character in word:
#         working_list.append(encryption_dictionary[character])
#     return ''.join(working_list)

def encrypt_or_decrypt(word, dict):
    '''WORD is the word to be encrypted or decrypted. ENCRYPTION_DICTIONARY is the ROT-13 dictionary used for encryption-decryption.'''
    working_list = []
    for character in word:
        working_list.append(dict[character])
    the_final_word = ''.join(working_list)
    return the_final_word


word_to_encrypt = "logic to get word from user"
# Encrypt the word:
the_encrypted_word = encrypt_or_decrypt(word_to_encrypt, dict)

print(the_encrypted_word)
