from unicodedata import name
from django.urls import path, include
from accounts.views import UserModelViewSet, DeleteAccount
from rest_framework.routers import DefaultRouter

app_name = "accounts"

router = DefaultRouter()
# takes three parameters - prefix, viewset, basename=None
router.register('', UserModelViewSet, )

urlpatterns = [
    path('delete/', DeleteAccount.as_view(), name='delete-users'),
    path('', include(router.urls)),
]

