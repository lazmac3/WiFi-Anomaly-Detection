from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
import requests

from .serializers import CreateUserSerializer

#I took this oAuth from Stelios' Cloud computing module, hard coding for my purposes below

	
CLIENT_ID = 'lv4D3ovZlgKnbzMlALGXupcua917Y9InNs7XNfSy'
CLIENT_SECRET = '47C7UPW6uX3sdg2xbgBUpfLCFuWV4ooC8GRZ5j5YBKiK7KQiUTc0LcsOiipThjosAfBixzBN9GuRtwq6FNn0DfcWeNunfDuzdRhtShlRgh0TzO25zeddOf73zTiXkhxL'


IP_token = 'http://127.0.0.1:8000/o/token/'
IP_revoke_token ='http://127.0.0.1:8000/o/revoke_token/'
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    # Put the data from the request into the serializer 
    serializer = CreateUserSerializer(data=request.data) 
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save() 
        # Then we get a token for the created user.
        # This could be done differentley 
        r = requests.post(IP_token, 
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(r.json())
    return Response(serializer.errors)



@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    r = requests.post(
    IP_token, 
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())



@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    r = requests.post(
    IP_token, 
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        IP_revoke_token, 
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise) 
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)
    
    
    
# Create your views here.
from rest_framework import viewsets


	
from .serializers import PredictionSerializer
from .models import Prediction
class PredictionViewset(viewsets.ModelViewSet):
	queryset = Prediction.objects.all()
	serializer_class = PredictionSerializer

from .serializers import UserSerializer
from django.contrib.auth.models import User	
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
from .serializers import AttackSerializer
from .models import Attack
class AttackViewset(viewsets.ModelViewSet):
	queryset = Attack.objects.all()
	serializer_class = AttackSerializer

	

def predictionRender(request): 
	user_list=User.objects.all()
	attack_list=Attack.objects.all().order_by('-created_at')
	return render(request,'predWebpage.html',{'attack':attack_list, 'users':user_list})
