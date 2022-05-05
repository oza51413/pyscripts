#!/usr/bin/python3
import base64

#Usage: receives user input and prints out the encoded and decoded form of the input

def generate_encryption():
	message = input("Enter a message to encrypt: ")
	encoded_message = base64.b64encode(message.encode('utf-8'))
	return encoded_message
print(generate_encryption())

def decrypt_encryption():
	#dont have to call generate_encryption, because by using it here it prints the 
	#encoded message
	decrypted = base64.b64decode(generate_encryption())
	return decrypted

print(decrypt_encryption())
