from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from.models import Enquiry
from django.contrib.auth.models import User

class UserSerilizer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EnquirySerilizer (serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'