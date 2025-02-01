import secrets

import pytest
from web3 import Web3

from auth.models import InviteCode


@pytest.mark.django_db
def test_sign_in_with_signature(client):
    new_wallet = Web3.eth.account.create()
    invite_code = InviteCode(code=secrets.token_hex(8))

    nonce_response = client.post(f"/auth/nonce/?wallet_address={new_wallet.address}&invite_code={invite_code.code}")
    assert nonce_response.ok == True
    message = nonce_response.data["message"]

    login_body = {
        "wallet_address": new_wallet.address,
        "signature": Web3.eth.account.sign_message(message),
        "invite_code": invite_code
    }
    login_response = client.post(f"/auth/login/", data=login_body)
