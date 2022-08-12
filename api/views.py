from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Movie
from .serializers import MovieSerializer, UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class MovieList(generics.ListCreateAPIView):
    """
    List all Movies, or create a new one
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, *kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, *kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a movie object
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly,
                           IsOwnerOrReadOnly]

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, *kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, *kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
