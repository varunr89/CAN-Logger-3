from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives import serialization
import base64

PEM_public_key_first = '-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE'
PEM_public_key_last = '\n-----END PUBLIC KEY-----\n'

public_key_hex = [0x3B, 0x3C, 0x19, 0x35, 0x90, 0xDA, 0xE4, 0x6F, 0x64, 0x8C, 0x7E, 0x5E, 0x52, 0x82, 0xA0, 0x98, 
0xA2, 0x5D, 0x7C, 0xC2, 0xDD, 0x3D, 0xA4, 0x8E, 0x18, 0xCF, 0x5E, 0xA1, 0x39, 0x73, 0x67, 0x6E,
0xDB, 0xD6, 0x25, 0xD2, 0xEC, 0x0E, 0xF7, 0x83, 0x4C, 0xC7, 0xD7, 0x5D, 0x5E, 0x02, 0x1D, 0x41, 
0xCB, 0x25, 0xFD, 0x1A, 0x1E, 0xEA, 0x32, 0x6B, 0x61, 0xC6, 0xF4, 0xC1, 0xBC, 0xF2, 0x21, 0x01]

data_hex = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 
0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F]

signature_hex = [0x86, 0x2B, 0x67, 0x14, 0x1C, 0x06, 0xE7, 0x08, 0xF5, 0xFA, 0x1D, 0x17, 0x8E, 0x81, 0xF9, 0x79, 
0x17, 0xBC, 0xBA, 0x85, 0xB4, 0x85, 0xAA, 0xBE, 0x1D, 0x1C, 0x2B, 0xCB, 0xE9, 0x43, 0x96, 0x3F,
0xB8, 0xFB, 0x75, 0x25, 0x3B, 0xF0, 0x0E, 0x0A, 0x76, 0x19, 0x58, 0x0F, 0xFA, 0x96, 0xB0, 0xCB, 
0x68, 0xED, 0x44, 0x81, 0x9F, 0x7B, 0x91, 0x6F, 0x68, 0x31, 0x4D, 0xC2, 0x83, 0xEE, 0xF6, 0xE3
]
pub_key = bytes(public_key_hex)
print("Puclic key is:", pub_key.hex().upper())
print("")

data = bytes(data_hex)
print("Data is:", data.hex().upper())
print("")
#Load Public Key
PEM_public_key = base64.b64encode(bytes(public_key_hex)).decode('ascii')
public_key_string = PEM_public_key_first + PEM_public_key[:28]+'\n'+ PEM_public_key[28:] + PEM_public_key_last
serialized_public_teensy = bytes(public_key_string,'ascii')
public_key = serialization.load_pem_public_key(serialized_public_teensy,backend=default_backend())

#Convert Signature to DER format
signature_r = 0
signature_s = 0
for i in range(32):
	signature_r = signature_r<<8|signature_hex[i]
	signature_s = signature_s<<8|signature_hex[i+32]
#print(hex(signature_r))
#print(hex(signature_s))
signature = utils.encode_dss_signature(signature_r,signature_s)
print("Signature is:",bytes(signature_hex).hex().upper())
print("")

#Verify the signature
if public_key.verify(signature,data,ec.ECDSA(hashes.SHA256()))== None:
	print("Verify Signature Successfully!")


