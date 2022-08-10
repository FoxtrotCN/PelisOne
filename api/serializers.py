from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=200)
    synopsis = serializers.CharField(style={'base_template': 'textarea.html'})
    genre = serializers.ChoiceField(choices=Movie.GENRE_CHOICES, default='')

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

