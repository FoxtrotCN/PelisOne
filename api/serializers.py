from rest_framework import serializers
from .models import Movie
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'synopsis', 'genre']

    def create(self, validated_data):
        """
        Create and return a new `Movie` instance, given the validated data.
        """
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Movie` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.synopsis = validated_data.get('synopsis', instance.synopsis)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'movies']

