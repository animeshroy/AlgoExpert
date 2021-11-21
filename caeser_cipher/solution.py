def caesarCipherEncryptor(string, key):
    return ''.join([chr(((ord(x)+key)%97)%26+97) if key else x for x in string ])