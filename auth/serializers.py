from rest_framework import serializers


class VerifySignatureSerializer(serializers.Serializer):
    wallet_address = serializers.CharField(required=True)
    signature = serializers.CharField(required=True)
    invite_code = serializers.CharField(required=True)