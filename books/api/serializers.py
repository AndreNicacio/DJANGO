from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from books import models

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'
