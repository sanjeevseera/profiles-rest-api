from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns A list API Views"""

        an_apiview = [
            'User HTTP methods as function (get, put, post, patch, delete)',
            'Is Similar to additional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', "an_apiview": an_apiview})

    def post(self, request):
        """"Creates a Hello message with our name"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle Update an Object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial Update an Object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """"Delete an object"""
        return Response({'method': 'DELETE'})
