from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def bcrypt(password):
        return pwd_context.hash(password)
    
    def verify(plain_password,hashed_password):
        return pwd_context.verify(hashed_password,plain_password)


