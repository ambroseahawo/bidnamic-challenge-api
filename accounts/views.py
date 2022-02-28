from django.shortcuts import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from accounts.serializers import UserModelSerializer

# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class DeleteAccount(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        current_user = request.user
        current_user.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
