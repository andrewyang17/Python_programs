from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
f = open("public.pem", 'wb')
f.write(key.publickey().exportKey('PEM'))
f.close()

f = open("private.pem", "wb")
f.write(key.exportKey('PEM'))
f.close()

public_key = RSA.importKey(open("public.pem", "rb").read())
private_key = RSA.importKey(open("private.pem", "rb").read())

encryptor = PKCS1_OAEP.new(public_key)
message = "fuck this"
encrypted = encryptor.encrypt(message.encode("utf-8"))
print(encrypted)

decryptor = PKCS1_OAEP.new(private_key)
decrypted = decryptor.decrypt(encrypted)
print(decrypted.decode("utf-8"))
