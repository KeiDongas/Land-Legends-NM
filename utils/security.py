import bcrypt
from database.models import User




def set_pwd_hash(pwd:str):
    pwd_bytes = pwd.encode("utf-8")
    salt = bcrypt.gensalt()
    pwd_hash = bcrypt.hashpw(pwd_bytes, salt)
    return pwd_hash.decode('utf-8')











def verify_password(password:str):
    if password == User.password:
        return {"message": "valid"}
    else:
        return {"message": "invalid"}

