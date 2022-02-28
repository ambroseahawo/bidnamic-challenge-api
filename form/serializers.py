from rest_framework import serializers
from form.models import Form

class FormDetailsSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y',])
    class Meta:
        model = Form
        fields = ['title', 'first_name', 'surname', 'dob', 'user',
                  'company_name', 'address', 'telephone', 'bid',
                  'google_id', 'id']
        extra_kwargs = {
            'id': {'read_only': True},
        }
