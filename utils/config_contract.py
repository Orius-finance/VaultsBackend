class ConfigUtils:
    @staticmethod
    def config_contract(address: str):
        pass

    @classmethod
    def is_whitelisted_users(cls, address: str):
        contract = cls.config_contract()
        return contract.functions.whitlisted_users(address).call()
