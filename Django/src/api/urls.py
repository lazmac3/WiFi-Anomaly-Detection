#api/urls.py
from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views

router = routers.DefaultRouter()
router.register('attack', views.AttackViewset)
urlpatterns = [
	path('register/', views.register),
	path('token/', views.token),
	path('token/refresh/', views.refresh_token),
	path('token/revoke/', views.revoke_token),
	path('', include(router.urls)),
	path('predictions/', views.predictionRender, name='api'),
]
