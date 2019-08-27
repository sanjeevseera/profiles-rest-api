from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """ Returns A list API Views"""

        an_apiview = [
            'User HTTP methods as function (get, put, post, patch, delete)',
            'Is Similar to additional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', "an_apiview": an_apiview})

