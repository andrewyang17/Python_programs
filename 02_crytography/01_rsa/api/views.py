import base64
from flask import jsonify, request
from Crypto.PublicKey import RSA

from . import api
from ..helper.wrappers import api_required
from ..helper.encryption import encryptor, decryptor, encryptor_to_file, decryptor_from_file
from .. import File


@api.route('/')
def index():
    return "RSA Algorithm"


@api.route('/encrypt', methods=['POST'])
@api_required
def encrypt():
    public_key = request.files['public_key']
    filename = "/tmp/example/key.pem"
    f = open(filename, 'wb')
    f.write(public_key.read())
    f.close()

    public_key = RSA.import_key(open(filename).read())
    data = "Fuck you"
    encrypted = encryptor(data, public_key)
    return jsonify({"data": str(encrypted)})


@api.route('/decrypt', methods=['POST'])
@api_required
def decrypt():
    data = request.values.get('data')
    output = decryptor(data)
    return jsonify({"output": output})


@api.route('/encrypt2', methods=['POST'])
@api_required
def encrypt2():
    public_key = request.files['public_key']
    filename = "/tmp/example/key.pem"
    f = open(filename, 'wb')
    f.write(public_key.read())
    f.close()

    public_key = RSA.import_key(open(filename).read())
    data = "Fuck you bitch"
    file_out = encryptor_to_file(data, public_key)
    file_url = File.url(file_out)
    return jsonify({"file": file_url})


@api.route('/decrypt2', methods=['POST'])
@api_required
def decrypt2():
    file_in = request.files['file']
    filename = "/tmp/example/example.txt"
    f = open(filename, 'wb')
    f.write(file_in.read())
    f.close()
    output = decryptor_from_file(filename)
    return jsonify({"output": output})
