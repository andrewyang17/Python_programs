from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

# Encrypt
data = "No newline at end of file".encode("utf-8")
file_out = open("encrypted_data.txt", "wb")
public_key = RSA.import_key(open("public.pem").read())
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
encryptor = PKCS1_OAEP.new(public_key)
enc_session_key = encryptor.encrypt(session_key)

# Encrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
[file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
file_out.close()


# Decrypt
file_in = open("encrypted_data.txt", "rb")
private_key = RSA.import_key(open("private.pem").read())
enc_session_key, nonce, tag, ciphertext = [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

# Decrypt the session key with the private RSA key
decryptor = PKCS1_OAEP.new(private_key)
session_key = decryptor.decrypt(enc_session_key)

# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))
