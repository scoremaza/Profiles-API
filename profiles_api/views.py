from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View """

    def get(self, request, format=None):
        """
       Profile_API version 0.0.0

        Parameters:

        -request (--request):  REST framework's Request instances
        -format (--format): Return an HTML-formatted representation 
        of the resource when that resource is requested by a web browser

        Returns:
        -A List of APIView Features
        """
        an_apiview = [
            'Uses HTTP methods as function (get, post patch put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})