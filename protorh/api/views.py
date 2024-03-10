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
        pass

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
