import secrets

from web3 import Web3


class AuthMessages:
    @classmethod
    def generate_nonce(cls):
        return secrets.token_hex(16)

    @classmethod
    def get_message(cls, nonce=None):
        return f"Sign this message to authenticate: {nonce or cls.generate_nonce()}"

    @classmethod
    def hash_message(cls, message: str):
        return Web3.solidity_keccak(text=message)

    @classmethod
    def recover_message(cls, hash: str, signature: str):
        return Web3.eth.account.recover_message(hash, signature=signature)