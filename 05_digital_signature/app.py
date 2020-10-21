import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5


def usage():
    print("Usage: \n"
          "variables.py -s <private-key> <data> <signature-file> \n"
          "variables.py -v <public-key> <data> <signature-file> \n")


if len(sys.argv) < 5:
    usage()
    quit()

OPTION = sys.argv[1]
KEY = sys.argv[2]
DATA = sys.argv[3]
SIGNATURE = sys.argv[4]


def generate_signature(private_key, data, sign):
    print("Generating signature ...")
    hash = SHA256.new(data)
    rsa = RSA.importKey(private_key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(hash)
    with open(sign, 'wb') as f:
        f.write(signature)


def verify_signature(public_key, data, sign):
    print("Verifying signature ...")
    hash = SHA256.new(data)
    rsa = RSA.importKey(public_key)
    signer = PKCS1_v1_5.new(rsa)
    with open(sign, 'rb') as f:
        signature = f.read()
        if signer.verify(hash, signature):
            print("Success")
        else:
            print("Verification failure")


with open(KEY, 'rb') as f:
    key = f.read()

with open(DATA, 'rb') as f:
    data = f.read()

if OPTION == "-s":
    generate_signature(key, data, SIGNATURE)
elif OPTION == '-v':
    verify_signature(key, data, SIGNATURE)
else:
    usage()
