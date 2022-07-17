import cv2
from werkzeug.utils import secure_filename
from pathlib import Path
from Crypto.Cipher import AES
import hashlib

BASE_DIR = Path(__file__).resolve().parent

def get_path(file:str):
    return str(str(BASE_DIR) + "/image_upload/" + file)

def check_upload_file(file):
          fp = file
          filename = fp.filename
          db_upload_path = secure_filename(filename)
          fp.save(str(BASE_DIR) + "/image_upload/" + db_upload_path )

def get_rgb_value(image_path): 
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    return img

def string_key():
    with open('foo.txt') as f:
        lines = f.readlines()
    return str(lines)


class CipherAES:
    def __init__(self, hash_key_data: bytes):
        self.hash_key_data = hash_key_data
        self.plaintext_msg = b'a'

    def generateCipher(self):
        cipher = AES.new(self.hash_key_data, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(self.plaintext_msg)
        return cipher.nonce, tag, ciphertext

    def decryptCipher(self, nonce, tag, ciphertext):
        cipher = AES.new(self.hash_key_data, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        return data.decode()

    def updateMessage(self, msg:bytes):
        self.plaintext_msg = msg.encode()
    
    @staticmethod
    def get_hash_md5(text:str) -> str:
        return hashlib.md5(text.encode('utf-8')).hexdigest().encode()
    
    @staticmethod
    def get_hash_sha512(text:str) -> str:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()

    @staticmethod
    def hash_file(filename):
        h  = hashlib.sha256()
        b  = bytearray(128*1024)
        mv = memoryview(b)
        with open(filename, 'rb', buffering=0) as f:
            for n in iter(lambda : f.readinto(mv), 0):
                h.update(mv[:n])
        return h.hexdigest()

