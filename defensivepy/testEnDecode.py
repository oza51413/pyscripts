#!/usr/bin/python3
import multipleEnDecoding

#[*]ENCODING...
message = input("Enter the secret message you want to encode")
#calling functions from the script we imported eg= scriptname.function(param1,param2)
	#this just prints out the encoding
print("Single Encoding using base64: ",multipleEnDecoding.encodeto_base64(message,1))
print("Double Encoding using base64: ",multipleEnDecoding.encodeto_base64(message,2))
print("Triple Encoding using base85: ",multipleEnDecoding.encodeto_base85(message,3))

	#Storing the encoding into variables to be able to use when decoding
		#technically we can store them and then print out the var abov
			#like this: print("Single Encoding using base64", base64Single)
base64Single = multipleEnDecoding.encodeto_base64(message,1)
base64Double = multipleEnDecoding.encodeto_base64(message,2)
base85Triple = multipleEnDecoding.encodeto_base85(message,3)



#[*]DECODING...
from multipleEnDecoding import decodefrom_base64, decodefrom_base85
#base64Single,base64Double, & base85Triple go in as "encodedmessage" param for the
	#decodefrom_base64 and decodefrom_base85 functions in multipleEnDecoding.py
print("Single Decoding from base64: ", multipleEnDecoding.decodefrom_base64(base64Single,1))
print("Double Decoding from base64: ", multipleEnDecoding.decodefrom_base64(base64Double,2))
print("Triple Decoding from base85: ", multipleEnDecoding.decodefrom_base85(base85Triple,3))
