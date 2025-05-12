from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class Hasher():

    def __init__(self):
        self.ph = PasswordHasher()

    def hasher(self, senha: str) -> str:
        return self.ph.hash(password=senha)

    def verifica_senha(self, senha: str, hash: str) -> bool:
        try:
            return self.ph.verify(hash, senha)
        except:
            return False
