import hashlib

def get_hash_md5(*text:str) -> str:
    message = hashlib.md5()
    for i in text:
        message.update(i.encode())
    return  message.hexdigest()


def get_hash_sha512(*text:str) -> str:
    message = hashlib.sha512()
    for i in text:
        message.update(i.encode())
    return  message.hexdigest()