import bcrypt
from database.models import User




def set_pwd_hash(pwd:str):
    pwd_bytes = pwd.encode("utf-8") #pasa la clave a bytes
    salt = bcrypt.gensalt()
    pwd_hash = bcrypt.hashpw(pwd_bytes, salt)
    return pwd_hash.decode('utf-8')



def verify_password(pwd:str, pwd_hash: str) -> bool:
    try:
        pwd_bytes = pwd.encode("utf-8")
        pwd_hash_byte = pwd_hash.encode("utf-8")
        return bcrypt.checkpw(pwd_bytes, pwd_hash_byte)
    except Exception:
        return False


