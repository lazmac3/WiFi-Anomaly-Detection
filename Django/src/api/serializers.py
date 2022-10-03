# myapi/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Prediction
from .models import Attack

class CreateUserSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		return user
	class Meta:
		model = User
		fields = ('id', 'username', 'password')
		extra_kwargs = {
			'password': {'write_only': True}
		}


		
class PredictionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Prediction
		fields = ('predicted')
		
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')
        
class AttackSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Attack
		fields = ('wlan_tag_length', 'wlan_country_info_fnm', 'wlan_da', 'wlan_sa', 'wlan_bssid', 'ip_src', 'ip_dst', 'wlan_fixed_reason_code', 'radiotap_channel_freq', 'udp_length')
		

