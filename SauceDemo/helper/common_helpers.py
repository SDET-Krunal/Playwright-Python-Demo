import base64
import logging


def encrypt_string(string_to_be_encrypt: str):
    """ Encrypts a string using Base64 """
    encrypted_string = base64.b64encode(string_to_be_encrypt.encode('utf-8')).decode('utf-8')
    logging.info("Encrypted string of '{}' :: {}".format(string_to_be_encrypt, encrypted_string))

    return encrypted_string


def decrypt_string(string_to_be_decrypt: str):
    """ Decrypts a Base64-encoded string """
    decrypted_string = base64.b64decode(string_to_be_decrypt.encode('utf-8')).decode('utf-8')
    logging.info("Decrypted string of '{}' :: {}".format(string_to_be_decrypt, decrypted_string))

    return decrypted_string
