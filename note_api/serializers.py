from rest_framework import serializers
from .models import *


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password' : { 'write_only': True }}

class CategoryPlainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {'user': {'read_only':True}}

class NoteDescriptiveSerializer(serializers.ModelSerializer):
    category = CategoryPlainSerializer(many=False, read_only=True)

    class Meta:
        model = Note
        fields = '__all__'
        extra_kwargs = {'category': {'read_only':True}, 'user': {'read_only':True}}

class CategoryDescriptiveSerializer(serializers.ModelSerializer):
    note = NoteDescriptiveSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'