#!/usr/bin/python3
import base 64


#ENCODING
def encodeto_base64(message, rounds):
	for _ in range(rounds):
		message = str(base64.b64encode.(message.encode('utf-8')))
		message = str(message)[2:-1]
	return str.encode(message)

def encodeto_base85(message, rounds):
	for _ in range(rounds):
		message = str(base64.b85encode(message.encode('utf-8')))
		message = str(message)[2:-1]
	return str.encode(message)


#DECODING
def decodefrom_base64(encodedmessage, rounds):
	for _ in range(rounds):
		encodedmessage = base64.b64decode(encodedmessage.decode('utf-8'))
	return encodedmessage

def decodefrom_base85(encodedmessage, rounds):
	for _ in range(rounds):
		encodedmessage = base64.b85decode(encodedmessage.decode('utf-8'))
	return encodedmessage


