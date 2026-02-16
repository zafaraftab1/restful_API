from django.views import View
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .import serializers,models,permissions
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .models import ProfileFeedItem
from .serializers import ProfileFeedSerializer




# Create your views here.


def standardized_response(message, data=None, success=True, http_status=status.HTTP_200_OK):
    """Return a standardized DRF Response payload.

    Args:
        message (str): Human-readable message.
        data (optional): Optional data payload (dict, list, etc.).
        success (bool): Whether the response denotes success.
        http_status (int): HTTP status code for the response.
    """
    payload = {
        'success': success,
        'message': message,
    }
    if data is not None:
        payload['data'] = data
    return Response(payload, status=http_status)


class home(View):
    def get(self,request):
        return render (request,'home.html')

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to urls'
        ]

        return standardized_response('Hello!', {'an_apiview': an_apiview})

    def post(self, request):
        """Created a hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object/only update fields provided in the request"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object."""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses Action (List, Create, Update, Patch, Delete)'
            'Automatically maps to URLs using Routers'
            'Provides more functionality with less code'
        ]

        return standardized_response('Hello!', {'an_apiview': an_apiview})

    def create(self, request):
        """Create a new hello message"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating reading and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnPermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""
    serializer_class = AuthTokenSerializer

    def create(self,request):
        """Use the ObtainAuthToken class to create a new token"""
        return ObtainAuthToken().as_view()(request._request)

class ProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus,IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged-in user"""
        serializer.save(user_profile=self.request.user)