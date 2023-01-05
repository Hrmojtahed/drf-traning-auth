from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.views import Response, status
from profiles_api import serializer
from rest_framework import viewsets

from profiles_api.models import UserProfile
from profiles_api.permissions import UpdateOwnProfile
from profiles_api.serializer import UserProfileSerializer


class TestApiView(APIView):
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        return Response({'message': 'hello world!'})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({'message': 'list of viewset'})

    def create(self,request):

        return Response({'message':'post of viewset'})


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (SearchFilter,)
    search_fields = ('name','email',)
