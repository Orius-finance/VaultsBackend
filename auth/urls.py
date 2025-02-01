from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import GenerateNonceView, VerifySignatureView, CreateInviteView, CheckInviteView, GetCurrentUser

urlpatterns = [
    path('auth/nonce/', GenerateNonceView.as_view(), name='generate-nonce'),
    path('auth/login/', VerifySignatureView.as_view(), name='verify-signature'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('auth/invite/create/', CreateInviteView.as_view(), name='create-invite'),
    path('auth/invite/check/<str:code>/', CheckInviteView.as_view(), name='check-invite'),
    path('auth/users/me', GetCurrentUser.as_view(), name='get-user'),
]
