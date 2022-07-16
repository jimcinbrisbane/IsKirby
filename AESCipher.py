from Crypto.Cipher import AES

### Requires this command > pip install pycryptodome==3.4.3

### Create CipherAES object with random_data (hash)
### Encrypt message with generateCipher
### Decrypt cipher with decryptCipher (needs nonce, tag, ciphertext and
### random_data (hash)
### Add message to encrypt with updateMessage

class CipherAES:
    def __init__(self, random_data: bytes):
        self.random_data = random_data
        self.plaintext_msg = b'a'

    def generateCipher(self):
        cipher = AES.new(self.random_data, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(self.plaintext_msg)
        return cipher.nonce, tag, ciphertext
        

    def decryptCipher(self, nonce, tag, ciphertext, random_data):
        cipher = AES.new(random_data, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        return data

    def updateMessage(msg: bytes)
        self.plaintext_msg = msg



## Example

#data = b'secret data'

#key = b'12345678901234567890123456789012'

#c = CipherAES(key, data)


#nonce, tag, ciphertext = c.generateCipher()
#print(ciphertext)

#msg = c.decryptCipher(nonce, tag, ciphertext, key)

#print(msg)
