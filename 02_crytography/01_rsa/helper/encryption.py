import os
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


def encryptor(data, public_key):
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted = encryptor.encrypt(data.encode("utf-8"))
    return encrypted


def decryptor(data, private_key="private.pem"):
    decryptor = PKCS1_OAEP.new(RSA.importKey(open(private_key, "rb").read()))
    decrypted = decryptor.decrypt(data)
    return decrypted.decode("utf-8")


def encryptor_to_file(data, public_key):
    data = data.encode("utf-8")
    if not os.path.isdir("/tmp/example"):
        os.mkdir("/tmp/example")
    filename = "encrypted_data.txt"
    file_out = open("/tmp/example/" + filename, "wb")
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    encryptor = PKCS1_OAEP.new(public_key)
    enc_session_key = encryptor.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
    file_out.close()
    return filename


def decryptor_from_file(file, private_key="private.pem"):
    file_in = open(file, "rb")
    private_key = RSA.import_key(open(private_key).read())
    enc_session_key, nonce, tag, ciphertext = [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

    # Decrypt the session key with the private RSA key
    decryptor = PKCS1_OAEP.new(private_key)
    session_key = decryptor.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return data.decode('utf-8')
