import web3
from web3 import Web3, AsyncWeb3

from utils import get_env_key

chain_config = {
    "base-sepolia": {
        "provider_url": get_env_key("PROVIDER_URL_BASE_SEPOLIA"),
        "chain_id": get_env_key("CHAIN_ID_BASE_SEPOLIA"),
        "currency_symbol": get_env_key("CURRENCY_BASE_SEPOLIA"),
    }
}

def get_provider(chain="base-sepolia"):
    if not (config := chain_config.get(chain)):
        raise ValueError()
    provider = Web3(Web3.HTTPProvider(config["provider_url"]))
    return provider

def get_async_provider(chain="base-sepolia"):
    if not (config := chain_config.get(chain)):
        raise ValueError()
    provider = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(config["provider_url"]))
    return provider

if __name__ == "__main__":
    provider = get_provider()
    print(provider.eth.get_block("latest"))
