#!/usr/bin/python3
import base64

secret_message = input("Enter a secret message to encode: ")

#Encoding...
encoded_message = base64.b64encode(secret_message.encode('utf-8'))
print(encoded_message)

#Decoding
decoded_message = base64.b64decode(encoded_message.decode('utf-8'))
print(decoded_message)
