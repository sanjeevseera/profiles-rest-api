from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from . import permissions
from rest_framework import filters


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

class HellowViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hellow message"""

        a_viewset = [
            'User_action (list, creation, retrieve, update, partial_update and destroy)',
            'Automatically maps to URLS using routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a New hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an objects by id ID"""
        return Response({"http_method": 'GET'})

    def update(self, request, pk=None):
        """Handle update an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle update part an object"""
        return Response({'http_method': 'PATCHT'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profile"""
    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfilePermissions,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')