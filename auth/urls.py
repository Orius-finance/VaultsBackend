from django.urls import path
from .views import GenerateNonceView, VerifySignatureView, CreateInviteView, CheckInviteView

urlpatterns = [
    path('auth/nonce/', GenerateNonceView.as_view(), name='generate-nonce'),
    path('auth/login/', VerifySignatureView.as_view(), name='verify-signature'),
    path('auth/invite/create/', CreateInviteView.as_view(), name='create-invite'),
    path('auth/invite/check/<str:code>/', CheckInviteView.as_view(), name='check-invite'),
    path('auth/users/me', name='get-user'),
]
