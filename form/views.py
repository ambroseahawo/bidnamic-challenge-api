from django.shortcuts import get_object_or_404, HttpResponse
from rest_framework.decorators import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from form.models import Form
from form.serializers import FormDetailsSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

# Create your views here.
class ListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_details = Form.objects.all().filter(user_id=request.user.id)
        serializer = FormDetailsSerializer(user_details, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, format=None, form=None):
        # copy request.data to allow mutability
        query_dict = request.data.copy()
        
        # validate date of birth submitted 
        date = query_dict['dob']
        birth_date = datetime.strptime(date, '%d/%m/%Y')
        age = (datetime.now() - birth_date).days/365
        
        query_dict['user'] = request.user.id
        
        serializer = FormDetailsSerializer(data=query_dict)

        if serializer.is_valid():
            if age < 18:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        db_data = get_object_or_404(Form, id=pk)
        return db_data
    
    def get(self, request, pk):
        user_details = self.get_object(pk)
        serializer = FormDetailsSerializer(user_details)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None, form=None):
        query_dict = request.data.copy()
        user_details = self.get_object(pk)

        # validate date of birth submitted
        date = query_dict['dob']
        birth_date = datetime.strptime(date, '%d/%m/%Y')
        age = (datetime.now() - birth_date).days/365

        query_dict['user'] = request.user.id
        serializer = FormDetailsSerializer(user_details, data=query_dict)

        if serializer.is_valid():
            if age < 18:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_details = self.get_object(pk)
        user_details.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
