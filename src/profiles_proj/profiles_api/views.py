from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from rest_framework import status
# Create your views here.
class HelloApiView(APIView):
    """Test api view functionality"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return list of features api offers"""

        an_apiview = [
            'Uses HTTP Methods as function - get,post,put,delete,patch',
            'Similar to a traditional django view',
            'Mapped manually to URLs'
        ]

        return Response({'message': 'Hello people!', 'an_apiview': an_apiview})

    def post(self, request):
        """ Create Hello message with name """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data['name']
            message = 'Hello {}!'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles update of object"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """ Handles updates to fields provided in req"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """ Handles delete of an object"""

        return Response({'method': 'delete'})

class HelloViewSets(viewsets.ViewSet):
    """Test api view sets """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return hello message """

        a_viewset = [
            'uses actions like list,create,retrieve, update, partial_update',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """ To create a new hello msg """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data['name']
            message = 'Hello {}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handles getting object by ID """

        return Response({'http_meth': 'get'})

    def update(self, request, pk=None):
        """ Handles update of object """

        return Response({'http_meth': 'put'})

    def partial_update(self, request, pk=None):
        """ Handles partial updates to an object """

        return Response({'http_meth': 'patch'})

    def destroy(self, request, pk=None):
        """ Handles delete of objects """

        return Response({'http_meth': 'delete'})
