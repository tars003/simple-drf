from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Categories, Articles
from .serializers import CategorySerializer, ArticleSerializer

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class CategoryView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )


class ArticleView(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


class GoogleView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}  # validate the token
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        # create user if not exist
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.save()

        # token = RefreshToken.for_user(user)  # generate token without username & password

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        response = {}
        response['username'] = user.username
        response['access_token'] = str(token)
        # response['refresh_token'] = str(token)
        return Response(response)


