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
            try:
                queryset = User.objects.get(id=id)
            except User.DoesNotExist:
                return Response({'errors': 'This todo item does not exist.'}, status=400)

            read_serializer = UserSerializer(queryset)

        else:
            queryset = User.objects.all()
            read_serializer = UserSerializer(queryset, many=True)
        return Response(read_serializer.data)

    def post(self, request):
        """_summary_

        Args:
            request (_type_): _description_
        """
        create_serializer = UserSerializer(data=request.data)
        if create_serializer.is_valid():
            user_item_object = create_serializer.save()
            read_serializer = UserSerializer(user_item_object)
            return Response(read_serializer.data, status=201)
        return Response(create_serializer.errors, status=400)

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
