from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from .models import User
from .serializers import UserSerializer

# Create your views here.


class UserView(APIView, UpdateModelMixin, DestroyModelMixin):
    """_summary_

    Args:
        APIView (_type_): _description_
        UpdateModelMixin (_type_): _description_
        DestroyModelMixin (_type_): _description_
    """

    def get(self, request, id=None):
        """_summary_
        """
        if id:
            # If an id is provided in the GET request, retrieve the Todo item by that id
            try:
                # Check if the todo item the user wants to update exists
                queryset = User.objects.get(id=id)
            except User.DoesNotExist:
                # If the todo item does not exist, return an error response
                return Response({'errors': 'This todo item does not exist.'}, status=400)

            # Serialize todo item from Django queryset object to JSON formatted data
            read_serializer = UserSerializer(queryset)

        else:
            # Get all todo items from the database using Django's model ORM
            queryset = User.objects.all()

            # Serialize list of todos item from Django queryset object to JSON formatted data
            read_serializer = UserSerializer(queryset, many=True)

        # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)

    def post(self, request):
        """_summary_

        Args:
            request (_type_): _description_
        """
        pass

    def put(self, request, id=None):
        """_summary_

        Args:
            request (_type_): _description_
            id (_type_, optional): _description_. Defaults to None.
        """
        pass

    def delete(self, request, id=None):
        """_summary_

        Args:
            request (_type_): _description_
            id (_type_, optional): _description_. Defaults to None.
        """
        pass
