from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """Test api view functionality"""

    def get(self, request, format=None):
        """Return list of features api offers"""

        an_apiview = [
            'Uses HTTP Methods as function - get,post,put,delete,patch',
            'Similar to a traditional django view',
            'Mapped manually to URLs'
        ]

        return Response({'message': 'Hello people!', 'an_apiview': an_apiview})
