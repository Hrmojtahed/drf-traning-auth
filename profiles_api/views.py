from rest_framework.views import APIView
from rest_framework.views import Response, status
from profiles_api import serializer
from rest_framework import viewsets


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
