import secrets

from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from auth.models import User, InviteCode
from auth.serializers import VerifySignatureSerializer
from utils.messages import AuthMessages


# Create your views here.
class GenerateNonceView(APIView):
    def post(self, request):
        wallet_address = request.query_params.get("wallet_address")
        if not wallet_address:
            return Response({"error": "Wallet address is required"}, status=status.HTTP_400_BAD_REQUEST)

        user, _ = User.objects.get_or_create(wallet_address=wallet_address, is_active=False)
        user.nonce = secrets.token_hex(16)
        user.save()

        message = AuthMessages.get_message(user.nonce)
        return Response({"message": message})


class VerifySignatureView(APIView):
    serializer_class = VerifySignatureSerializer

    def post(self, request):
        serializer = self.serializer_class(request.data)
        serializer.is_valid(raise_exception=True)
        wallet_address = serializer.data.get('wallet_address')
        signature = serializer.data.get('signature')

        user = get_object_or_404(User, wallet_address=wallet_address)

        message = f"Sign this message to authenticate: {user.nonce}"
        message_hash = AuthMessages.hash_message(message)

        recovered_address = AuthMessages.recover_message(message_hash, signature=signature)

        if recovered_address.lower() != wallet_address.lower():
            return Response({"error": "Invalid signature"}, status=status.HTTP_403_FORBIDDEN)

        refresh = RefreshToken.for_user(user)
        user.nonce = None
        user.save()
        return Response({
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh)
        })


class CreateInviteView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        invite = InviteCode.objects.create()
        return Response({"invite_code": invite.code})


class CheckInviteView(APIView):
    def get(self, request, code):
        invite = InviteCode.objects.filter(code=code, is_used=False).first()
        if invite:
            return Response({"valid": True})
        return Response({"valid": False}, status=status.HTTP_400_BAD_REQUEST)

class GetCurrentUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return request.user
